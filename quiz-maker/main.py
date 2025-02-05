import json
import random
import os

FLASHCARDS_FILE = "flashcards.json"

def load_flashcards():
    """Load flashcards from the JSON file."""
    if os.path.exists(FLASHCARDS_FILE):
        with open(FLASHCARDS_FILE, "r") as file:
            return json.load(file)
    return []

def save_flashcards(flashcards):
    """Save flashcards to the JSON file."""
    with open(FLASHCARDS_FILE, "w") as file:
        json.dump(flashcards, file, indent=4)

def add_flashcard(flashcards):
    """Add a new flashcard."""
    question = input("Enter the question: ")
    question_type = input("Is this a multiple-choice question? (yes/no): ").strip().lower()

    if question_type == "yes":
        options = []
        for i in range(4):
            option = input(f"Enter option {i+1}: ")
            options.append(option)
        correct_answer = input("Enter the correct option (1-4): ").strip()
        flashcards.append({
            "type": "multiple_choice",
            "question": question,
            "options": options,
            "answer": correct_answer
        })
    else:
        answer = input("Enter the answer: ").strip()
        flashcards.append({
            "type": "fill_in",
            "question": question,
            "answer": answer
        })
    print("Flashcard added successfully!")

def quiz(flashcards):
    """Quiz the user with randomly selected flashcards."""
    if not flashcards:
        print("No flashcards available. Add some first!")
        return

    random.shuffle(flashcards)
    for card in flashcards:
        print("\nQuestion:", card["question"])
        if card["type"] == "multiple_choice":
            for i, option in enumerate(card["options"]):
                print(f"{i+1}. {option}")
            user_answer = input("Your answer (1-4): ").strip()
            if user_answer == card["answer"]:
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is: {card['answer']}")
        else:
            user_answer = input("Your answer: ").strip().lower()
            if user_answer == card["answer"].lower():
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is: {card['answer']}")
        input("Press Enter to continue...")

def main():
    """Main function to run the flashcard program."""
    flashcards = load_flashcards()

    while True:
        print("\n1. Add a flashcard")
        print("2. Quiz yourself")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_flashcard(flashcards)
            save_flashcards(flashcards)
        elif choice == "2":
            quiz(flashcards)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
