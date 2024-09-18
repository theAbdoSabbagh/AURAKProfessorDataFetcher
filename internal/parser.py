from bs4 import BeautifulSoup
from internal.objects import Professor

class Parser:
    def __init__(self):
        self.soup = None
    
    def set_content(self, content: str):
        """Set the content of the parser.

        Args:
        ---------
            content (str):
                The content to parse.
        """

        self.soup = BeautifulSoup(content, 'html.parser')
    
    def get_professors(self, department: str):
        """Extract the professors from the page.

        Args:
        ---------
            department (str):
                The department name.

        Returns:
        ---------
            list[Professor]:
                A list of Professor objects.
            
        Raises:
        ---------
            AssertionError:
                If the content is not set before calling this method.
        """

        if not self.soup:
            raise AssertionError("Content not get the professors data. Please set the content first.")

        professors = []
        for item in self.soup.find_all('div', class_='p-4 p-md-5 ps-3 ps-md-4 m-0 h-100'):
            name = item.find('h4', class_='readmore-title').get_text(strip=True)
            role = item.find('p', class_='lead readmore-subtitle').get_text(strip=True)
            room_number = item.find_all('p')[1].get_text(strip=True)  # The room number is the second <p> element
            phone_number = item.find_all('p')[2].get_text(strip=True)  # The phone number is the third <p> element

            professors.append(
                Professor(
                    name,
                    role,
                    room_number if len(room_number) > 0 else None,
                    phone_number if "read more" not in phone_number.lower() else None,
                    department = department
                )
            )

        return professors
