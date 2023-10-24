import sys, json
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def main():
    p = porchpirate()
    collections = json.loads(p.collections('4127fdda-08be-4f34-af0e-a8bdc06efaba'))
    for collection in collections['data']: 
        requests = collection['requests']
        #print(requests)
        for r in requests:
            request_data = p.request(r['id'])
            print(request_data)
            

if __name__ == "__main__":
    main()