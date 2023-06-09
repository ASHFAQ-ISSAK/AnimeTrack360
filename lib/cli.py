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

        options = ['1. Browse Anime', '2. View Anime Details', '3. Add Anime', '4. Delete Anime',
                '5. Add Review', '6. Delete Review', '7. Update Anime', '8. Exit']
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

        Styles.success("Anime added successfully.")


    def delete_anime(self):
        print("-------------------------------------")
        # Delete an anime from the database
        Crud.delete_anime()


    def add_review(self):
        print("-------------------------------------")
        # Add a new review to the database
        Crud.add_review()

        Styles.success("Review added successfully.")


    def delete_review(self):
        print("-------------------------------------")
        # Delete a review from the database
        Crud.delete_review()



    def update_anime(self):
        print("-------------------------------------")
        # Update an existing anime in the database
        Crud.update_anime()

    def run_all_methods_in_crud(self):
        print("-------------------------------------")
        # Run all methods in the Crud class
        Crud.get_all()
        Crud.get_anime_details()
        Crud.add_anime()
        Crud.delete_anime()
        Crud.add_review()
        Crud.delete_review()
        Crud.update_anime()
        print(Color.GREEN + "All methods in Crud executed successfully." + Color.END)


    def exit_program(self):
        sentence = "Thank you for using AnimeWatch360. Goodbye!"
        click.echo(click.style('.' * len(sentence), fg='yellow'))
        click.echo(click.style(sentence, fg='magenta', dim=True, underline=True))
        click.echo(click.style('.' * len(sentence), fg='yellow'))
        

    def run(self):
        while True:
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
                self.add_review()
            elif choice == "6":
                self.delete_review()
            elif choice == "7":
                self.update_anime()
            elif choice == "8":
                self.run_all_methods_in_crud()
            elif choice == "9":
                self.exit_program()
                break
            else:
                Styles.error("Invalid choice. Please try again.")


if __name__ == "__main__":
    init(autoreset=True)
    color = Fore.CYAN
    text = 'Welcome to AnimeWatch360'
    art = pyfiglet.figlet_format(text, width=150)
    colored_art = color + art
    click.echo(click.style(colored_art))
    cli = CLI()
    cli.run()
