class Case:
    def __init__(self, title, suspect, notes=None):
        self.status = "open"
        self.title = title
        self.suspect = suspect
        self.notes = [notes] if notes else []


    def add_note(self, text):
            if text == None:
                 raise Exception("text must contain a string")
            elif text == "":
                raise Exception("No empty strings - please enter a message")
            elif len(text) > 200:
                raise Exception("String too long - please shorten to 200 or less characters")
            else:
                self.notes.append(text)
    
    def __str__(self):
         
         return f"Case title: {self.title}, Case suspect: {self.suspect}, Case notes: {self.notes}"

