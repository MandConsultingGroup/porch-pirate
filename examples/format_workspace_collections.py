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
        collection = json.loads(p.collection(collection))
        collection_name = collection['data']['name']
        collection_id = collection['data']['id']
        collection_created_at = collection['data']['createdAt']
        collection_updated_at = collection['data']['updatedAt']
        print(collection_name, collection_id, collection_created_at, collection_updated_at)

if __name__ == "__main__":
    main()