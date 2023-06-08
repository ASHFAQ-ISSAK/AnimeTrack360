from models.models import Review, User, Anime, session


def add_anime():
    username = str(input("Enter username  :"))
    email = str(input("Enter    email    : "))
    favorite_anime = str(input("Enter  favorite anime  : "))
    session.add(User(username, email, favorite_anime))

def get_all_anime():
    animes = session.query(Anime).all()
    for anime in animes:
        print(f"Anime ID: {Anime.id}, Name: {Anime.title}, Email: {Anime.description}")
def delete_anime():
    anime_name=int('Enter the name of the anime you want to delete')


def get_anime_status():
    pass


def get_current_watch_anime():
    pass
