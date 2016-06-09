# Python communication with tmux

Tools to send lines or file contents to tmux sessions
from python and from the command line. This is mainly
a wrapper around the `tmux send-keys` command to make
it suitable for programmatic use from python or, via
the command line, from other programs.

This is not a python tool for wrapping tmux in general; see
`pytmux` for a package that uses python for configuring tmux
sessions.


## why py2tmux?

My main motivation is text editing: I want an easy way to send arbitrary
content (I'm willing to live with just ascii content) to running terminal
sessions, without worrying about terminal emulation.

The workflow I'm picturing is an open terminal side-by-side with an emacs or
vim session, and a key binding in the editor that lets you send text as if it
were copy-pasted from the text editor.

Use cases include developing shell scripts in vim or emacs and wanting to
evaluate regions, or sending python commands to an ipython shell that you
dropped into from pudb (there are existing options for hooking up to a
dedicated ipython session, but I often use an embedded shell or a
pudb-instantiated ipython session in my development workflow).

I'm intending to release an emacs package and spacemacs layer that
makes use of `py2tmux`, although I make no promises if or when I'll
get to it.


## to install

Use pip. Since this is alpha software, I'd recommend an editable
install so you can fix bugs (don't worry, the codebase is tiny):
```
pip install -e .
```

## commands

List tmux sessions:
```
> py2tmux list-sessions
[out]
mysession: 1 windows (created Wed Jun  8 15:06:20 2016) [116x53] (attached)
```

Send content from stdin to a tmux session (in this case, it's running an
interactive ipython shell):
```
> py2tmux send-content -s mysession << EOF
x = 15
x ** 2
EOF
[out]
content sent
```
Note that nothing is echoed to this terminal; you'll see both the
content sent and the results in the tmux session itself, an any
evaluation of what your command did should be done there.

You can also send content from a file rather than stdin:
```
> py2tmux send-content -s mysession -if some_file.txt
[out]
content sent
```

Send a single line to a tmux session - this is more useful in some
situations where you don't want to deal with stdin or temp files:
```
> py2tmux send-line -s mysession -l "%run some_python_file.py"
[out]
line sent
```

## limitations

At present `py2tmux` is not suitable for communicating between windows
of the same tmux session, only for sending content to the active window
of a different session.
