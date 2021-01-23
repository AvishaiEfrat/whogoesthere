import tempfile
import pytest
import logging
import sqlite3

@pytest.fixture(scope='session', autouse=True)
def logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


@pytest.fixture
def database():
    with tempfile.NamedTemporaryFile() as f:
        logging.info(f'creating a SQLite database at {f.name}')
        yield sqlite3.connect(f.name)
