
from faker import Faker
import random
from models.models import Review, User, Anime, session

# Create an instance of the Faker class
fake = Faker()

# Generate seed data using Faker
animes = []
users = []
reviews = []

# Generate 10 anime records
for _ in range(10):
    anime = Anime(
        title=fake.name(),
        description=fake.text(),
        genre=random.choice(['Action', 'Adventure', 'Comedy', 'Drama']),
        episode_count=random.randint(12, 24),
        status=random.choice(['Ongoing', 'Finished']),
        watched=fake.boolean()
    )
    animes.append(anime)

# Generate 5 user records
for _ in range(5):
    user = User(
        username=fake.user_name(),
        email=fake.email(),
        favorite_anime=random.choice(animes)
    )
    users.append(user)

# Generate 10 review records
for _ in range(10):
    review = Review(
        rating=random.randint(1, 5),
        comment=fake.text(),
        anime=random.choice(animes),
        user=random.choice(users)
    )
    reviews.append(review)

# Add the instances to the session
session.add_all(animes + users + reviews)

# Commit the changes to the database
session.commit()
=======
from models.models import Review,User,Anime,session, Base, engine

from faker import Faker
import random 

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session.query(Review).delete()
    session.query(User).delete()
    session.query(Anime).delete()
    # session.query(anime_users).delete()

    faker = Faker()
    faker.seed(1)

    GENRES = [
    "Action","Adventure","Comedy","Drama","Fantasy","Romance","Slice of Life","Supernatural","Mystery","Thriller",
    "Sci-Fi","Horror","Mecha","Sports","Historical","Psychological","School","Music","Shounen","Shoujo"]

    STATUS = ["Ongoing","Completed","On Hold","Dropped","Upcoming","Hiatus"]
    animes = []
    for _ in range(80):
        anime  = Anime(
            title = faker.word(),
            description = faker.text(),
            genre = random.choice(GENRES),
            episode_count = random.randint(1, 200),
            watched = random.randint(0,1),
            status = random.choice(STATUS),
        )

        session.add(anime)
        session.commit()
        animes.append(anime)

    users = []
    for i in range(50):
        user = User(
            username = faker.name(),
            email = faker.email(),
            favorite_anime_id = random.choice(animes).id,
        )
        session.add(user)
        session.commit()
        users.append(user)

    reviews = []
    for user in users:
        for i in range(random.randint(1,5)):
            anime = random.choice(animes)
            if user not in anime.users:
                anime.users.append(user)
                session.commit()
            
            review = Review(
                rating = random.randint(1,10),
                comment = faker.text(),
                anime_id = anime.id,
                user_id = user.id
            )

            reviews.append(review)

    session.bulk_save_objects(reviews)
    session.commit()
    session.close()
