class Anime:
    def __init__(self, anime_id, title, description, genre, episode_count, status):
        self.anime_id = anime_id
        self.title = title
        self.description = description
        self.genre = genre
        self.episode_count = episode_count
        self.status = status

    def get_anime_details(self):
        # Retrieve and display anime details
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Episodes: {self.episode_count}")
        print(f"Status: {self.status}")
        print("---")
        print(f"Description:\n{self.description}")

    def update_anime_status(self, new_status):
        # Update the status of the anime
        self.status = new_status
