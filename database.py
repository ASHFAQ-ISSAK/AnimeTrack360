import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        # Establish a connection to the database
        self.connection = sqlite3.connect(self.db_name)
        # Create necessary tables if they don't exist
        create_anime_table = """
        CREATE TABLE IF NOT EXISTS anime (
            anime_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            genre TEXT,
            episode_count INTEGER,
            status TEXT
        )
        """
        create_reviews_table = """
        CREATE TABLE IF NOT EXISTS reviews (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            anime_id INTEGER,
            rating INTEGER,
            comment TEXT,
            FOREIGN KEY (anime_id) REFERENCES anime (anime_id)
        )
        """
        cursor = self.connection.cursor()
        cursor.execute(create_anime_table)
        cursor.execute(create_reviews_table)
        self.connection.commit()

    def disconnect(self):
        # Close the database connection
        self.connection.close()

    def execute_query(self, query, params=None):
        # Execute the provided SQL query on the database
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()

    def add_anime(self, title, description, genre, episode_count, status):
        # Add a new anime to the database
        query = (
            "INSERT INTO anime (title, description, genre, episode_count, status) "
            "VALUES (?, ?, ?, ?, ?)"
        )
        params = (title, description, genre, episode_count, status)
        self.execute_query(query, params)

    def add_user(self, username, email, favorite_anime):
        # Add a new user to the database
        query = (
            "INSERT INTO users (username, email, favorite_anime) " "VALUES (?, ?, ?)"
        )
        params = (username, email, favorite_anime)
        self.execute_query(query, params)

    def add_review(self, anime_id, rating, comment):
        # Add a new review to the database
        query = "INSERT INTO reviews (anime_id, rating, comment) VALUES (?, ?, ?)"
        params = (anime_id, rating, comment)
        self.execute_query(query, params)

    def delete_review(self, review_id):
        # Delete a review from the database based on its ID
        query = f"DELETE FROM reviews WHERE review_id = {review_id}"
        self.execute_query(query)

    def delete_anime(self, anime_id):
        # Delete an anime from the database based on its ID
        query = f"DELETE FROM anime WHERE anime_id = {anime_id}"
        self.execute_query(query)
