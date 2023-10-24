import sys
import json
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def format_results(search_results):
    for result in search_results['data']:
        name = result['document']['name']
        author = result['document']['publisherName']
        try:
            description = result['document']['description']
        except:
            description = "No description available."
        try:
            lastupdated = result['document']['updatedAt']
        except:
            lastupdated = "No data available"
        print(f"Item name: {name}")
        print(f"Author: {author}")
        print(f"Last updated: {lastupdated}")
        print(f"Description: {description}\n")

def main():
    with open("dummy_input/telus_search_results.json", "r") as f:
        search_results = json.load(f)
        format_results(search_results)

if __name__ == "__main__":
    main()