import socket
from collections import namedtuple
from urllib.parse import urlparse

REMOTE = namedtuple('REMOTE', ['scheme', 'hostname', 'address', 'port', 'resource', 'ssl'])


def parses(url: str) -> REMOTE:
    url = urlparse(url)
    scheme = url.scheme
    hostname = url.hostname
    address = socket.gethostbyname(hostname)
    port = url.port or (443 if scheme == 'wss' else 80)
    resource = url.path
    ssl = True if scheme == 'wss' else False
    if url.query:
        resource += '?' + url.query
    return REMOTE(scheme, hostname, address, port, resource, ssl)


res = parses("ws://echo.websocket.org?sign=i9878")
print(res.address, res.port, res.resource)