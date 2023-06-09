import logging
import os
import sqlalchemy as sa

from sqlalchemy import func
from models.models import Review, User, Anime, session
from styles import Styles
import click


# Set the logging level to suppress SQLAlchemy logs
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

# Disable SQLAlchemy logging
logging.getLogger(sa.__name__).setLevel(logging.ERROR)
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
        print("Anime added successfully!")


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
        print("User added successfully!")


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
        print("Review added successfully!")


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

    @staticmethod
    def get_anime_count():
        # Get the total count of anime in the database
        count = session.query(func.count(Anime.id)).scalar()
        print(f"Total Anime Count: {count}")

    @staticmethod
    def get_average_episode_count():
        # Get the average episode count of all anime
        average_count = session.query(func.avg(Anime.episode_count)).scalar()
        print(f"Average Episode Count: {average_count}")

    @staticmethod
    def get_max_episode_count():
        # Get the maximum episode count among all anime
        max_count = session.query(func.max(Anime.episode_count)).scalar()
        print(f"Maximum Episode Count: {max_count}")

    @staticmethod
    def get_min_episode_count():
        # Get the minimum episode count among all anime
        min_count = session.query(func.min(Anime.episode_count)).scalar()
        print(f"Minimum Episode Count: {min_count}")

    @staticmethod
    def get_total_watched_anime_count():
        # Get the total count of watched anime
        count = session.query(func.count(Anime.id)).filter(
            Anime.watched == True).scalar()
        print(f"Total Watched Anime Count: {count}")

    @staticmethod
    def get_genre_counts():
        # Get the count of anime in each genre
        genre_counts = session.query(Anime.genre, func.count(
            Anime.id)).group_by(Anime.genre).all()
        for genre, count in genre_counts:
            print(f"Genre: {genre}, Count: {count}")

    @staticmethod
    def get_top_rated_anime():
        # Get the top-rated anime based on average review ratings
        top_rated = (
            session.query(Anime.title, func.avg(Review.rating))
            .join(Review)
            .group_by(Anime.id)
            .order_by(func.avg(Review.rating).desc())
            .limit(5)
            .all()
        )
        for title, rating in top_rated:
            print(f"Anime: {title}, Average Rating: {rating:.2f}")

    @staticmethod
    def get_anime_with_most_reviews():
        # Get the anime with the most number of reviews
        most_reviews = (
            session.query(Anime.title, func.count(Review.id))
            .join(Review)
            .group_by(Anime.id)
            .order_by(func.count(Review.id).desc())
            .first()
        )
        if most_reviews:
            title, review_count = most_reviews
            print(f"Anime: {title}, Review Count: {review_count}")
        else:
            print("No anime found.")

    @staticmethod
    def get_users_with_multiple_reviews():
        # Get the users who have written multiple reviews
        users = (
            session.query(User.username, func.count(Review.id))
            .join(Review)
            .group_by(User.id)
            .having(func.count(Review.id) > 1)
            .all()
        )
        for username, review_count in users:
            print(f"User: {username}, Review Count: {review_count}")

    @staticmethod
    def get_anime_with_most_episodes():
        # Get the anime with the highest number of episodes
        anime = session.query(Anime).order_by(
            Anime.episode_count.desc()).first()
        if anime:
            print(
                f"Anime with Most Episodes: {anime.title}, Episode Count: {anime.episode_count}")
        else:
            print("No anime found.")

    @staticmethod
    def get_average_rating_for_anime(anime_id):
        # Get the average rating for a specific anime
        average_rating = session.query(func.avg(Review.rating)).filter(
            Review.anime_id == anime_id).scalar()
        print(f"Average Rating for Anime ID {anime_id}: {average_rating:.2f}")

    @staticmethod
    def get_user_favorite_anime_count(user_id):
        # Get the count of favorite anime for a specific user
        favorite_anime_count = session.query(func.count(
            User.favorite_anime_id)).filter(User.id == user_id).scalar()
        print(
            f"Favorite Anime Count for User ID {user_id}: {favorite_anime_count}")

    @staticmethod
    def get_anime_by_genre(genre):
        # Get all anime of a specific genre
        anime_list = session.query(Anime).filter(Anime.genre == genre).all()
        for anime in anime_list:
            print(f"Anime: {anime.title}, Genre: {anime.genre}")

    @staticmethod
    def get_anime_watched_status_count():
        # Get the count of anime based on their watched status
        status_counts = (
            session.query(Anime.status, func.count(Anime.id))
            .group_by(Anime.status)
            .all()
        )
        for status, count in status_counts:
            print(f"Status: {status}, Count: {count}")
