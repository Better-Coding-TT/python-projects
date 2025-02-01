import json
import datetime
import matplotlib.pyplot as plt

mood_file = "mood_logs.json"

def load_mood_logs():
    """Load mood logs from the file."""
    try:
        with open(mood_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_mood_logs(mood_logs):
    """Save mood logs to the file."""
    with open(mood_file, "w") as file:
        json.dump(mood_logs, file, indent=4)

def log_mood(mood_logs):
    """Log the user's mood."""
    mood = input("How are you feeling? (e.g., happy, sad, energetic, calm): ").strip().lower()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mood_logs.append({"timestamp": now, "mood": mood})
    print("Mood logged successfully!")

def view_mood_trends(mood_logs):
    """Visualize mood trends over time."""
    if not mood_logs:
        print("No mood logs found.")
        return

    mood_count = {}
    for log in mood_logs:
        mood = log["mood"]
        if mood in mood_count:
            mood_count[mood] += 1
        else:
            mood_count[mood] = 1

    plt.figure(figsize=(10, 5))
    plt.bar(mood_count.keys(), mood_count.values(), color='skyblue')
    plt.xlabel("Moods")
    plt.ylabel("Frequency")
    plt.title("Mood Trends Over Time")
    plt.show()
    print("Mood trends displayed. Close the chart window to continue.")

def weekly_summary(mood_logs):
    """Generate a weekly summary of moods."""
    if not mood_logs:
        print("No mood logs found.")
        return

    now = datetime.datetime.now()
    week_ago = now - datetime.timedelta(days=7)
    recent_logs = [log for log in mood_logs if datetime.datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S") >= week_ago]

    if not recent_logs:
        print("No mood logs in the last 7 days.")
        return

    mood_count = {}
    for log in recent_logs:
        mood = log["mood"]
        if mood in mood_count:
            mood_count[mood] += 1
        else:
            mood_count[mood] = 1

    print("\n--- Weekly Summary ---")
    for mood, count in mood_count.items():
        print(f"{mood.capitalize()}: {count} times")

def main():
    mood_logs = load_mood_logs()

    while True:
        print("\n--- Mood Tracker ---")
        print("1. Log Your Mood")
        print("2. View Mood Trends")
        print("3. Weekly Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            log_mood(mood_logs)
            save_mood_logs(mood_logs)
        elif choice == "2":
            view_mood_trends(mood_logs)
        elif choice == "3":
            weekly_summary(mood_logs)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
