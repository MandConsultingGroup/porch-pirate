import requests
import warnings
from urllib3.exceptions import InsecureRequestWarning

# cooked up by
# Dominik Penner (@zer0pwn)
# &&& Jake Bolam (@xixasec)

WHITE   = '\033[37m'
BLUE    = '\033[34m'
BLACK   = "\u001b[30m"
RED     = "\u001b[31m"
YELLOW  = "\u001b[33m"
MAGENTA = "\u001b[35m"
CYAN    = "\u001b[36m"
WHITE   = "\u001b[37m"
GREEN   = "\u001b[32m"
BOLD    = '\033[1m'
END     = '\033[0m'

class porchpirate():
    warnings.simplefilter('ignore', InsecureRequestWarning)
    def __init__(self, proxy=None):
        self.WS_API_URL = 'https://www.postman.com/_api/ws/proxy'
        self.WORKSPACE_API_URL = 'https://www.postman.com/_api/workspace'
        self.INDICE_KEYWORDS = {
            "workspace": "collaboration.workspace",
            "collection": "runtime.collection",
            "request": "runtime.request",
            "api": "adp.api",
            "flow": "flow.flow",
            "team": "apinetwork.team"
        }
        if proxy is not None:
            self.proxies = {
                'http': 'http://' + proxy,
                'https': 'http://' + proxy
            }
        else:
            self.proxies = None

    def _show_formatted_search_results(self, search_results):
        for result in search_results['data']:
            try:
                entity_type = result['document']['entityType']
            except:
                entity_type = 'Unknown'
            try:
                entity_id = result['document']['id']
            except:
                entity_id = False
            try:
                workspace_id = result['document']['workspaces'][0]['id']
            except:
                workspace_id = False
            try:
                name = result['document']['name']
            except:
                name = False
            try:
                author = result['document']['publisherHandle']
            except:
                author = False
            try:
                authorId = result['document']['publisherId']
            except:
                authorId = False
            try:
                description = result['document']['description']
            except:
                description = False
            try:
                lastupdated = result['document']['updatedAt']
            except:
                lastupdated = "No data available"
            print(f"[{CYAN}{entity_type}{END}] [{YELLOW}{entity_id}{END}]")
            if author:
                print(f" {BOLD}Author: {END}{CYAN}{author} [{authorId}]{END}")
            if workspace_id:
                print(f" {BOLD}Workspace: {END}{YELLOW}{workspace_id}{END}")
            if name:
                print(f" {BOLD}Name: {END}{GREEN}{name}{END}")
            if description:
                print(f" {BOLD}Description: {END}{WHITE}{description}{END}")
            print()
    
    def _show_formatted_workspace(self, workspace_results):
        user = workspace_results['data']['profileInfo']['publicName']
        userid = workspace_results['data']['profileInfo']['profileId']
        name = workspace_results['data']['name']
        slug = workspace_results['data']['profileInfo']['slug']
        url = f"https://www.postman.com/{user}/workspace/{slug}"
        collection_count = len(workspace_results['data']['dependencies']['collections'])
        globals = workspace_results['globals']
        print(f"{BOLD}- Name: {END}{CYAN}{name}{END}")
        print(f"{BOLD}- User: {END}{CYAN}{user}{END}")
        print(f"{BOLD}- User ID: {END}{YELLOW}{userid}{END}\n")
        for environment in globals:
            try:
                print(f"{BOLD}- Environment: {END}{YELLOW}{environment['data']['name']}{END}")
            except:
                print(f"{BOLD}- Environment: {END}{YELLOW}Globals{END}")
            for e in environment['data']['values']:
                print(f"{BOLD} - {END}{YELLOW}{e['key']}{END}={GREEN}{e['value']}{END}")
            print()
        print(f"{BOLD}- Collections ({collection_count}): {END}")
        for collection in workspace_results['data']['dependencies']['collections']:
            collectionurl = f"https://www.postman.com/{user}/workspace/{slug}/collection/{collection}"
            print(f"{BOLD} - {END}{YELLOW}{collection}{END}")

    def _show_formatted_globals_findings(self, globals_results):
        try:
            data = globals_results['finding']['data']['values']
        except:
            data = "None"
        if data:
            print(f"\n{BOLD}- Author: {END}{CYAN}{globals_results['name']}{END}")
            try:
                for d in globals_results['finding']['data']['values']:
                    print(f"{BOLD}- Key: {END}{YELLOW}{d['key']}{END}")
                    print(f"{BOLD}- Value: {END}{GREEN}{d['value']}{END}")
                print("\n")
            except:
                pass

    def _show_formatted_collection(self, collection):
        collection_owner = collection['data']['owner']
        collection_name = collection['data']['name']
        collection_id = collection['data']['id']
        collection_created_at = collection['data']['createdAt']
        collection_updated_at = collection['data']['updatedAt']
        collection_request_count = len(collection['data']['order'])
        print(f"\n{BOLD}Collection ID {YELLOW}{collection_id}{END}")
        print(f"{BOLD} - Title: {END}{CYAN}{collection_name}{END}")
        print(f"{BOLD} - Owner ID: {END}{YELLOW}{collection_owner}{END}")
        print(f"{BOLD} - Created at: {END}{CYAN}{collection_created_at}{END}{END}")
        print(f"{BOLD} - Last updated: {END}{CYAN}{collection_updated_at}{END}{END}")

    def _show_formatted_collections(self, workspace_collections):
        for collection in workspace_collections['data']:
            collection_id = collection['id']
            collection_name = collection['name']
            collection_requests = collection['requests']
            collection_request_count = len(collection['requests'])
            print(f"\n{BOLD}Collection ID{END} {YELLOW}{collection_id}{END}")
            print(f"{BOLD}- Name: {END}{CYAN}{collection_name}{END}{END}")
            print(f"{BOLD}- Requests: {END}{END}")
            for request in collection_requests:
                print(f"{BOLD} {END} - {YELLOW}{request['name']}{END}")

    def _show_formatted_request(self, request, requestid):
        request_id = requestid
        request_name = request['name']
        request_url = request['url']
        request_data = request['data']
        request_query_params = request['queryParams']
        request_method = request['method']
        request_headers = request['headerData']
        
        print(f"{BOLD}\nRequest ID {END}{YELLOW}{request_id}{END}")
        print(f"{BOLD}- Name: {END}{CYAN}{request_name}{END}")
        print(f"{BOLD}- URL: {END}{YELLOW}{request_url}{YELLOW}{END}")
        try:
            if "auth" in request:
                print(f"{BOLD}- Authorization: {END}{YELLOW}{request['auth']['type']}{YELLOW}{END}")
                if request['auth']['type'] == 'basic':
                    for element in request['auth']['basic']:
                        print(f"  {BOLD}- {END}{YELLOW}{element['key']}{END}={GREEN}{element['value']}{END}")
                elif request['auth']['type'] == 'oauth2':
                    for element in request['auth']['oauth2']:
                        print(f"  {BOLD}- {END}{YELLOW}{element['key']}{END}: {GREEN}{element['value']}{END}")
        except:
            pass
        print(f"{BOLD}- Request Method: {END}{YELLOW}{request_method}{END}")
        for param in request_query_params:
            request_value = param['value']
            request_url = request_url.replace(request_value, '{}{}{}{}'.format(GREEN, request_value, END, YELLOW))

        for header in request_headers:
            header_value = header['value']
            header_key = header['key']
            if header_value != '':
                print(f"{BOLD}- Header: {END}{YELLOW}{header_key}{END}: {GREEN}{header_value}{END}{END}")
        # this is for requests with POST data or "Body" defined
        if request['dataMode'] == 'params':
            for parameter in request_data:
                param_value = parameter['value']
                param_key = parameter['key']
                print(f"{BOLD}- Request Body: {END}{YELLOW}{param_key}{END}={GREEN}{param_value}{END}{END}")
        elif request['dataMode'] == 'raw':
            print(f"{BOLD}- Request Body: {END}{GREEN}{request['rawModeData']}{END}{END}")
        for param_name in request_query_params:
            print(f"{BOLD}- Parameter: {END}{YELLOW}{param_name['key']}{END}={GREEN}{param_name['value']}{END}")
        if request["preRequestScript"] != None:
            print(f"{BOLD}- Pre-Request Script: {END}{GREEN}{request['preRequestScript']}{END}")
    
    def _show_formatted_user(self, profile, collections, workspaces):
        print(f"{BOLD}- Username: {END}{CYAN}{profile['info']['slug']}{END}")
        print(f"{BOLD}- Friendly: {END}{CYAN}{profile['info']['friendly']}{END}")
        print(f"{BOLD}- User ID: {END}{YELLOW}{profile['entity_id']}{END}\n")
        print(f"{BOLD}Collections:{END}")
        for entity in collections['data']['collections']:
            entity_id = entity['entityId']
            entity_name = entity['name']
            print(f" - {YELLOW}{entity_id}{END}{END} ({entity_name}{END})")
        print(f"\n{BOLD}Workspaces:{END}")
        for entity in workspaces['data']['workspaces']:
            entity_id = entity['entityId']
            entity_name = entity['name']
            print(f" - {YELLOW}{entity_id}{END}{END} ({entity_name}{END})")
        print(f"\n{BOLD}Teams:{END}")
        for entity in profile['info']['teams']:
            entity_id = entity['id']
            entity_name = entity['friendly']
            print(f" - {YELLOW}{entity_id}{END}{END} ({entity_name}{END})")
            
    def _show_formatted_team(self, profile, collections, workspaces, members):
        print(f"{BOLD}- Team Name: {END}{CYAN}{profile['info']['slug']}{END}")
        print(f"{BOLD}- Friendly: {END}{CYAN}{profile['info']['friendly']}{END}")
        print(f"{BOLD}- Team ID: {END}{YELLOW}{profile['entity_id']}{END}\n")
        print(f"{BOLD}Collections:{END}")
        for entity in collections['data']['collections']:
            entity_id = entity['entityId']
            entity_name = entity['name']
            print(f" - {YELLOW}{entity_id}{END}{END} ({entity_name}{END})")
        print(f"\n{BOLD}Workspaces:{END}")
        for entity in workspaces['data']['workspaces']:
            entity_id = entity['entityId']
            entity_name = entity['name']
            print(f" - {YELLOW}{entity_id}{END}{END} ({entity_name}{END})")
        print(f"\n{BOLD}Members:{END}")
        for entity in members:
            user_name = entity['user_id']
            user_id = entity['friendly']
            print(f" - {YELLOW}{user_name}{END}{END} ({user_id}{END})")

    def search(self, term, page=None, indice=None, limit=100):
        if limit is not 100:
            limit = int(limit)
        if page is not None:
            page = int(page)*limit
        else:
            page = 0
        search_headers = {
            "Content-Type": "application/json",
            "X-App-Version": "10.18.8-230926-0808",
            "X-Entity-Team-Id": "0",
            "Origin": "https://www.postman.com",
            "Referer": "https://www.postman.com/search?q=&scope=public&type=all",
        }
        
        if indice is not None:
            if indice in self.INDICE_KEYWORDS:
                queryIndices = [self.INDICE_KEYWORDS[indice]]
            else:
                raise ValueError("Invalid keyword provided for 'indice'")
        else:
            queryIndices = [
                "collaboration.workspace",
                "runtime.collection",
                "runtime.request",
                "adp.api",
                "flow.flow",
                "apinetwork.team"
            ]
        
        search_data = {
            "service": "search",
            "method": "POST",
            "path": "/search-all",
            "body": {
                "queryIndices": queryIndices,
                "queryText": "{0}".format(term),
                "size": limit,
                "from": page,
                "clientTraceId": "",
                "requestOrigin": "srp",
                "mergeEntities": "true",
                "nonNestedRequests": "true",
                "domain": "public"
            }
        }
        response = requests.post(self.WS_API_URL, headers=search_headers, json=search_data, proxies=self.proxies, verify=False)
        return response.text

    def search_stats(self, term):
        stat_headers = {
            "Content-Type": "application/json",
            "X-App-Version": "10.18.8-230926-0808",
            "X-Entity-Team-Id": "0",
            "Origin": "https://www.postman.com",
            "Referer": "https://www.postman.com/search?q=&scope=public&type=all",
        }
        stat_data = {
            "service":"search",
            "method":"POST",
            "path":"/count",
            "body": {
                "queryText":"{0}".format(term),
                "queryIndices":[
                    "collaboration.workspace",
                    "runtime.collection",
                    "runtime.request",
                    "adp.api",
                    "flow.flow",
                    "apinetwork.team"
                    ],
                "domain":"public"
            }
        }
        response = requests.post(self.WS_API_URL, headers=stat_headers, json=stat_data, proxies=self.proxies, verify=False)
        return response.text
    
    def build_curl_request(self, request):
        curl_request = f"curl -X {request['method']} '{YELLOW}{request['url']}{END}' \\\n"
        for header in request['headerData']:
            curl_request += f"-H '{YELLOW}{header['key']}{END}: {GREEN}{header['value']}{END}' \\\n"
        try:
            if request['auth']['type'] == 'basic':
                curl_request += f"-u '{GREEN}{request['auth']['basic'][1]['value']}{END}:{GREEN}{request['auth']['basic'][0]['value']}{END}' \\\n"
            elif request['auth']['type'] == 'oauth2':
                # add oauth2 oauth1 etc support
                pass
        except:
            pass
        if request['dataMode'] == 'params':
            for parameter in request['data']:
                curl_request += f"-d '{YELLOW}{parameter['key']}{END}={GREEN}{parameter['value']}{END}' "
        elif request['dataMode'] == 'raw':
            curl_request += f"--data-raw '{GREEN}{request['rawModeData']}{END}'"
        return curl_request

    def workspace(self, id):
        response = requests.get(f'https://www.postman.com/_api/workspace/{id}', proxies=self.proxies, verify=False)
        return response.text
    
    def workspace_globals(self, id):
        response = requests.get(f'https://www.postman.com/_api/workspace/{id}/globals', proxies=self.proxies, verify=False)
        return response.text
    
    def collection(self, id):
        response = requests.get(f'https://www.postman.com/_api/collection/{id}', proxies=self.proxies, verify=False)
        return response.text
    
    def collections(self, id):
        response = requests.post(f'https://www.postman.com/_api/list/collection?workspace={id}', proxies=self.proxies, verify=False)
        return response.text

    def request(self, id):
        response = requests.get(f'https://www.postman.com/_api/request/{id}', proxies=self.proxies, verify=False)
        return response.text
    
    def environment(self, id):
        response = requests.get(f'https://www.postman.com/_api/environment/{id}', proxies=self.proxies, verify=False)
        return response.text
    
    def profile(self, handle):
        header = {
            'Content-Type': 'application/json'
        }
        postdata = {
            "path": f'/api/profiles/{handle}',
            "service": "ums",
            "method": "get"
        }
        response = requests.post(self.WS_API_URL, json=postdata, headers=header, proxies=self.proxies, verify=False)
        return response.text
    
    def user(self, userid):
        headers = {
            'Content-Type': 'application/json'
        }
        postdata = {
            "service":"publishing",
            "method":"get",
            "path":f"/v1/api/profile/user/{userid}"
        }
        response = requests.post(self.WS_API_URL, json=postdata, headers=headers, proxies=self.proxies, verify=False)
        return response.text   
    
    def user_collections(self, userid):
        headers = {
            'Content-Type': 'application/json'
        }
        postdata = {
            "service":"publishing",
            "method":"get",
            "path":f"/v1/api/profile/user/{userid}?requestedData=collection"
        }
        response = requests.post(self.WS_API_URL, json=postdata, headers=headers, proxies=self.proxies, verify=False)
        return response.text

    def user_workspaces(self, userid):
        headers = {
            'Content-Type': 'application/json'
        }
        postdata = {
            "service":"publishing",
            "method":"get",
            "path":f"/v1/api/profile/user/{userid}?requestedData=workspace"
        }
        response = requests.post(self.WS_API_URL, json=postdata, headers=headers, proxies=self.proxies, verify=False)
        return response.text

    def team(self, teamid):
        headers = {
            'Content-Type': 'application/json'
        }
        postdata = {
            "service":"publishing",
            "method":"get",
            "path":f"/v1/api/profile/team/{teamid}"
        }
        response = requests.post(self.WS_API_URL, json=postdata, headers=headers, proxies=self.proxies, verify=False)
        return response.text
    
    def team_collections(self, teamid):
        headers = {
            'Content-Type': 'application/json'
        }
        postdata = {
            "service":"publishing",
            "method":"get",
            "path":f"/v1/api/profile/team/{teamid}?requestedData=collection"
        }
        response = requests.post(self.WS_API_URL, json=postdata, headers=headers, proxies=self.proxies, verify=False)
        return response.text

    def team_workspaces(self, teamid):
        headers = {
            'Content-Type': 'application/json'
        }
        postdata = {
            "service":"publishing",
            "method":"get",
            "path":f"/v1/api/profile/team/{teamid}?requestedData=workspace"
        }
        response = requests.post(self.WS_API_URL, json=postdata, headers=headers, proxies=self.proxies, verify=False)
        return response.text