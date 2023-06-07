class Review:
    def __init__(self, review_id, anime_id, rating, comment):
        self.review_id = review_id
        self.anime_id = anime_id
        self.rating = rating
        self.comment = comment

    def get_review_details(self):
        # Retrieve and display review details
        print(f"Review ID: {self.review_id}")
        print(f"Anime ID: {self.anime_id}")
        print(f"Rating: {self.rating}")
        print(f"Comment: {self.comment}")
