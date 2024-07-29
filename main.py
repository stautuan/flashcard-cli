import os
import time


def main():
    choice = ""
    prompts = ["Add an entry", "View entries", "Study now", "Quit"]

    while choice != "4":
        clear_screen()
        print("What would you like to do?")
        for i in range(0, len(prompts)):
            print(f"{i + 1} - {prompts[i]}")
        choice = input(">>> ")

        if choice == "1":
            add_entry("french.txt")
        elif choice == "2":
            get_entries("french.txt")
        elif choice == "3":
            random_entry()
        elif choice == "4":
            print("Au revoir!")
            break
        else:
            print(
                f"Oops, '{choice}' is an invalid input. Give it another go... :)")
            time.sleep(3)


def clear_screen():
    os.system("clear")


def add_entry(file):
    while True:
        clear_screen()
        print("======= New Entry ========")
        with open(file, "a") as f:
            text = input("Text: ")
            translation = input("Translation: ")
            f.write(f"{text}: {translation}\n")
            print("Added!\n")

        choice = input("Continue? [y/n] ").lower()
        if choice == "n":
            break


def get_entries(file):
    clear_screen()
    f = open(file, "r")
    print(f.read())

    while True:
        choice = input("Press 1 to go back\n>>> ")
        if choice == "1":
            break


def random_entry():
    pass


if __name__ == "__main__":
    main()
