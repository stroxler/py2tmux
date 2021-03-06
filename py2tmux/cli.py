"command line interface for py2tmux"
import sys
import click

import py2tmux.clickargs as clickargs
from .tmux import (
    list_sessions, send_content, send_full_line, send_tab_line, send_endl
)


@click.group()
def main():
    pass


@main.command('list-sessions')
def _list_sessions():
    """
    List active tmux sessions
    """
    for session in list_sessions():
        print session


@main.command('send-line')
@clickargs.session()
@clickargs.line()
def _send_line(session, line):
    """
    Send a single line of text from a file or stdin to a tmux session.

    A newline will be added at the end.
    """
    send_full_line(session, line)

@main.command('send-tab')
@clickargs.session()
@clickargs.line()
def _send_tab(session, line):
    """
    Send a single line of text from a file or stdin to a tmux session,
    with a tab added at the end.

    This is useful if you are talking to tmux from a text editor and you
    want to get tab completion

    """
    send_tab_line(session, line)


@main.command('send-content')
@clickargs.session()
@clickargs.input_file()
def _send_content(session, input_file):
    """
    Send a block of text from a file or stdin to a tmux session.

    A newline will be added at the end.
    """
    if input_file is None:
        send_content(session, sys.stdin)
    else:
        with open(input_file, 'r') as f:
            send_content(session, f)
    print "content sent"
