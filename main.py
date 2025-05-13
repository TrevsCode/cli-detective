from case import Case
from investigations import Investigations

def main():
    logbook = Investigations()
    while True:

        print(" --- Welcome to the CLI file management system! ---")
        print("Press 1 to review all open cases")
        print("Press 2 to add a new case")
        print("Press 3 to add a note to an existing case")
        print("Press 4 to search for specific cases")
        print("Press 5 to close an active case")
        print("Press q to quit your active CLI session")

        choice = input("Enter your selection: ")

        if choice == '1':
            logbook.list_cases()
        elif choice == '2':
            title = input("Enter the title: ")
            suspect = input("Enter your suspect: ")
            notes = input("Enter your notes: ")
            new_case = Case(title, suspect, notes)
            logbook.add_case(new_case)
        elif choice == '3':
            findtitle = input("Enter the title you're searching for: ")
            case_to_update = logbook.get_case_by_title(findtitle)
            note = input("Provide your new note: ")
            case_to_update.add_note(note)
        elif choice == '4':
            casesuspect = input("Which suspect are you looking at cases for?: ")
            results = logbook.search_cases(casesuspect)
            if results:
                for case in results:
                    print(case)
            else:
                print(f"No cases found by the name of {casesuspect}")
        elif choice == '5':
            closecase = input("Which case would you like to close, please enter the title: ")
            try:
                case_to_close = logbook.get_case_by_title(closecase)
                logbook.close_case(closecase)
                print(f"Case with title {closecase} has been closed!")
            except Exception:
                print(f"Unable to find cases by the name of: {closecase}")
        elif choice == 'q':
            break
        else:
            print("Please make a valid selection!")

        

if __name__ == "__main__":
    main()
