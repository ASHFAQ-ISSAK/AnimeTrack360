import logging
import os
import sqlalchemy as sa
from cli_color_py import red, bright_yellow, green, bold,bright_magenta

from app import Crud

# Set the logging level to suppress SQLAlchemy logs
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

# Disable SQLAlchemy logging
logging.getLogger(sa.__name__).setLevel(logging.ERROR)


class CLI:
    def show_menu(self):
        print("-------------------------------------")
        print(bold(bright_magenta("Welcome to AnimeWatch360!")))
        print("1. Browse Anime")
        print("2. View Anime Details")
        print("3. Add Anime")
        print("4. Delete Anime")
        print("5. Add Review")
        print("6. Delete Review")
        print("7. Update Anime")
        print("8. Run All Methods in Crud")
        print("9. Exit")

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
        print(Color.GREEN + "Anime added successfully." + Color.END)

    def delete_anime(self):
        print("-------------------------------------")
        # Delete an anime from the database
        Crud.delete_anime()
        print(Color.GREEN + "Anime deleted successfully." + Color.END)

    def add_review(self):
        print("-------------------------------------")
        # Add a new review to the database
        Crud.add_review()
        print(green( "Review added successfully."))

    def delete_review(self):
        print("-------------------------------------")
        # Delete a review from the database
        Crud.delete_review()
        print(Color.GREEN + "Review deleted successfully." + Color.END)

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
                self.update_anime()
            elif choice == "8":
                self.run_all_methods_in_crud()
            elif choice == "9":
                self.exit_program()
                break
            else:
                print(Color.RED + "Invalid choice. Please try again." + Color.END)


if __name__ == "__main__":
    cli = CLI()
    cli.run()
