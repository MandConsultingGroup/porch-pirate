import sys, json
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def main():
    p = porchpirate()
    request = json.loads(p.request('30128925-bc9d4872-7005-4d81-b2d5-15dddb08e5cc'))['data']
    curl = p.build_curl_request(request)
    print(curl)

if __name__ == "__main__":
    main()