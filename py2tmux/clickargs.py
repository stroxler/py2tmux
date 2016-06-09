"command line args for py2tmux"
import click


EXISTING_FILE = click.Path(exists=True, file_okay=True, dir_okay=False)


def session():
    return click.option(
        '--session', '-s', type=str, required=True,
        help="Target session. Must already be running"
    )


def input_file():
    return click.option(
        '--input-file', '-if', type=EXISTING_FILE,
        help="File to send as input. If None, stdin is used",
        default=None,
        show_default=True,
    )


def line():
    return click.option(
        '--line', '-l', type=str, required=True,
        help="Line to send as input. A newline is appended.",
    )
