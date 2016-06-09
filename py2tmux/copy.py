import re
import os
import shutil

from .constants import PY2TMUX_PRJ_DIR


def copy_py2tmux(target_directory):
    """
    Copy the py2tmux codebase, replacing the package name as approprate.

    """
    print "Copying to {}".format(target_directory)
    package_name = os.path.basename(target_directory)
    # copy the codebase
    shutil.copytree(PY2TMUX_PRJ_DIR, target_directory,
                    ignore=lambda d, f: ['.git'])
    # remove any lingering temp files
    remove_pyc_and_egg_infos(target_directory)
    # replace py2tmux and PY2TMUX as appropriate
    replace_py2tmux(target_directory, package_name)
    # move the package folder
    shutil.move(
        os.path.join(target_directory, 'py2tmux'),
        os.path.join(target_directory, package_name)
    )


def remove_pyc_and_egg_infos(target_directory):
    """
    Remove all the pyc and egg-info files
    """

    def remove_if_pyc_or_egg_info(path):
        if path.endswith('.pyc'):
            print "removing {}".format(path)
            os.unlink(path)
        elif path.endswith('.egg-info'):
            print "removing {}".format(path)
            shutil.rmtree(path)

    def remove_in_walk_callback(_, dirname, fnames):
        for f in fnames:
            path = os.path.join(dirname, f)
            remove_if_pyc_or_egg_info(path)

    walk_all(target_directory,
             remove_in_walk_callback,
             None,)


def replace_py2tmux(target_directory, package_name):
    """
    Replace all instances of py2tmux and PY2TMUX in the
    full project
    """

    def replace(path):
        print "replacing py2tmux in {}".format(path)
        replace_py2tmux_in_file(path, 'py2tmux', package_name)
        replace_py2tmux_in_file(path, 'PY2TMUX', package_name.upper())

    def remove_in_walk_callback(_, dirname, fnames):
        for f in fnames:
            path = os.path.join(dirname, f)
            if os.path.isfile(path):
                replace(path)

    walk_all(target_directory,
             remove_in_walk_callback,
             None,)


def replace_py2tmux_in_file(filepath, searchfor, replacement):
    """
    Rewrite a file after doing a search-and-replace. See
    `search_and_replace` for details
    """
    print "Replacing in {}".format(filepath)
    with open(filepath, 'r') as f:
        content = f.read()
    replaced_content = search_and_replace(content, searchfor, replacement)
    with open(filepath, 'w') as f:
        f.write(replaced_content)


def search_and_replace(content, searchfor, replacement):
    """
    Search for a string `searchfor` (which is assumed to be evaluatable as a
    regexp) in a string `content` and replace all instances with `replacement`.
    Return the result.
    """
    rx = re.compile(searchfor)
    return rx.sub(replacement, content)


def walk_all(dirname, func, arg):
    """
    Wrapper around os.path.walk that also walks the top level
    """
    func(arg, dirname, os.listdir(dirname))
    os.path.walk(dirname, func, arg)
