class Investigations:
    def __init__(self, cases):
        self.cases = []

    def add_case(self, case):
        self.cases.append(case)
        
    def list_cases(self):
        open_cases = []
        for case in self.cases:
            if case.status == "open":
                open_cases.append(case)
        return open_cases