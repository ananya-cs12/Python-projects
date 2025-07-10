import random

def load_movies():
    try:
        with open("movies.txt", "r", encoding="utf-8") as F1:
            movies = {}
            for i in F1:
                genre, title = i.strip().split(" - ")
                if genre not in movies:
                    movies[genre] = []
                movies[genre].append(title)
            return movies
    except FileNotFoundError:
        return {}

def save_movie(genre, title):
    with open("movies.txt", "a", encoding="utf-8") as F1:
        F1.write(f"{genre} - {title}\n")

def recommend_movie(movies):
    if not movies:
        print("No movies found. Add some first.")
        return
    print("\nAvailable genres:", ", ".join(movies.keys()))
    genre = input("Choose a genre: ").strip().lower()
    if genre in movies:
        print(f"Recommended: {random.choice(movies[genre])}")
    else:
        print("Genre not found. Try again.")

def add_movie(movies):
    genre = input("Enter genre: ").strip().lower()
    title = input("Enter movie title: ").strip()
    if genre and title:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(title)
        save_movie(genre, title)
        print(f"'{title}' added under '{genre}'.")

def view_movies(movies):
    if not movies:
        print("No movies found.")
        return
    print("\nAll Movies:")
    for genre, titles in movies.items():
        print(f"\n{genre.capitalize()}:")
        for title in titles:
            print(f" - {title}")

def movie_recommender():
    print("************Welcome to the Movie Recommender!*************")
    movies = load_movies()

    while True:
        print("\n1. Recommend a movie")
        print("2. Add a movie")
        print("3. View all movies")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            recommend_movie(movies)
        elif choice == '2':
            add_movie(movies)
        elif choice == '3':
            view_movies(movies)
        elif choice == '4':
            print("Thanks for using the Movie Recommender!")
            break
        else:
            print("Invalid choice. Try again.")

movie_recommender()
