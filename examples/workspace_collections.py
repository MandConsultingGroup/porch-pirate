import sys, json
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def main():
    collections = []
    p = porchpirate()
    workspace = json.loads(p.workspace('4127fdda-08be-4f34-af0e-a8bdc06efaba'))['data']
    for collection in workspace['dependencies']['collections']:
        collections.append(collection)
    for collection in collections:
        print(p.collection(collection))

if __name__ == "__main__":
    main()