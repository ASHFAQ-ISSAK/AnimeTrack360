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
