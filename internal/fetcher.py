from rich import print
from concurrent.futures import ThreadPoolExecutor, as_completed
from internal.logger import Logger
from internal.requester import Requester
from internal.parser import Parser

class Fetcher:
    def __init__(self):
        self.requester = Requester()
        self.logger = Logger()
        self.professors = []
        self.seen_professors = set()  # To track unique professors

    def fetch_professor_data(self, name, url):
        parser = Parser()  # Create a new Parser instance for each thread
        response = self.requester.get(url)
        if response.status_code != 200:
            self.logger.error(f"Failed to fetch {name} data. Status code: {response.status_code}")
            return None
        
        self.logger.success(f"Fetched {name} data successfully!")
        parser.set_content(response.text)
        return parser.get_professors(name)

    def run(self):
        subpages = {
            "Department of Management": "department_1=1&search_1=#aurak-school-of-business-0_item",
            "Department of Accounting and Finance": "department_1=11&search_1=#aurak-school-of-business-0_item",
            "Department of Biotechnology": "department_2=8&search_2=#aurak-school-of-arts-sciences-1_item",
            "Department of Humanities and Social Sciences (1)": "department_2=9&search_2=#aurak-school-of-arts-sciences-1_item",
            "Department of Humanities and Social Sciences (2)": "page=2&department_2=9&search_2=#aurak-school-of-arts-sciences-1_item",
            "Department of Humanities and Social Sciences (3)": "page=3&department_2=9&search_2=#aurak-school-of-arts-sciences-1_item",
            "Department of Mathematics and Physics": "department_2=10&search_2=#aurak-school-of-arts-sciences-1_item",
            "Department of Civil and Infrastructure Engineering": "department_6=2&search_6=#aurak-school-of-engineering-and-computing-2_item",
            "Department of Chemical and Petroleum Engineering": "department_6=3&search_6=#aurak-school-of-engineering-and-computing-2_item",
            "Department of Computer Science and Engineering": "department_6=5&search_6=#aurak-school-of-engineering-and-computing-2_item",
            "Department of Electrical and Electronics Engineering": "department_6=6&search_6=#aurak-school-of-engineering-and-computing-2_item",
            "Department of Mechanical Engineering": "department_6=7&search_6=#aurak-school-of-engineering-and-computing-2_item",
            "Department of Architecture": "department_6=13&search_6=#aurak-school-of-engineering-and-computing-2_item",
        }

        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_name = {
                executor.submit(
                    self.fetch_professor_data, name, url, 
                ): name for name, url in subpages.items()
            }
            for future in as_completed(future_to_name):
                try:
                    result = future.result()
                    if result:
                        for professor in result:
                            if (professor.name, professor.role) not in self.seen_professors:
                                self.professors.append(professor)
                                self.seen_professors.add((professor.name, professor.role))
                except Exception as exc:
                    self.logger.error(f"An error occurred: {exc}")

    def save_professors(self):
        with open("professors.txt", "w", encoding="utf-8") as file:
            for professor in self.professors:
                file.write(str(professor) + "\n\n")
    
    def display_professors(self):
        for professor in self.professors:
            self.logger.info(professor)
            print(f"\n\n{'=' * 15}\n")
