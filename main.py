import random
import os
import time


def main():
    choice = ""
    prompts = ["Add an entry", "View entries", "Study now", "Quit"]

    while choice != "4":
        clear_screen()
        print("What would you like to do?")
        for i in range(len(prompts)):
            print(f"{i + 1} - {prompts[i]}")
        choice = input(">>> ")

        if choice == "1":
            add_entry("french.txt")
        elif choice == "2":
            get_entries("french.txt")
        elif choice == "3":
            get_entry("french.txt")
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

# TODO: Fix the function below (it's a mess!)


def get_entry(file):
    f = open(file, "r")
    items_list = f.read().split('\n')
    new_list = items_list[:-1]

    while len(new_list) > 0:
        clear_screen()
        item = random.choice(new_list)
        item_list = item.split(": ")
        print(item_list[0])
        answer = input("Translate: ").lower()

        if answer == item_list[1]:
            print("Correct!")
            time.sleep(2)
        else:
            print(f'The correct answer is "{item_list[1]}"\n')
            print("Press N to go Next")
            print("Press H to go Home")
            choice = input().lower()
            if choice == "h":
                break

        new_list.remove(item)


if __name__ == "__main__":
    main()
