#! /usr/bin/env/ python3 

import pyfiglet
from colorama import init, Fore
from app import Crud
import click

def show(text_array):
        for text in text_array:
            click.echo(click.style(text, fg='bright_magenta', bold=True ))

def error(text):
    click.echo(click.style(text, fg='red', bold=True))

def success(text):
    click.echo(click.style(text, fg='green', bold=True))


class CLI:

    def show_menu(self):
        print("-------------------------------------")
        init(autoreset=True)
        color = Fore.CYAN
        text = 'Welcome to AnimeWatch360'
        art = pyfiglet.figlet_format(text, width=150)
        colored_art = color + art
        click.echo(click.style(colored_art))
        options = ['1. Browse Anime', '2. View Anime Details', '3. Add Anime', '4. Delete Anime',
                '5. Add Review', '6. Delete Review', '7. Update Anime', '8. Exit']
        show(options)
        # print("1. Browse Anime")
        # print("2. View Anime Details")
        # print("3. Add Anime")
        # print("4. Delete Anime")
        # print("5. Add Review")
        # print("6. Delete Review")
        # print("7. Update Anime")
        # print("8. Exit")

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
        success("Anime added successfully.")

    def delete_anime(self):
        print("-------------------------------------")
        # Delete an anime from the database
        Crud.delete_anime()
        # print("Anime deleted successfully.")

    def add_review(self):
        print("-------------------------------------")
        # Add a new review to the database
        Crud.add_review()
        success("Review added successfully.")

    def delete_review(self):
        print("-------------------------------------")
        # Delete a review from the database
        Crud.delete_review()
        # print("Review deleted successfully.")

    def update_anime(self):
        print("-------------------------------------")
        # Update an existing anime in the database
        Crud.update_anime()

    def exit_program(self):
        sentence = "Thank you for using AnimeWatch360. Goodbye!"
        click.echo(click.style('.' * len(sentence), fg='yellow'))
        click.echo(click.style(sentence, fg='magenta', dim=True, underline=True))
        click.echo(click.style('.' * len(sentence), fg='yellow'))

    def run(self):
        while True:
            self.show_menu()
            choice = click.prompt(click.style("Enter your choice ", fg='yellow', bold=True))

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
                self.exit_program()
                break
            else:
                error("Invalid choice. Please try again.")


if __name__ == "__main__":
    cli = CLI()
    cli.run()

