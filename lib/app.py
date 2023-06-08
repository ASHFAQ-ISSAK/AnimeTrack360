from models.models import Review, User, Anime, session
from styles import Styles
import click


class Crud:

    @staticmethod
    def add_anime():
        # Add a new anime to the database
        title = Styles.inputs("Enter Title: ")
        description = Styles.inputs("Enter desc: ")
        genre = Styles.inputs("Enter genre: ")
        episode_count = int(Styles.inputs('Enter eps_count: '))
        status = Styles.inputs('Status: ')
        watched = Styles.inputs('Enter True or False for Watched: ').lower() == 'true'

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
        username = Styles.inputs('Enter username: ')
        email = Styles.inputs("Enter email: ")
        favorite_anime_id = int(Styles.inputs("Enter favorite anime ID: "))

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
        rating = int(Styles.inputs('Enter rating: '))
        comment = Styles.inputs('Enter comment: ')
        anime_id = int(Styles.inputs('Enter anime ID: '))
        user_id = int(Styles.inputs('Enter user ID: '))

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
        id = int(Styles.inputs("Enter the review ID: "))
        review = session.query(Review).get(id)

        if review:
            session.delete(review)
            session.commit()
            Styles.success("Review deleted successfully!")
        else:
            Styles.error("Review not found.")


    @staticmethod
    def delete_anime():
        # Delete an anime from the database based on its ID
        id = int(Styles.inputs("Enter anime ID: "))
        anime = session.query(Anime).get(id)

        if anime:
            session.delete(anime)
            session.commit()
            Styles.success("Anime deleted successfully!")
        else:
            Styles.error("Anime not found.")


    @staticmethod
    def update_anime():
        id = int(Styles.inputs("Enter Anime ID: "))
        anime = session.query(Anime).get(id)

        if anime:
            new_title = Styles.inputs("Enter new Title: ")
            new_description = Styles.inputs("Enter new Description: ")

            anime.title = new_title
            anime.description = new_description
            session.commit()
            Styles.success("Anime updated successfully!")
        else:
            Styles.error("Anime not found.")


    @staticmethod
    def get_all():
        animes = session.query(Anime).all()
        if animes:
            i = 1
            click.echo(click.style('Here\'s the list of all animes', fg='blue', dim=True, underline=True))
            for anime in animes:
                Styles.mod_styles(f"{i}. Anime: {anime.title}, Episode Count: {anime.episode_count}")
                i += 1        

        else:
            Styles.error('No animes available')


    @staticmethod
    def get_anime_details():
        id = int(Styles.inputs('Enter Anime ID'))
        anime = session.query(Anime).get(id)

        if anime:
            Styles.mod_styles(f"-> Title: {anime.title}")
            Styles.mod_styles(f"-> Description: {anime.description}")
            Styles.mod_styles(f"-> Genre: {anime.genre}")
            Styles.mod_styles(f"-> Episode Count: {anime.episode_count}")
            Styles.mod_styles(f"-> Status: {anime.status}")
            Styles.mod_styles(f"-> Watched: {anime.watched}")
        else:
            Styles.error("Anime not found.")


