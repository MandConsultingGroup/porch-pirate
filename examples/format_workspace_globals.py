import sys
import json
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def format_results(global_results):
    for result in global_results['data']['values']:
        key = result['key']
        value = result['value']
        print({ "key": key, "value": value })
        
def main():
    with open("dummy_input/workspace_globals.json", "r") as f:
        globals_results = json.load(f)
        format_results(globals_results)

if __name__ == "__main__":
    main()