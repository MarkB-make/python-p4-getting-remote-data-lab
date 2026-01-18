import requests
import json

class GetRequester:
    def __init__(self, url):
        """Initialize the GetRequester with a URL string."""
        self.url = url
    
    def get_response_body(self):
        """Send a GET request to the URL and return the response body."""
        response = requests.get(self.url)
        return response.content
    
    def load_json(self):
        """Send a request and return the JSON data as a Python list or dictionary."""
        response_body = self.get_response_body()
        return json.loads(response_body)