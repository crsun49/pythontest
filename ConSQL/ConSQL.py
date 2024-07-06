import pyodbc

class SQLServerDB:
    def __init__(self):
        self.server = "ODC--ZLQTEWAZKP\SQLEXPRESS"
        self.database = "pythontest"
        self.username = "sa"
        self.password = "95938"
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                f'SERVER={self.server};'
                f'DATABASE={self.database};'
                f'UID={self.username};'
                f'PWD={self.password}'
            )
            self.cursor = self.conn.cursor()
            print("Connected to SQL Server")
        except pyodbc.Error as e:
            print(f"Error connecting to SQL Server: {e}")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            print("Query executed successfully")
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()

    def fetch_data(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except pyodbc.Error as e:
            print(f"Error fetching data: {e}")
            return None

    def insert_data(self, table, columns, data):
        try:
            placeholders = ','.join(['?' for _ in columns])
            query = f"INSERT INTO {table} ({','.join(columns)}) VALUES ({placeholders})"
            self.cursor.executemany(query, data)
            self.conn.commit()
            print(f"Inserted {self.cursor.rowcount} rows into {table}")
        except pyodbc.Error as e:
            print(f"Error inserting data: {e}")
            self.conn.rollback()

    def update_data(self, table, update_dict, condition, params=None):
        try:
            set_clause = ','.join([f"{key} = ?" for key in update_dict.keys()])
            query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
            values = list(update_dict.values())
            if params:
                values.extend(params)
            self.cursor.execute(query, values)
            self.conn.commit()
            print(f"Updated {self.cursor.rowcount} rows in {table}")
        except pyodbc.Error as e:
            print(f"Error updating data: {e}")
            self.conn.rollback()

    def delete_data(self, table, condition, params=None):
        try:
            query = f"DELETE FROM {table} WHERE {condition}"
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            print(f"Deleted {self.cursor.rowcount} rows from {table}")
        except pyodbc.Error as e:
            print(f"Error deleting data: {e}")
            self.conn.rollback()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Disconnected from SQL Server")

# # Example usage:
# if __name__ == "__main__":
#     # Replace with your SQL Server connection details
#     server = 'your_server'
#     database = 'your_database'
#     username = 'your_username'
#     password = 'your_password'
#
#     db = SQLServerDB()
#
#     # Example: Insert multiple rows
#     data_to_insert = [
#         ('John', 'Doe', 'john.doe@email.com'),
#         ('Jane', 'Smith', 'jane.smith@email.com')
#     ]
#     db.insert_data('Users', ['FirstName', 'LastName', 'Email'], data_to_insert)
#
#     # Example: Update data
#     update_params = {'FirstName': 'Johnny'}
#     db.update_data('Users', update_params, 'LastName = ?', ['Doe'])
#
#     # Example: Delete data
#     db.delete_data('Users', 'LastName = ?', ['Smith'])
#
#     # Example: Select data
#     rows = db.fetch_data('SELECT * FROM Users')
#     if rows:
#         for row in rows:
#             print(row)