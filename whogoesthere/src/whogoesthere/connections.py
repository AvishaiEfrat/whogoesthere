_CREATE_TABLE = """
CREATE TABLE {table_name} (
        id INTEGER PRIMARY KEY,
	local_ip TEXT NOT NULL,
        local_port INTEGER NOT NULL,
	remote_ip TEXT NOT NULL,
        remote_port INTEGER NOT NULL
);
"""

class Connections:
    def __init__(self, database):
        self._database = database
        self.table_name = 'connections'

    def create_table(self):
        create_command = _CREATE_TABLE.format(table_name = self.table_name)
        self._database.execute(create_command)
        self._database.commit()

    def monitor(self):
# this should run in a separate thread
        pass
