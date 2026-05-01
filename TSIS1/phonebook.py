import json
from connect import get_connection

# ---------- ADD CONTACT ----------
def add_contact():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")

    cur.execute(
        "INSERT INTO phonebook(name,email,birthday) VALUES (%s,%s,%s)",
        (name, email, birthday)
    )

    conn.commit()
    cur.close()
    conn.close()

# ---------- ADD PHONE ----------
def add_phone():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))
    conn.commit()

    cur.close()
    conn.close()

# ---------- MOVE GROUP ----------
def move_group():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    group = input("Group: ")

    cur.execute("CALL move_to_group(%s,%s)", (name, group))
    conn.commit()

    cur.close()
    conn.close()

# ---------- SEARCH ----------
def search():
    conn = get_connection()
    cur = conn.cursor()

    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

# ---------- FILTER ----------
def filter_group():
    conn = get_connection()
    cur = conn.cursor()

    group = input("Group: ")

    cur.execute("""
        SELECT c.name, c.email
        FROM phonebook c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

# ---------- SORT ----------
def sort_contacts():
    conn = get_connection()
    cur = conn.cursor()

    field = input("Sort by (name/birthday): ")
    cur.execute(f"SELECT name,email,birthday FROM phonebook ORDER BY {field}")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

# ---------- PAGINATION ----------
def pagination():
    conn = get_connection()
    cur = conn.cursor()

    limit = 3
    offset = 0

    while True:
        cur.execute("SELECT * FROM get_contacts_paginated(%s,%s)", (limit, offset))

        for row in cur.fetchall():
            print(row)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        else:
            break

    cur.close()
    conn.close()

# ---------- EXPORT JSON ----------
def export_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name,c.email,c.birthday,g.name,p.phone,p.type
        FROM phonebook c
        LEFT JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones p ON c.id=p.contact_id
    """)

    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f, default=str, indent=4)

    print("Exported!")

    cur.close()
    conn.close()

# ---------- IMPORT JSON ----------
def import_json():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for row in data:
        name,email,birthday,group,phone,ptype = row

        cur.execute("SELECT 1 FROM phonebook WHERE name=%s",(name,))
        if cur.fetchone():
            choice = input(f"{name} exists (skip/overwrite): ")
            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM phonebook WHERE name=%s",(name,))

        cur.execute(
            "INSERT INTO phonebook(name,email,birthday) VALUES (%s,%s,%s)",
            (name,email,birthday)
        )

    conn.commit()
    cur.close()
    conn.close()

# ---------- MENU ----------
def menu():
    while True:
        print("\n1 Add contact")
        print("2 Add phone")
        print("3 Move to group")
        print("4 Search")
        print("5 Filter by group")
        print("6 Sort")
        print("7 Pagination")
        print("8 Export JSON")
        print("9 Import JSON")
        print("0 Exit")

        ch = input("Choice: ")

        if ch == "1": add_contact()
        elif ch == "2": add_phone()
        elif ch == "3": move_group()
        elif ch == "4": search()
        elif ch == "5": filter_group()
        elif ch == "6": sort_contacts()
        elif ch == "7": pagination()
        elif ch == "8": export_json()
        elif ch == "9": import_json()
        elif ch == "0": break

if __name__ == "__main__":
    menu()