class Queries:
    CREATE_SERVICE_TABLE = """
        CREATE TABLE IF NOT EXISTS service (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            number INTEGER, 
            date INTEGER,
            quality INTEGER,
            cleanable INTEGER,
            last TEXT
        )
    """