import random
import os
import time

FILE_NAME = "french.txt"
PROMPTS = ["Add an entry", "View entries", "Study now", "Quit"]


def main():
    choice = ""

    while choice != "4":
        clear_screen()
        display_menu(PROMPTS)
        choice = input(">>> ")

        if choice == "1":
            add_entry(FILE_NAME)
        elif choice == "2":
            display_entries(FILE_NAME)
        elif choice == "3":
            study_entries(FILE_NAME)
        elif choice == "4":
            print("Au revoir!")
            break
        else:
            print(
                f"Oops, '{choice}' is an invalid input. Give it another go... :)")
            time.sleep(3)


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def display_menu(prompts):
    print("What would you like to do?")
    for i in range(len(prompts)):
        print(f"{i + 1} - {prompts[i]}")


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


def display_entries(file):
    clear_screen()
    with open(file, "r") as f:
        print(f.read())

    while True:
        choice = input("Press 1 to go back\n>>> ")
        if choice == "1":
            break

# TODO: Fix the function below (it's a mess!)


def study_entries(file):
    with open(file, "r") as f:
        items_list = f.read().split('\n')

    new_list = items_list[:-1]
    while len(new_list) > 0:
        clear_screen()
        item = random.choice(new_list)
        text, translation = item.split(": ")
        print(text)
        answer = input("Translate: ").lower()

        if answer == translation:
            print("Correct!")
            time.sleep(2)
        else:
            print(f'The correct answer is "{translation}"\n')
            print("Press N to go Next")
            print("Press H to go Home")
            choice = input().lower()
            if choice == "h":
                break

        new_list.remove(item)

    if not new_list:
        clear_screen()
        print("You have reached the end.")
        time.sleep(2)


if __name__ == "__main__":
    main()
