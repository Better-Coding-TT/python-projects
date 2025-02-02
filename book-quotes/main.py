import json
import matplotlib.pyplot as plt

QUOTES_FILE = "quotes.json"

def load_quotes():
    """Load quotes from the file."""
    try:
        with open(QUOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_quotes(quotes):
    """Save quotes to the file."""
    with open(QUOTES_FILE, "w") as file:
        json.dump(quotes, file, indent=4)

def add_quote(quotes):
    """Add a new quote."""
    quote = input("Enter the quote: ")
    book = input("Enter the book title: ")
    author = input("Enter the author: ")
    tags = input("Enter tags (comma-separated, e.g., inspirational, funny): ").strip().split(",")

    quote_entry = {
        "quote": quote,
        "book": book,
        "author": author,
        "tags": [tag.strip() for tag in tags]
    }
    quotes.append(quote_entry)
    print("Quote added successfully!")

def view_quotes(quotes):
    """View all quotes."""
    if not quotes:
        print("No quotes found.")
        return

    print("\n--- All Quotes ---")
    for i, entry in enumerate(quotes, 1):
        print(f"{i}. Quote: {entry['quote']}")
        print(f"   Book: {entry['book']}")
        print(f"   Author: {entry['author']}")
        print(f"   Tags: {', '.join(entry['tags'])}")
        print()

def search_quotes(quotes):
    """Search quotes by book, author, or tag."""
    if not quotes:
        print("No quotes found.")
        return

    search_term = input("Enter a book title, author, or tag to search: ").strip().lower()
    results = []

    for entry in quotes:
        if (search_term in entry["book"].lower() or
            search_term in entry["author"].lower() or
            any(search_term in tag.lower() for tag in entry["tags"])):
            results.append(entry)

    if not results:
        print("No matching quotes found.")
        return

    print("\n--- Search Results ---")
    for i, entry in enumerate(results, 1):
        print(f"{i}. Quote: {entry['quote']}")
        print(f"   Book: {entry['book']}")
        print(f"   Author: {entry['author']}")
        print(f"   Tags: {', '.join(entry['tags'])}")
        print()

def visualize_tags(quotes):
    """Visualize the frequency of tags using a bar chart."""
    if not quotes:
        print("No quotes found.")
        return

    tag_counts = {}
    for entry in quotes:
        for tag in entry["tags"]:
            if tag in tag_counts:
                tag_counts[tag] += 1
            else:
                tag_counts[tag] = 1

    plt.figure(figsize=(10, 5))
    plt.bar(tag_counts.keys(), tag_counts.values(), color='skyblue')
    plt.xlabel("Tags")
    plt.ylabel("Frequency")
    plt.title("Tag Frequency in Quotes")
    plt.xticks(rotation=45)
    plt.show()
    print("Tag frequency chart displayed. Close the chart window to continue.")

def main():
    quotes = load_quotes()

    while True:
        print("\n--- Personal Book Quote Tracker ---")
        print("1. Add a Quote")
        print("2. View All Quotes")
        print("3. Search Quotes")
        print("4. Visualize Tags")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_quote(quotes)
            save_quotes(quotes)
        elif choice == "2":
            view_quotes(quotes)
        elif choice == "3":
            search_quotes(quotes)
        elif choice == "4":
            visualize_tags(quotes)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
