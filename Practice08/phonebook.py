from connect import get_connection


import csv
from connect import get_connection

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



def load_csv():
    insert_from_csv("contacts.csv")


def search():
    conn = get_connection()
    cur = conn.cursor()

    pattern = input("Pattern: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def upsert():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()

    cur.close()
    conn.close()


def insert_many():
    names = input("Names (comma): ").split(",")
    phones = input("Phones (comma): ").split(",")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_many_contacts(%s, %s)", (names, phones))
    conn.commit()

    cur.close()
    conn.close()


def pagination():
    conn = get_connection()
    cur = conn.cursor()

    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def delete():
    conn = get_connection()
    cur = conn.cursor()

    value = input("Name or phone: ")
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()

    cur.close()
    conn.close()


def menu():
    while True:
        print("\n1 Load CSV")
        print("2 Search")
        print("3 Upsert")
        print("4 Insert many")
        print("5 Pagination")
        print("6 Delete")
        print("0 Exit")

        choice = input()

        if choice == "1":
            load_csv()
        elif choice == "2":
            search()
        elif choice == "3":
            upsert()
        elif choice == "4":
            insert_many()
        elif choice == "5":
            pagination()
        elif choice == "6":
            delete()
        elif choice == "0":
            break


if __name__ == "__main__":
    menu()