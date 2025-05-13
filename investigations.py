class Investigations:
    def __init__(self):
        self.cases = []

    def add_case(self, case):
        self.cases.append(case)
        
    def list_cases(self):
        open_cases = []
        for case in self.cases:
            if case.status == "open":
                open_cases.append(case)
        if open_cases:
            for case in open_cases:
                print(case)
        else:
            print("No cases found")
    
    
    def search_cases(self, name):
        filtered_cases = []
        for case in self.cases:
            if case.suspect == name:
                filtered_cases.append(case)
        return filtered_cases

    def close_case(self, title):
        for case in self.cases:
            if case.title == title:
             case.status = "Closed"

    def get_case_by_title(self, title):
        for case in self.cases:
            if case.title == title:
                return case
        else:
            raise Exception("Case title not found")