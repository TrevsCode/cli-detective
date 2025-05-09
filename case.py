class Case:
    def __init__(self, title, suspect, notes=None):
        self.status = "open"
        self.notes = []
        self.title = title
        self.suspect = suspect

    def add_note(self, text):
            if text == None:
                 raise Exception("text must contain a string")
            elif text == "":
                raise Exception("No empty strings - please enter a message")
            elif len(text) > 200:
                raise Exception("String too long - please shorten to 200 or less characters")
            else:
                self.notes.append(text)
    

if __name__ == "__main__":
    my_case = Case("Thomas unpluged the pcs", "Thomas")
    my_case.add_note("Observed thomas sneaking behind pc's on security footage.")
    print(f"Title: {my_case.title}")
    print(f"Suspect: {my_case.suspect}")
    print(f"Notes: {my_case.notes}")
    print(f"Status: {my_case.status}")

