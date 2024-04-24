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
    CREATE_KINDS_TABLE = """
            CREATE TABLE IF NOT EXISTS kinds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        """
    CREATE_FOOD_TABLE = """
            CREATE TABLE IF NOT EXISTS food (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                author TEXT,
                price INTEGER,
                picture TEXT,
                kind_id INTEGER,
                FOREIGN KEY (kind_id) REFERENCES kinds(id)
            )
        """
    DROP_KINDS_TABLE = "DROP TABLE IF EXISTS kinds"
    DROP_FOOD_TABLE = "DROP TABLE IF EXISTS food"
    POPULATE_KINDS = """
            INSERT INTO kinds (name) VALUES ('десерт'),
            ('второе'), ('закуска'), ('суп')
        """
    POPULATE_FOOD = """
            INSERT INTO food (name, author, price, picture, kind_id) VALUES 
            ('Тирамису', 'Итальянская кухня', 300, 'images/tiramisu.jpg', 1),
            ('Бефстроганов', 'Русская кухня', 500, 'images/beef_strogonaff.jpg', 2),
            ('Гуакамоле', 'Мексиканская кухня', 250, 'images/guacamole.jpg', 3),
            ('Чизкейк', 'Американская кухня', 350, 'images/cheese.jpeg', 1),
            ('Пицца', 'Итальянская кухня', 400, 'images/pizza.jpg', 2),
            ('Салат Цезарь', 'Американская кухня', 200, 'images/chezar.jpg', 3),
            ('Борщ', 'Украинская кухня', 180, 'images/borsh.webp', 4),
            ('Тирамису 2', 'Итальянская кухня', 320, 'images/tiramisu2.jpg', 1),
            ('Паста карбонара', 'Итальянская кухня', 450, 'images/pasta.jpg', 2),
            ('Греческий салат', 'Греческая кухня', 220, 'images/salat.jpg', 3),
            ('Суп из лапши рамен', 'Японская кухня', 200, 'images/ramen.jpg', 4)
        """
