import click
from black import format_str, FileMode

from . import bcc
from . import elf
from . import program


def handle_program_text(ctx, param, value) -> str:
    if value.startswith("@"):
        with open(value[1:]) as f:
            value = f.read()
    return value


def handle_extra_vars(ctx, param, value) -> dict:
    res = {}
    if not value:
        return res
    for val in value.split(","):
        k, v = val.split("=", 1)
        res[k] = v
    return res


@click.group(
    context_settings=dict(help_option_names=["-h", "--help"]),
    invoke_without_command=True,
)
@click.pass_context
@click.option(
    "-t",
    "--target",
    help="golang binary to trace",
)
@click.option(
    "-e",
    "--extra-vars",
    callback=handle_extra_vars,
    help="extra variables to render bcc script, e.g. -e sym_pid=233,real_target=/path/to/bin",  # noqa
)
@click.option("-o", "--output", help="output filename", default="trace.bcc.py")
@click.option(
    "-p",
    "--program-text",
    nargs=1,
    default="",
    callback=handle_program_text,
)
def main(
    ctx,
    target: str,
    program_text: str,
    extra_vars: dict[str, str],
    output: str,
):
    if ctx.invoked_subcommand is not None:
        return

    extra_vars.setdefault("real_target", target)
    trace_uprobes = program.parse(program_text)
    elf_interpreter = elf.Interpreter(target)
    print(
        format_str(
            bcc.render(trace_uprobes, elf_interpreter, extra_vars),
            mode=FileMode(),
        ),
        file=open(output, "w"),
    )
    print(f"generated {output}")
