import os

class Guest:
    def __init__(self, name, group, preferences):
        self.name = name
        self.group = group
        self.preferences = preferences

    def __str__(self):
        return f"{self.name} ({self.group}) - {self.preferences}"


class Table:
    def __init__(self, number):
        self.number = number
        self.guests = []

    def add_guest(self, guest):
        self.guests.append(guest)

    def __str__(self):
        guest_names = ", ".join(guest.name for guest in self.guests)
        return f"Table {self.number}: {guest_names}"


class SeatingManager:
    MAX_GUESTS_PER_TABLE = 8

    def __init__(self):
        self.guest_list = []
        self.tables = []

    def add_guest(self):
        name = input("Enter guest name: ").strip()
        group = input("Enter group (e.g., family/friends): ").strip()
        preferences = input("Enter preferences (e.g., 'Near John, Away from Alice'): ").strip()
        self.guest_list.append(Guest(name, group, preferences))
        print("Guest added successfully!")

    def assign_seats(self):
        self.tables.clear()
        table_number = 1

        grouped_guests = {}
        for guest in self.guest_list:
            grouped_guests.setdefault(guest.group, []).append(guest)

        for group, guests in grouped_guests.items():
            for guest in guests:
                excluded_guests = self._get_excluded_guests(guest)
                near_guests = self._get_near_guests(guest)

                table = next(
                    (
                        t
                        for t in self.tables
                        if len(t.guests) < self.MAX_GUESTS_PER_TABLE
                        and not any(g.name in excluded_guests for g in t.guests)  
                        and (not near_guests or any(g.name in near_guests for g in t.guests))  
                    ),
                    None,
                )

                if not table:
                    table = Table(table_number)
                    self.tables.append(table)
                    table_number += 1

                table.add_guest(guest)

        print("Seating arrangement completed!")

    def _get_near_guests(self, guest):
        """Parses the 'near' preferences from a guest's preferences string."""
        near_guests = []
        if "near" in guest.preferences.lower():
            preferences = guest.preferences.lower()
            start_index = preferences.find("near") + len("near")
            names = preferences[start_index:].split(",")
            near_guests = [name.strip().title() for name in names]
        return near_guests

    def _get_excluded_guests(self, guest):
        """Parses the 'away from' preferences from a guest's preferences string."""
        excluded_guests = []
        if "away from" in guest.preferences.lower():
            preferences = guest.preferences.lower()
            start_index = preferences.find("away from") + len("away from")
            names = preferences[start_index:].split(",")
            excluded_guests = [name.strip().title() for name in names]
        return excluded_guests

    def view_seating_arrangement(self):
        if not self.tables:
            print("No seating arrangement found. Please assign seats first.")
            return

        print("\n=== Seating Arrangement ===")
        for table in self.tables:
            print(table)

    def save_seating_plan(self):
        with open("seating_plan.txt", "w") as file:
            for table in self.tables:
                file.write(str(table) + "\n")
        print("Seating plan saved to 'seating_plan.txt'.")

    def load_seating_plan(self):
        if not os.path.exists("seating_plan.txt"):
            print("No saved seating plan found.")
            return

        self.tables.clear()
        with open("seating_plan.txt", "r") as file:
            for line in file:
                parts = line.split(":")
                if len(parts) == 2:
                    table_number = int(parts[0].replace("Table ", "").strip())
                    guest_names = parts[1].strip().split(", ")
                    table = Table(table_number)
                    for name in guest_names:
                        guest = next((g for g in self.guest_list if g.name == name), None)
                        if guest:
                            table.add_guest(guest)
                    self.tables.append(table)

        print("Seating plan loaded successfully!")


def main():
    manager = SeatingManager()

    while True:
        print("\n=== Event Seating Arranger ===")
        print("1. Add Guest")
        print("2. Assign Seats")
        print("3. View Seating Arrangement")
        print("4. Save Seating Plan")
        print("5. Load Seating Plan")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            manager.add_guest()
        elif choice == "2":
            manager.assign_seats()
        elif choice == "3":
            manager.view_seating_arrangement()
        elif choice == "4":
            manager.save_seating_plan()
        elif choice == "5":
            manager.load_seating_plan()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
