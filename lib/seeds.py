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

