import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class PlagiaGuard:
    def __init__(self, code):
        self.code = code

    def logic(self):
        GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Get the token from environment variable
        if not GITHUB_TOKEN:
            raise ValueError("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        
        query = self.code

        url = f"https://api.github.com/search/code?q={query}+in:file+language:python"

        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }

        return requests.get(url, headers=headers)

    def output(self):
        response = self.logic()
        if response.status_code == 200:
            return response.json()
        else:
            return False
        

    def show_results(self):
        results = self.output()
        if results:
            links = {}
            for item in results['items'][:10]:
                links[item['name']] = item['html_url']
            return links
        else:
            return f"GitHub API error: {self.logic().status_code}"
    



