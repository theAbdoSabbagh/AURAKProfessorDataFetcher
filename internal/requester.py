from requests import get

class Requester:
    def __init__(self):
        self.base_url = "https://aurak.ac.ae/academics/meet-the-faculty?"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        }
    
    def get(self, url):
        """Send a GET request to the specified URL and return the response.

        Args:
        ---------
            url (str):
                The URL to send the GET request to.

        Returns:
        ---------
            The response object.
        """
        
        return get(
            f"{self.base_url}{url}",
            headers = self.headers
        )
