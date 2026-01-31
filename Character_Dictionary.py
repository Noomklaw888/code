import json
import os

FILE = "chardict.json"


def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


def read_all():
    data = load_data()
    if not data:
        print("No characters found.")
        return

    for name, desc in data.items():
        print(f"{name}: {desc}")

def search_character(name):
    data = load_data()
    name_lower = name.lower()
    
    for key, desc in data.items():
        if key.lower() == name_lower:
            print(f"{key}: {desc}")
            return
    
    print("Character not found.")


while True:
    choice = input("Read or Exit? (r / e): ").lower()

    if choice == "r":
        allornothing = input("All or Search?(a,s)")
        if allornothing == "a":
            read_all()
        elif allornothing == "s":
            name = input("Character name to search: ")
            search_character(name)
        else:
            print("Invalid choice!")
    elif choice == "e":
        break

    else:
        print("Invalid choice!")

