import sqlalchemy as sa
from cli_color_py import red, bright_yellow, green, bold,bright_magenta

from app import Crud

import pyfiglet
from colorama import init, Fore
from app import Crud
from styles import Styles
import click



class CLI:
    def show_menu(self):
        print("-------------------------------------")

        options = ['1. Browse Anime', '2. View Anime Details', '3. Add Anime', '4. Delete Anime', '5. Add User',
                '6. Delete User', '7. Add Review', '8. Delete Review', '9. Update Anime','10. See Total Anime Count',
                '11. Total Watched Anime','12. Genre List','13. Get Top Rated Animes', '14. Average Rating For an Anime', 
                '15. Filter Anime By Genre', '16. Anime Watch Status', '17. Exit']
        Styles.show(options)


    def browse_anime(self):
        print("-------------------------------------")
        # Browse available anime
        Crud.get_all()


    def view_anime_details(self):
        print("-------------------------------------")
        # View details of a specific anime
        Crud.get_anime_details()


    def add_anime(self):
        print("-------------------------------------")
        # Add a new anime to the database
        Crud.add_anime()


    def delete_anime(self):
        print("-------------------------------------")
        # Delete an anime from the database
        Crud.delete_anime()


    def add_user(self):
        Crud.add_user()


    def delete_user(self):
        Crud.delete_user()


    def add_review(self):
        print("-------------------------------------")
        # Add a new review to the database
        Crud.add_review()


    def delete_review(self):
        print("-------------------------------------")
        # Delete a review from the database
        Crud.delete_review()


    def update_anime(self):
        print("-------------------------------------")
        # Update an existing anime in the database
        Crud.update_anime()


    def get_anime_count(self):
        print("-------------------------------------")
        Crud.get_anime_count()


    def get_total_watched(self):
        print("-------------------------------------")
        Crud.get_total_watched_anime_count()

    
    def get_genre_list(self):
        print("-------------------------------------")
        Crud.get_genre_counts()

    
    def get_top_rated_Animes(self):
        Crud.get_top_rated_anime()

    
    def get_average_rating_for_an_anime(self):
        Crud.get_average_rating_for_anime()

    
    def anime_by_genre(self):
        Crud.get_anime_by_genre()

    
    def watch_status(self):
        Crud.get_anime_watched_status_count()


    # def run_all_methods_in_crud(self):
    #     print("-------------------------------------")
    #     # Run all methods in the Crud class
    #     Crud.get_all()
    #     Crud.get_anime_details()
    #     Crud.add_anime()
    #     Crud.delete_anime()
    #     Crud.add_review()
    #     Crud.delete_review()
    #     Crud.update_anime()
    #     Styles.success("All methods in Crud executed successfully.")


    def exit_program(self):
        sentence = "Thank you for using AnimeWatch360. Goodbye!"
        click.echo(click.style('.' * len(sentence), fg='yellow'))
        click.echo(click.style(sentence, fg='magenta', dim=True, underline=True))
        click.echo(click.style('.' * len(sentence), fg='yellow'))
        

    def run(self):
        while True:
            init(autoreset=True)
            color = Fore.CYAN
            text = 'AnimeWatch360!'
            art = pyfiglet.figlet_format(text, width=100)
            art_colored = color + art
            click.echo(click.style(art_colored, blink=True))
            self.show_menu()
            choice = Styles.main_inputs("Enter your choice")

            if choice == "1":
                self.browse_anime()
            elif choice == "2":
                self.view_anime_details()
            elif choice == "3":
                self.add_anime()
            elif choice == "4":
                self.delete_anime()
            elif choice == "5":
                self.add_user()
            elif choice == "6":
                self.delete_user()
            elif choice == "7":
                self.add_review()
            elif choice == "8":
                self.delete_review()
            elif choice == "9":
                self.update_anime()
            elif choice == "10":
                self.get_anime_count()
            elif choice == "11":
                self.get_total_watched()
            elif choice == "12":
                self.get_genre_list()
            elif choice == "13":
                self.get_top_rated_Animes()
            elif choice == "14":
                self.get_average_rating_for_an_anime()
            elif choice == "15":
                self.anime_by_genre()
            elif choice == "16":
                self.watch_status()
            elif choice == "17":
                self.exit_program()
                break
            else:
                Styles.error("Invalid choice. Please try again.")


if __name__ == "__main__":
    init(autoreset=True)
    color = Fore.CYAN
    text = 'Welcome to AnimeWatch360!'
    art = pyfiglet.figlet_format(text, width=150)
    colored_art = color + art
    click.echo(click.style(colored_art))
    cli = CLI()
    cli.run()
