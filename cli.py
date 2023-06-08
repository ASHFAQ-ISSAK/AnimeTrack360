#! /usr/bin/env/ python3 

from database import Database
from anime import Anime
from review import Review
import pyfiglet
from colorama import init, Fore

color = 'green'


class CLI:
    def __init__(self):
        self.database = Database("anime_project.db")

    def show_menu(self):
        print("-------------------------------------")
        init(autoreset=True)
        text = 'Welcome to AnimeWatch360'
        color = Fore.CYAN
        art = pyfiglet.figlet_format(text, width=150)
        colored_art = color + art
        print(colored_art)
        print("1. Browse Anime")
        print("2. View Anime Details")
        print("3. Add Anime")
        print("4. Delete Anime")
        print("5. Add Review")
        print("6. Delete Review")
        print("7. Exit")

    def browse_anime(self):
        print("-------------------------------------")
        # Browse available anime
        self.database.connect()
        query = "SELECT * FROM anime"
        cursor = self.database.connection.cursor()
        cursor.execute(query)
        anime_records = cursor.fetchall()
        self.database.disconnect()

        if len(anime_records) > 0:
            print("Available Anime:")
            for anime_record in anime_records:
                anime = Anime(*anime_record)
                print(f"{anime.anime_id}. {anime.title}")
        else:
            print("No anime available.")

    def view_anime_details(self):
        print("-------------------------------------")
        # View details of a specific anime
        anime_id = int(input("Enter the anime ID: "))

        self.database.connect()
        query = f"SELECT * FROM anime WHERE anime_id = {anime_id}"
        cursor = self.database.connection.cursor()
        cursor.execute(query)
        anime_record = cursor.fetchone()
        self.database.disconnect()

        if anime_record is not None:
            anime = Anime(*anime_record)
            anime.get_anime_details()
        else:
            print("Anime not found.")

    def add_anime(self):
        print("-------------------------------------")
        # Add a new anime to the database
        title = input("Enter the title of the anime: ")
        description = input("Enter the description of the anime: ")
        genre = input("Enter the genre of the anime: ")
        episode_count = int(input("Enter the episode count of the anime: "))
        status = input("Enter the status of the anime: ")

        self.database.connect()
        self.database.add_anime(title, description, genre, episode_count, status)
        self.database.disconnect()

        print("Anime added successfully.")

    def delete_anime(self):
        print("-------------------------------------")
        # Delete an anime from the database
        anime_id = int(input("Enter the anime ID to delete: "))

        self.database.connect()
        self.database.delete_anime(anime_id)
        self.database.disconnect()

        print("Anime deleted successfully.")

    def add_review(self):
        print("-------------------------------------")
        # Add a new review to the database
        anime_id = int(input("Enter the anime ID: "))
        rating = int(input("Enter your rating for the anime (1-5): "))
        comment = input("Enter your review comment: ")

        self.database.connect()
        self.database.add_review(anime_id, rating, comment)
        self.database.disconnect()

        print("Review added successfully.")

    def delete_review(self):
        print("-------------------------------------")
        # Delete a review from the database
        review_id = int(input("Enter the review ID to delete: "))

        self.database.connect()
        self.database.delete_review(review_id)
        self.database.disconnect()

        print("Review deleted successfully.")

    def exit_program(self):
        print("Thank you for using AnimeWatch360. Goodbye!")
        print("-------------------------------------")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.browse_anime()
            elif choice == "2":
                self.view_anime_details()
            elif choice == "3":
                self.add_anime()
            elif choice == "4":
                self.delete_anime()
            elif choice == "5":
                self.add_review()
            elif choice == "6":
                self.delete_review()
            elif choice == "7":
                self.exit_program()
                break
            else:
                print("Invalid choice. Please try again.")


cli = CLI()
cli.run()
