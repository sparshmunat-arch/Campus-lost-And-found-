from database import create_database, update_database
import sqlite3
from matcher import calculate_similarity
from users import create_users_table, register_user

create_database()
update_database()
create_users_table()

while True:

    print("===================================")
    print("      CAMPUS LOST AND FOUND")
    print("===================================")
    print("1. Register User")
    print("2. Report Lost Item")
    print("3. Report Found Item")
    print("4. Search Items")
    print("5. Find Possible Matches")
    print("6. Claim Found Item")
    print("7. Reports")
    print("8. Exit")

    choice = input("Enter your choice: ")

    print("You selected:", choice)
    if choice == "1":
        register_user()

    elif choice == "2":
        print("\n--- Report Lost Item ---")

        item_name = input("Enter item name: ").strip()
        while item_name == "":
            print("Item name cannot be empty.")
            item_name = input("Enter item name: ").strip()
        description = input("Describe the item: ").strip()
        while description == "":
            print("Description cannot be empty.")
            description = input("Describe the item: ").strip()
        location = input("Where did you lose it? ").strip()
        while location == "":
            print("Location cannot be empty.")
            location = input("Where did you lose it? ").strip()
        date = input("When did you lose it? ").strip()
        while date == "":
            print("Date cannot be empty.")
            date = input("When did you lose it? ").strip()
        connection = sqlite3.connect("lost_found.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO lost_items (item_name, description, location, date)
            VALUES (?, ?, ?, ?)
        """, (item_name, description, location, date))

        connection.commit()
        connection.close()

        print("\nLost item recorded successfully!")
        print("Item:", item_name)
        print("Description:", description)
        print("Location:", location)
        print("Date:", date)
        
    elif choice == "3":
        print("\n--- Report Found Item ---")

        item_name = input("Enter item name: ").strip()
        while item_name == "":
            print("Item name cannot be empty.")
            item_name = input("Enter item name: ").strip()
        description = input("Describe the item: ").strip()
        while description == "":
            print("Description cannot be empty.")
            description = input("Describe the item: ").strip()
        location = input("Where did you find it? ").strip()
        while location == "":
            print("Location cannot be empty.")
            location = input("Where did you find it? ").strip()
        date = input("When did you find it? ").strip()
        while date == "":
            print("Date cannot be empty.")
            date = input("When did you find it? ").strip()
        connection = sqlite3.connect("lost_found.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO found_items (item_name, description, location, date)
            VALUES (?, ?, ?, ?)
        """, (item_name, description, location, date))

        connection.commit()
        connection.close()

        print("\nFound item recorded successfully!")
        print("Item:", item_name)
        print("Description:", description)
        print("Location:", location)
        print("Date:", date)
    elif choice == "4":
        print("\n--- Search Items ---")

        search = input("Enter item name to search: ")

        connection = sqlite3.connect("lost_found.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, item_name, description, location, date
            FROM lost_items
            WHERE item_name LIKE ? OR description LIKE ? OR location LIKE ?
        """, ("%" + search + "%", "%" + search + "%", "%" + search + "%"))

        lost_items = cursor.fetchall()

        cursor.execute("""
            SELECT id, item_name, description, location, date
            FROM found_items
            WHERE item_name LIKE ? OR description LIKE ? OR location LIKE ?
        """, ("%" + search + "%", "%" + search + "%", "%" + search + "%"))

        found_items = cursor.fetchall()

        connection.close()

        print("\n--- Lost Items ---")

        if lost_items:
            for item in lost_items:
                print("ID:", item[0])
                print("Item:", item[1])
                print("Description:", item[2])
                print("Location:", item[3])
                print("Date:", item[4])
                print("--------------------")
        else:
            print("No matching lost items found.")

        print("\n--- Found Items ---")

        if found_items:
            for item in found_items:
                print("ID:", item[0])
                print("Item:", item[1])
                print("Description:", item[2])
                print("Location:", item[3])
                print("Date:", item[4])
                print("--------------------")
        else:
            print("No matching found items.")    
    elif choice == "5":
        print("\n--- Find Possible Matches ---")

        lost_id = input("Enter the ID of the lost item: ")

        connection = sqlite3.connect("lost_found.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, item_name, description, location, date
            FROM lost_items
            WHERE id = ?
        """, (lost_id,))

        lost_item = cursor.fetchone()

        if lost_item is None:
            print("Lost item not found.")
        else:
            cursor.execute("""
                SELECT id, item_name, description, location, date, status
                FROM found_items
            """)

            found_items = cursor.fetchall()

            if not found_items:
                print("No found items available for matching.")
            else:
                matches = []

                for found_item in found_items:
                    score = calculate_similarity(lost_item, found_item)

                    if score >= 30:
                        matches.append((score, found_item))

                matches.sort(reverse=True, key=lambda x: x[0])

                if matches:
                    print("\nPossible Matches:")

                    for score, item in matches:
                        if score >= 80:
                            match_level = "Very Strong Match"
                        elif score >= 60:
                            match_level = "Strong Match"
                        elif score >= 40:
                            match_level = "Possible Match"
                        else:
                            match_level = "Weak Match"

                        print("\nMatch Score:", score, "%")
                        print("Match Level:", match_level)
                        print("Item:", item[1])
                        print("Description:", item[2])
                        print("Location:", item[3])
                        print("Date:", item[4])
                        print("Status:", item[5])
                        print("--------------------")
                else:
                    print("No strong matches found.")

        connection.close()
    elif choice == "6":
        print("\n--- Claim Found Item ---")

        item_id = input("Enter the ID of the found item: ")

        connection = sqlite3.connect("lost_found.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, item_name, description, location, date, status
            FROM found_items
            WHERE id = ?
        """, (item_id,))

        item = cursor.fetchone()

        if item is None:
            print("Found item not found.")

        elif item[5] == "CLAIMED":
            print("This item has already been claimed.")

        else:
            cursor.execute("""
                UPDATE found_items
                SET status = 'CLAIMED'
                WHERE id = ?
            """, (item_id,))

            connection.commit()

            print("\nItem claimed successfully!")
            print("Item:", item[1])
            print("Status: CLAIMED")

        connection.close()
    elif choice == "7":
        print("\n--- Reports & Statistics ---")

        connection = sqlite3.connect("lost_found.db")
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM lost_items")
        total_lost = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM found_items")
        total_found = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM found_items
            WHERE status = 'CLAIMED'
        """)
        total_claimed = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM found_items
            WHERE status = 'FOUND'
        """)
        total_unclaimed = cursor.fetchone()[0]

        connection.close()

        print("\n===== CAMPUS LOST & FOUND REPORT =====")
        print("Total Lost Items:", total_lost)
        print("Total Found Items:", total_found)
        print("Items Claimed:", total_claimed)
        print("Items Still Unclaimed:", total_unclaimed)    
    elif choice == "8":
        print("Thank you for using Campus Lost and Found!")
        break

    else:
        print("Invalid choice. Please try again.")