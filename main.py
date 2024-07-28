def main():
    task = ""
    while task != "2":
        task = input(
            "What would you like to do?\n1 - Add an entry\n2 - Quit\n")
        if task == '1':
            add_entry()
        elif task == "2":
            print("Quitting...")
            break
        else:
            print("Invalid input!\n")


def add_entry():
    list_dict = {}
    while True:
        print("======= New Entry ========")
        sentence = input("Sentence: ")
        definition = input("Definition: ")
        list_dict[sentence] = definition
        print("Added!\n")

        answer = input("Continue? [y/n] ").lower()
        if answer == "n":
            print("==========================")
            break


main()
