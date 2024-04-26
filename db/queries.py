class Queries:
    CREATE_SERVICE_TABLE = """
        CREATE TABLE IF NOT EXISTS service (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age VARCHAR, 
            salary_or_grade TEXT,
            occupation TEXT
        )
    """
