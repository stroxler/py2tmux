"Tools for sending tmux commands"
import sh


def list_sessions():
    return sh.tmux('ls').stdout.split('\n')


def send_content(session, f):
    """
    Given a file descriptor `f` (typically stdin or a text file), send its
    content to the tmux session `session` one line at a time, adding
    an extra endline.
    """
    for line in f:
        send_line(session, line)
    send_endl(session)


def send_line(session, line):
    sh.tmux('send-keys', '-t', session, '-l', line)


def send_endl(session):
    sh.tmux('send-keys', '-t', session, 'Enter')
