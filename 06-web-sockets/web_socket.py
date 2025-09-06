import socket
import ssl
from urllib.parse import urlparse


def parse_url(url: str):
    """Url parser implementation."""
    return urlparse(url)


def create_raw_socket(address_familiy, socket_kind):
    """Create a raw web socket."""
    return socket.socket(address_familiy, socket_kind)


def secure_socket(raw_socket, host):
    """Wraps a raw web socket in SSL."""
    return context.wrap_socket(raw_socket, server_hostname=host)


if __name__ == '__main__':

    url = 'https://nba.com'
    parsed = parse_url(url)

    host = parsed.hostname
    port = parsed.port or 443

    context = ssl.create_default_context()
    raw_socket = create_raw_socket(socket.AF_INET, socket.SOCK_STREAM)

    ssl_socket = secure_socket(raw_socket, host)
    ssl_socket.connect((host, port))

    print("Connected securely to '{0}' on port {1}".format(host, port))
    ssl_socket.close()
