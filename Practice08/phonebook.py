import psycopg2
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def search(pattern):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def upsert(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_many(names, phones):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL insert_many_contacts(%s, %s)", (names, phones))
    conn.commit()
    cur.close()
    conn.close()

def get_paginated(limit, offset):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete(value):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    cur.close()
    conn.close()

def menu():
    while True:
        print("1 Search")
        print("2 Upsert")
        print("3 Insert many")
        print("4 Pagination")
        print("5 Delete")
        print("0 Exit")
        choice = input()
        if choice == "1":
            search(input())
        elif choice == "2":
            upsert(input(), input())
        elif choice == "3":
            names = input().split(",")
            phones = input().split(",")
            insert_many(names, phones)
        elif choice == "4":
            get_paginated(int(input()), int(input()))
        elif choice == "5":
            delete(input())
        elif choice == "0":
            break

if __name__ == "__main__":
    menu()