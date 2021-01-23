import tempfile
import logging
import sqlite3
import socket
import pytest
import socketserver
import whogoesthere.connections
import time

def stall(duration, reason):
    logging.info(f'stalling {duration} seconds for: {reason}')
    time.sleep(duration)

@pytest.fixture
def logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


@pytest.fixture
def database():
    with tempfile.NamedTemporaryFile() as f:
        logging.info(f'creating a SQLite database at {f.name}')
        yield sqlite3.connect(f.name)

@pytest.fixture
def servers():
    PORT = 7777
    servers = []
    for host in [f'127.0.33.{100 + i}' for i in range(3)]:
        logging.info(f'setting up server to listen on {(host, PORT)}')
        server = socketserver.TCPServer((host, PORT), socketserver.BaseRequestHandler)
        servers.append(server)

    yield servers

    for server in servers:
        server.server_close()


def connect_sockets(servers):
    logging.info(f'connecting sockets to {[s.server_address for s in servers]}')
    sockets = []
    for host in servers:
        sock = socket.socket()
        sock.connect(host.server_address)
        sockets.append(sock)

def test_accumulate_connections(logger, database, servers):
    connections = whogoesthere.connections.Connections(database)
    connections.create_table()
    results = database.execute(f'SELECT * FROM {connections.table_name}')
    assert list(results) == []

    connect_sockets(servers)

    connections.monitor()
    stall(5, 'monitoring to see connections')


    results = database.execute(f'SELECT * FROM {connections.table_name}')
    results = list(results)
    assert len(results) >= len(servers)
    assert_all_connections_found(results, servers)

def assert_all_connections_found(results, servers):
    actual = set()
    for result in results:
        _, local_ip, local_port, remote_ip, remote_port = result
        actual.add((remote_ip, remote_port))

    for expected in servers:
        assert expected.server_address in actual
