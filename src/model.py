import os
import requests
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

class PlagiaGuard:
    def __init__(self, code):
        self.code = code

    def logic(self):
        GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") 
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
            return {}
        

    def show_results(self):
        results = self.output()
        if results:
            links = {}
            for item in results['items'][:10]:
                links[item['name']] = item['html_url']
            return links
        else:
            return {}
    
    def table_output(self):
        links = self.show_results()
        if links:
            data = {
                "Name" : list(links.keys()),
                "URL" : list(links.values())
            }
            df = pd.DataFrame(data = data)
            indexes = [i for i in range(1, 11)]
            df.index = indexes

            df['URL'] = df['URL'].apply(lambda url: f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>')

            html_table = df.to_html(escape = False, index = False)
            return html_table
        else:
            return {}






