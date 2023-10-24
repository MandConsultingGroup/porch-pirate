import sys, json
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

WHITE = '\033[37m'
BLUE = '\033[34m'
BLACK = "\u001b[30m"
RED = "\u001b[31m"
YELLOW = "\u001b[33m"
MAGENTA = "\u001b[35m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37m"
GREEN = "\u001b[32m"
BOLD = '\033[1m'
END = '\033[0m'

def main():
    p = porchpirate()
    request = json.loads(p.request('2052387-24db9f10-04ba-4354-a1f6-7a84046110a3'))['data']
    request_id = request['id']
    request_name = request['name']
    request_url = request['url']
    request_query_params = request['queryParams']
    request_method = request['method']
    print(request['name'])
    print(f"{BOLD}{YELLOW}[*]{END} Fetching request ID {CYAN}{request_id}{END}")
    print(f"{BOLD}________________________________________________________________________________{END}")
    print(f"{BOLD}> {BLUE}Name: {END}{CYAN}{request_name}{END}")
    print(f"{BOLD}> {BLUE}Request Method: {END}{CYAN}{request_method}{END}{END}")
    print(f"{BOLD}> {BLUE}Request URL: {END}{CYAN}{request_url}{END}{END}")
    print(f"{BOLD}________________________________________________________________________________{END}\n\n")

if __name__ == "__main__":
    main()