# Copyright 2018 Streamlit Inc. All rights reserved.

"""A bunch of useful utilities."""

# Python 2/3 compatibility
from __future__ import print_function, division, unicode_literals, absolute_import
from streamlit.compatibility import setup_2_3_shims
setup_2_3_shims(globals())

# flake8: noqa
import base58
import contextlib
import errno
import functools
import os
import platform
import socket
import subprocess
import threading
import urllib
import uuid

try:
    import urllib.request  # for Python3
except ImportError:
    pass

from streamlit.logger import get_logger
LOGGER = get_logger(__name__)


STREAMLIT_ROOT_DIRECTORY = '.streamlit'

# Magic strings used to mark exceptions that have been handled by Streamlit's
# excepthook. These string should be printed to stderr.
EXCEPTHOOK_IDENTIFIER_STR = (
    'Streamlit has caught the following unhandled exception...')


# URL for checking the current machine's external IP address.
_AWS_CHECK_IP = 'http://checkip.amazonaws.com'


# URL of Streamlit's help page.
HELP_DOC = 'https://streamlit.io/secret/docs/'


def _decode_ascii(str):
    """Decodes a string as ascii."""
    return str.decode('ascii')


@contextlib.contextmanager
def streamlit_read(path, binary=False):
    """Opens a context to read this file relative to the streamlit path.

    For example:

    with read('foo.txt') as foo:
        ...

    opens the file `%s/foo.txt`

    path   - the path to write to (within the streamlit directory)
    binary - set to True for binary IO
    """ % STREAMLIT_ROOT_DIRECTORY
    filename = os.path.abspath(os.path.join(STREAMLIT_ROOT_DIRECTORY, path))
    if os.stat(filename).st_size == 0:
       raise Error('Read zero byte file: "%s"' % filename)

    mode = 'r'
    if binary:
        mode += 'b'
    with open(os.path.join(STREAMLIT_ROOT_DIRECTORY, path), mode) as handle:
        yield handle


@contextlib.contextmanager
def streamlit_write(path, binary=False):
    """
    Opens a file for writing within the streamlit path, and
    ensuring that the path exists. For example:

        with open_ensuring_path('foo/bar.txt') as bar:
            ...

    opens the file %s/foo/bar.txt for writing,
    creating any necessary directories along the way.

    path   - the path to write to (within the streamlit directory)
    binary - set to True for binary IO
    """ % STREAMLIT_ROOT_DIRECTORY
    mode = 'w'
    if binary:
        mode += 'b'
    path = os.path.join(STREAMLIT_ROOT_DIRECTORY, path)
    directory = os.path.split(path)[0]
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        with open(path, mode) as handle:
            yield handle
    except OSError as e:
        msg = ['Unable to write file: %s' % os.path.abspath(path)]
        if e.errno == errno.EINVAL and platform.system() == 'Darwin':
            msg.append('Python is limited to files below 2GB on OSX. '
                       'See https://bugs.python.org/issue24658')
        raise Error('\n'.join(msg))


def escape_markdown(raw_string):
    """Returns a new string which escapes all markdown metacharacters.

    Args
    ----
    raw_string : str
        A string, possibly with markdown metacharacters, e.g. "1 * 2"

    Returns
    -------
    A string with all metacharacters escaped.

    Examples
    --------
    ::
        escape_markdown("1 * 2") -> "1 \* 2"
    """
    metacharacters = ['\\', '*', '-', '=', '`', '!', '#', '|']
    result = raw_string
    for character in metacharacters:
        result = result.replace(character, '\\' + character)
    return result


def get_static_dir():
    dirname = os.path.dirname(os.path.normpath(__file__))
    return os.path.normpath(os.path.join(dirname, 'static'))


def memoize(func):
    """Decorator to memoize the result of a no-args func."""
    result = []
    @functools.wraps(func)
    def wrapped_func():
        if not result:
            result.append(func())
        return result[0]
    return wrapped_func


def write_proto(ws, msg):
    """Writes a proto to a websocket.

    Parameters
    ----------
    ws : WebSocket
    msg : Proto

    Returns
    -------
    Future
        See tornado.websocket.websocket_connect. This returns a Future whose
        result is a WebSocketClientConnection.
    """
    return ws.write_message(msg.SerializeToString(), binary=True)


def build_report_id():
    """Randomly generate a report ID."""
    return base58.b58encode(uuid.uuid4().bytes).decode("utf-8")


def make_blocking_http_get(url, timeout=5):
    try:
        return urllib.request.urlopen(url, timeout=timeout).read()
    except Exception:
        return None


_external_ip = None


def get_external_ip():
    """Get the *external* IP address of the current machine.

    Returns
    -------
    string
        The external IPv4 address of the current machine.

    """
    global _external_ip

    if _external_ip is not None:
        return _external_ip

    response = make_blocking_http_get(_AWS_CHECK_IP, timeout=5)

    if response is None:
        LOGGER.warning(
            'Did not auto detect external IP.\n'
            'Please go to %s for debugging hints.', HELP_DOC)
    else:
        _external_ip = response.decode('utf-8').strip()

    return _external_ip


_internal_ip = None


def get_internal_ip():
    """Get the *local* IP address of the current machine.

    From: https://stackoverflow.com/a/28950776

    Returns
    -------
    string
        The local IPv4 address of the current machine.

    """
    global _internal_ip

    if _internal_ip is not None:
        return _internal_ip

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't even have to be reachable
        s.connect(('8.8.8.8', 1))
        _internal_ip = s.getsockname()[0]
    except Exception:
        _internal_ip = '127.0.0.1'
    finally:
        s.close()

    return _internal_ip


def open_browser(url):
    """Open a web browser pointing to a given URL.

    We use this function instead of Python's `webbrowser` module because this
    way we can capture stdout/stderr to avoid polluting the terminal with the
    browser's messages. For example, Chrome always prints things like "Created
    new window in existing browser session", and those get on the user's way.

    url : str
        The URL. Must include the protocol.

    """

    system = platform.system()

    if system == 'Linux':
        cmd = ['xdg-open', url]
    elif system == 'Darwin':
        cmd = ['open', url]
    elif system == 'Windows':
        cmd = ['start', '""', url]
    else:
        raise Error('Cannot open browser in platform "%s"' % system)

    with open(os.devnull, 'w') as devnull:
        subprocess.Popen(cmd, stdout=devnull, stderr=subprocess.STDOUT)


def is_type(obj, fqn_type_str):
    """Check type without importing expensive modules.

    Parameters
    ----------
    obj : any
        The object to type-check.
    fqn_type_str : str
        The fully-qualified type string.

    Example
    -------

    To check whether somthing is a Matplotlib Figure without importing
    matplotlib, use:

    >>> is_type(foo, 'matplotlib.figure.Figure')

    """
    the_type = type(obj)
    module = the_type.__module__
    name = the_type.__name__
    return fqn_type_str == '%s.%s' % (module, name)


class Error(Exception):
    pass
