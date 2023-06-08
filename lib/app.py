from models.models import Review, User, Anime, session


class Crud:

    def add_anime():
        # Add a new anime to the database
        title = input("Enter Title: ")
        description = input("Enter desc: ")
        genre = input("Enter genre")
        episode_count = int(input('Enter eps_count: '))
        status = input('Status')
        watched = input('Enter True or False for Watched: ')

        user = User(title=title, description=description, genre=genre,
                    status=status, episode_count=episode_count, watched=watched)
        session.add(user)
        session.commit()

    def add_user(self, username, email, favorite_anime):
        # Add a new user to the database
        username = input('Enter username: ')
        email = input("enter email: ")
        favorite_anime = input("Enter favorite anime: ")

        user = User(username, email, favorite_anime)
        session.add(user)
        session.commit()

    def add_review():
        # Add a new review to the database
        rating = int(input('Enter rating: '))
        comment = str(input('Enter comment'))

        review = Review(rating=rating, comment=comment)
        session.add(review)
        session.commit()

    def delete_review():
        # Delete a review from the database based on its ID
        id = int(input("Enter the review id"))
        session.delete(Review(id=id))

    def delete_anime():
        # Delete an anime from the database based on its ID
        id = int(input("Enter anime id: "))
        session.delete(Anime(id=id))
    def update_anime():
        id = int(input("Enter Anime ID: "))
        anime = session.query(Anime).filter_by(id=id).first()
        
        if anime:
            new_title = input("Enter new Title: ")
            new_description = input("Enter new  Description: ")

            anime.title = new_title
            anime.description = new_description
            session.commit()
            print("Anime updated successfully!")
        else:
            print("Anime not found.")
