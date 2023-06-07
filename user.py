class User:
    def __init__(self, user_id, username, email, favorite_anime):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.favorite_anime = favorite_anime

    def get_user_details(self):
        print("User Details:")
        print(f"User ID: {self.user_id}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Favorite Anime: {self.favorite_anime}")

    def update_favorite_anime(self, new_favorite_anime):
        self.favorite_anime = new_favorite_anime
