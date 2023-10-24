import sys, json
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def main():
    p = porchpirate()
    results = json.loads(p.search('bell.ca'))
    ids = []
    for result in results['data']:
        try:
            workspace = result['document']['workspaces']
        except:
            test = "test"
        for w in workspace:
            ids.append(w['id'])

    for id in ids:
        print(p.workspace_globals(id))
    
if __name__ == "__main__":
    main()