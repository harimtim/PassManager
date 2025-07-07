import sqlite3

class SQLHandler:
    def __init__(self, filename):
        self.filename = filename
        self.author = "harimtim"
        self.date = "07.07.2025"
        self.github = "https://github.com/harimtim/PassManager"
        self.db = sqlite3.connect(self.filename)
        self.cur = self.db.cursor()
        self.table_name = "PassManager"
        self.init()#

    def init(self):
        self.cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account TEXT NOT NULL,
                password TEXT NOT NULL
            )
            """
        )
        self.db.commit()

    def showall(self):
        result = self.cur.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return result.fetchall()
    
    def add(self, account: str, password: str):
        add_sql = self.cur.execute(
            f"INSERT INTO {self.table_name} (account, password) VALUES (?, ?)",
            (account, password)
        )
        self.db.commit()

    def delete(self, account):
        ...

    def close(self):
        self.db.commit()
        self.db.close()

    def reset(self):
        self.cur.execute("DROP TABLE {}".format(self.table_name))
        self.db.commit()
        self.init()
