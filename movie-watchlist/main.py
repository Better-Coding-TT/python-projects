import json

WATCHLIST_FILE = "watchlist.json"

def load_watchlist():
    """Load the watchlist from the file."""
    try:
        with open(WATCHLIST_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_watchlist(watchlist):
    """Save the watchlist to the file."""
    with open(WATCHLIST_FILE, "w") as file:
        json.dump(watchlist, file, indent=4)

def add_movie(watchlist):
    """Add a movie to the watchlist."""
    title = input("Enter the movie title: ")
    genre = input("Enter the genre: ")
    year = input("Enter the release year: ")

    movie = {
        "title": title,
        "genre": genre,
        "year": year,
        "watched": False,
        "rating": None,
        "review": None
    }
    watchlist.append(movie)
    print(f"'{title}' added to your watchlist!")

def view_watchlist(watchlist):
    """View all movies in the watchlist."""
    if not watchlist:
        print("Your watchlist is empty.")
        return

    print("\n--- Your Watchlist ---")
    for i, movie in enumerate(watchlist, 1):
        status = "Watched" if movie["watched"] else "Not Watched"
        rating = f", Rating: {movie['rating']}/5" if movie["rating"] else ""
        review = f"\n   Review: {movie['review']}" if movie["review"] else ""
        print(f"{i}. {movie['title']} ({movie['year']}) - {movie['genre']} - {status}{rating}{review}")

def mark_as_watched(watchlist):
    """Mark a movie as watched and optionally rate and review it."""
    view_watchlist(watchlist)
    if not watchlist:
        return

    try:
        choice = int(input("Enter the number of the movie to mark as watched: ")) - 1
        if 0 <= choice < len(watchlist):
            movie = watchlist[choice]
            if movie["watched"]:
                print(f"'{movie['title']}' is already marked as watched.")
            else:
                movie["watched"] = True
                rating = input("Rate the movie (1-5, or leave blank): ")
                if rating.isdigit() and 1 <= int(rating) <= 5:
                    movie["rating"] = int(rating)
                review = input("Write a review (or leave blank): ")
                if review:
                    movie["review"] = review
                print(f"'{movie['title']}' marked as watched!")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    watchlist = load_watchlist()

    while True:
        print("\n--- Personal Movie Watchlist and Recommender ---")
        print("1. Add a Movie")
        print("2. View Watchlist")
        print("3. Mark as Watched and Review")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_movie(watchlist)
            save_watchlist(watchlist)
        elif choice == "2":
            view_watchlist(watchlist)
        elif choice == "3":
            mark_as_watched(watchlist)
            save_watchlist(watchlist)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
