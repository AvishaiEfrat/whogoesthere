import tempfile
import sqlite3
import socket
import pytest
import whogoesthere.connections


@pytest.fixture
def database():
    with tempfile.NamedTemporaryFile() as f:
        yield sqlite3.connect(f.name)

def connect_sockets():
    HOSTS = ["google.com", "ubuntu.com", "stackoverflow.com"]
    HTTPS = 443
    sockets = []
    for host in HOSTS:
        sock = socket.socket()
        sock.connect((host, HTTPS))
        sockets.append(sock)

    return [sock.getpeername() for sock in sockets]

def test_accumulate_connections(database):
    connections = whogoesthere.connections.Connections(database)
    connections.create_table()
    results = database.execute(f'SELECT * FROM {connections.table_name}')
    assert list(results) == []
    peers = connect_sockets()


