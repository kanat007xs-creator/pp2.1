import csv
from connect import get_connection

# CREATE - добавить контакт
def insert_contact(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

# CREATE - добавить контакт
def create_new_table(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"""CREATE TABLE {name} (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    phone VARCHAR(20) NOT NULL
                )""")
    conn.commit()
    print("Table was created successfully!")
    cur.close()
    conn.close()

#CSV
def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row['name'], row['phone'])
            )

    conn.commit()
    cur.close()
    conn.close()

#бәрін корсету
def get_all_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

#фильтром
def search_by_name(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

def search_by_phone_prefix(prefix):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"{prefix}%",))
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

#UPDATE
def update_contact(old_name, new_name=None, new_phone=None):
    conn = get_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute("UPDATE phonebook SET name=%s WHERE name=%s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, old_name))

    conn.commit()
    cur.close()
    conn.close()

#DELETE
def delete_contact_by_name(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    conn.commit()

    cur.close()
    conn.close()

def delete_contact_by_phone(phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
    conn.commit()

    cur.close()
    conn.close()

#Console
def menu():
    while True:
        print("\n1. Add contact")
        print("2. Import from CSV")
        print("3. Show all contacts")
        print("4. Search by name")
        print("5. Search by phone prefix")
        print("6. Update contact")
        print("7. Delete by name")
        print("8. Delete by phone")
        print("9. Create new table")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            insert_from_csv("contacts.csv")

        elif choice == "3":
            get_all_contacts()

        elif choice == "4":
            name = input("Enter name: ")
            search_by_name(name)

        elif choice == "5":
            prefix = input("Enter prefix: ")
            search_by_phone_prefix(prefix)

        elif choice == "6":
            old = input("Old name: ")
            new_name = input("New name (leave empty): ")
            new_phone = input("New phone (leave empty): ")

            update_contact(
                old,
                new_name if new_name else None,
                new_phone if new_phone else None
            )

        elif choice == "7":
            name = input("Name to delete: ")
            delete_contact_by_name(name)

        elif choice == "8":
            phone = input("Phone to delete: ")
            delete_contact_by_phone(phone)

        elif choice == "9":
            name = input("Give the name of table: ")
            create_new_table(name)

        elif choice == "0":
            break

menu()