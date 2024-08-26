import json
import os


def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            return json.load(f)
    return {}


def add_note(title, content):
    notes = load_notes()
    notes[title] = content
    with open("notes.json", "w") as f:
        json.dump(notes, f)


def list_notes():
    notes = load_notes()
    for title in notes:
        print(f"\nTitle: {title}\nContent: {notes[title]}\n")



def delete_note(title):
    notes = load_notes()
    if title in notes:
        del notes[title]
        with open("notes.json", "w") as f:
            json.dump(notes, f)
        print(f"Note with title '{title}' was deleted.")
    else:
        print(f"Note with title '{title}' does not exist.")


def main():
    while True:
        action = input("Choose an action: add, delete, list or exit: ")
        if action == "add":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            add_note(title, content)
        elif action == "list":
            list_notes()
        elif action == "delete":
            title = input("Enter the title of the note you want to be deleted: ")
            delete_note(title)
        elif action == "exit":
            break


if __name__ == "__main__":
    main()
