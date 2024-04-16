class Queries:
    CREATE_SERVICE_TABLE = """
        CREATE TABLE IF NOT EXISTS service (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            number VARCHAR, 
            date DATETIME,
            quality TEXT,
            cleanable TEXT,
            last TEXT
        )
    """