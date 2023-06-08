from models.models import Review, User, Anime, session
import click

def error(text):
    click.echo(click.style(text, fg='red', bold=True))

def success(text):
    click.echo(click.style(text, fg='green', bold=True))

def styles(text, color='blue'):
    click.echo(click.style(text, fg=color, dim=True))

class Crud:

    @staticmethod
    def add_anime():
        # Add a new anime to the database
        title = input("Enter Title: ")
        description = input("Enter desc: ")
        genre = input("Enter genre: ")
        episode_count = int(input('Enter eps_count: '))
        status = input('Status: ')
        watched = input('Enter True or False for Watched: ').lower() == 'true'

        anime = Anime(
            title=title,
            description=description,
            genre=genre,
            status=status,
            episode_count=episode_count,
            watched=watched
        )
        session.add(anime)
        session.commit()

    @staticmethod
    def add_user():
        # Add a new user to the database
        username = input('Enter username: ')
        email = input("Enter email: ")
        favorite_anime_id = int(input("Enter favorite anime ID: "))

        user = User(
            username=username,
            email=email,
            favorite_anime_id=favorite_anime_id
        )
        session.add(user)
        session.commit()

    @staticmethod
    def add_review():
        # Add a new review to the database
        rating = int(input('Enter rating: '))
        comment = input('Enter comment: ')
        anime_id = int(input('Enter anime ID: '))
        user_id = int(input('Enter user ID: '))

        review = Review(
            rating=rating,
            comment=comment,
            anime_id=anime_id,
            user_id=user_id
        )
        session.add(review)
        session.commit()

    @staticmethod
    def delete_review():
        # Delete a review from the database based on its ID
        id = int(input("Enter the review ID: "))
        review = session.query(Review).get(id)

        if review:
            session.delete(review)
            session.commit()
            success("Review deleted successfully!")
        else:
            error("Review not found.")

    @staticmethod
    def delete_anime():
        # Delete an anime from the database based on its ID
        id = int(input("Enter anime ID: "))
        anime = session.query(Anime).get(id)

        if anime:
            session.delete(anime)
            session.commit()
            success("Anime deleted successfully!")
        else:
            error("Anime not found.")

    @staticmethod
    def update_anime():
        id = int(input("Enter Anime ID: "))
        anime = session.query(Anime).get(id)

        if anime:
            new_title = input("Enter new Title: ")
            new_description = input("Enter new Description: ")

            anime.title = new_title
            anime.description = new_description
            session.commit()
            success("Anime updated successfully!")
        else:
            error("Anime not found.")

    @staticmethod
    def get_all():
        animes = session.query(Anime).all()
        if animes:
            i = 1
            click.echo(click.style('Here\'s the list of all animes', fg='green', dim=True, underline=True))
            for anime in animes:
                styles(f"{i}. Anime: {anime.title}, Episode Count: {anime.episode_count}")
                i += 1
        else:
            error('No animes available')

    @staticmethod
    def get_anime_details():
        # choice = click.prompt(click.style("Enter your choice ", fg='green', bold=True))
        id = int(click.prompt(click.style("Enter Anime ID: ", fg='yellow', bold=True)))
        anime = session.query(Anime).get(id)

        if anime:
            styles(f"=> Title: {anime.title}")
            styles(f"=> Description: {anime.description}")
            styles(f"=> Genre: {anime.genre}")
            styles(f"=> Episode Count: {anime.episode_count}")
            styles(f"=> Status: {anime.status}")
            styles(f"=> Watched: {anime.watched}")
        else:
            error("Anime not found.")


