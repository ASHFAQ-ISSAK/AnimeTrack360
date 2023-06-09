#! /usr/bin/env/ python3 

from database import Database
from anime import Anime
from review import Review
from colorama import Fore, init



class CLI:
    def __init__(self):
        self.database = Database("anime_project.db")

    def show_menu(self):
        print("-------------------------------------")
        print(f"{Fore.WHITE}Welcome to AnimeWatch360!")
        print(f"{Fore.GREEN}1. Browse Anime")
        print(f"{Fore.GREEN}2. View Anime Details")
        print(f"{Fore.GREEN}3. Add Anime")
        print(f"{Fore.GREEN}4. Delete Anime")
        print(f"{Fore.GREEN}5. Add Review")
        print(f"{Fore.GREEN}6. Delete Review")
        print(f"{Fore.GREEN}7. Exit")


    def browse_anime(self):
        print("-------------------------------------")
        self.database.connect()
        query = "SELECT * FROM anime"
        cursor = self.database.connection.cursor()
        cursor.execute(query)
        anime_records = cursor.fetchall()
        self.database.disconnect()

        if len(anime_records) > 0:
            print(f"{Fore.YELLOW}Available Anime:")
            for anime_record in anime_records:
                anime = Anime(*anime_record)
                print(f"{anime.anime_id}. {anime.title}")
        else:
            print(f"{Fore.YELLOW}No anime available.")

    def view_anime_details(self):
        print("-------------------------------------")
        anime_id = int(input(f"{Fore.CYAN}Enter the anime ID: "))

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
            print(f"{Fore.RED}Anime not found.")

    def add_anime(self):
        print("-------------------------------------")
        title = input(f"{Fore.MAGENTA}Enter the title of the anime: ")
        description = input(f"{Fore.MAGENTA}Enter the description of the anime: ")
        genre = input(f"{Fore.MAGENTA}Enter the genre of the anime: ")
        episode_count = int(
            input(f"{Fore.MAGENTA}Enter the episode count of the anime: ")
        )
        status = input(f"{Fore.MAGENTA}Enter the status of the anime: ")

        self.database.connect()
        self.database.add_anime(title, description, genre, episode_count, status)
        self.database.disconnect()

        print(f"{Fore.GREEN}Anime added successfully.")

    def delete_anime(self):
        print("-------------------------------------")
        anime_id = int(input(f"{Fore.RED}Enter the anime ID to delete: "))

        self.database.connect()
        self.database.delete_anime(anime_id)
        self.database.disconnect()

        print(f"{Fore.YELLOW}Anime deleted successfully.")

    def add_review(self):
        print("-------------------------------------")
        anime_id = int(input(f"{Fore.CYAN}Enter the anime ID: "))
        rating = int(input(f"{Fore.CYAN}Enter your rating for the anime (1-5): "))
        comment = input(f"{Fore.CYAN}Enter your review comment: ")

        self.database.connect()
        self.database.add_review(anime_id, rating, comment)
        self.database.disconnect()

        print(f"{Fore.GREEN}Review added successfully.")

    def delete_review(self):
        print("-------------------------------------")
        review_id = int(input(f"{Fore.RED}Enter the review ID to delete: "))

        self.database.connect()
        self.database.delete_review(review_id)
        self.database.disconnect()

        print(f"{Fore.YELLOW}Review deleted successfully.")

    def exit_program(self):
        print(f"{Fore.WHITE}Thank you for using AnimeWatch360. Goodbye!")
        print("-------------------------------------")

    def run(self):
        while True:
            self.show_menu()
            choice = input(f"{Fore.WHITE}Enter your choice: ")

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
                print(f"{Fore.RED}Invalid choice. Please try again.")


init()
cli = CLI()
cli.run()
