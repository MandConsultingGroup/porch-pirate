# Porch Pirate

![](https://i.imgur.com/CWW5b0D.png)

Porch Pirate started as a tool to quickly uncover Postman secrets, and has slowly begun to evolve into a multi-purpose reconaissance / OSINT framework for Postman. While other tools attempt to identify very specific keywords as "secrets" (and for the most part, only search for these strings in global variables), we realized we required capabilities that were "secret-agnostic", and had enough flexibility to capture false-positives that still provided offensive value.

Porch Pirate enumerates and presents sensitive results (global secrets, unique headers, endpoints, query parameters, authorization, etc), from publicly accessible Postman entities, such as:

- Workspaces
- Collections
- Requests
- Users
- Teams

## Installation

```bash
python3 -m pip install porch-pirate
```

## Using the client

![](https://i.imgur.com/t2PJ2jF.png)

The Porch Pirate client can be used to nearly fully conduct reviews on public Postman entities in a quick and simple fashion. There are intended workflows and particular keywords to be used that can typically maximize results. These methodologies can be located on our blog: **Plundering Postman with Porch Pirate**.

Porch Pirate supports the following arguments to be performed on collections, workspaces, or users.

- `--globals`
- `--collections`
- `--requests`
- `--urls`
- `--dump`
- `--raw`
- `--curl`

#### Simple Search

```bash
porch-pirate -s "coca-cola.com"
```

#### Get Workspace Globals

By default, Porch Pirate will display globals from all active and inactive environments if they are defined in the workspace. Provide a `-w` argument with the workspace ID (found by performing a simple search, or automatic search dump) to extract the workspace's globals, along with other information.

```bash
porch-pirate -w abd6bded-ac31-4dd5-87d6-aa4a399071b8
```

#### Dump Workspace

When an interesting result has been found with a simple search, we can provide the workspace ID to the `-w` argument with the `--dump` command to begin extracting information from the workspace and its collections.

```bash
porch-pirate -w abd6bded-ac31-4dd5-87d6-aa4a399071b8 --dump
```

#### Automatic Search and Globals Extraction

Porch Pirate can be supplied a simple search term, following the `--globals` argument. Porch Pirate will dump all relevant workspaces tied to the results discovered in the simple search, but only if there are globals defined. This is particularly useful for quickly identifying potentially interesting workspaces to dig into further.

```bash
porch-pirate -s "shopify" --globals
```

#### Automatic Search Dump

Porch Pirate can be supplied a simple search term, following the `--dump` argument. Porch Pirate will dump all relevant workspaces and collections tied to the results discovered in the simple search. This is particularly useful for quickly sifting through potentially interesting results.

```bash
porch-pirate -s "coca-cola.com" --dump
```

#### Extract URLs from Workspace

A particularly useful way to use Porch Pirate is to extract all URLs from a workspace and export them to another tool for fuzzing.

```bash
porch-pirate -w abd6bded-ac31-4dd5-87d6-aa4a399071b8 --urls
```

#### Automatic URL Extraction

Porch Pirate will recursively extract all URLs from workspaces and their collections related to a simple search term.

```bash
porch-pirate -s "coca-cola.com" --urls
```

#### Show Collections in a Workspace

```bash
porch-pirate -w abd6bded-ac31-4dd5-87d6-aa4a399071b8 --collections
```

#### Show Workspace Requests

```bash
porch-pirate -w abd6bded-ac31-4dd5-87d6-aa4a399071b8 --requests
```

#### Show raw JSON

```bash
porch-pirate -w abd6bded-ac31-4dd5-87d6-aa4a399071b8 --raw
```

#### Show Entity Information

```bash
porch-pirate -w WORKSPACE_ID
```
```bash
porch-pirate -c COLLECTION_ID
```
```bash
porch-pirate -r REQUEST_ID
```
```bash
porch-pirate -u USERNAME/TEAMNAME
```

### Convert Request to Curl

Porch Pirate can build curl requests when provided with a request ID for easier testing.

```bash
porch-pirate -r 11055256-b1529390-18d2-4dce-812f-ee4d33bffd38 --curl
```

### Use a proxy

```bash
porch-pirate -s coca-cola.com --proxy 127.0.0.1:8080
```

## Using as a library

#### Searching

```python
p = porchpirate()
print(p.search('coca-cola.com'))
```

#### Get Workspace Collections

```python
p = porchpirate()
print(p.collections('4127fdda-08be-4f34-af0e-a8bdc06efaba'))
```

#### Dumping a Workspace

```python
p = porchpirate()
collections = json.loads(p.collections('4127fdda-08be-4f34-af0e-a8bdc06efaba'))
for collection in collections['data']: 
    requests = collection['requests']
    for r in requests:
        request_data = p.request(r['id'])
        print(request_data)
```

#### Grabbing a Workspace's Globals

```python
p = porchpirate()
print(p.workspace_globals('4127fdda-08be-4f34-af0e-a8bdc06efaba'))
```

## Other Examples

Other library usage examples can be located in the `examples` directory, which contains the following examples:

- `dump_workspace.py`
- `format_search_results.py`
- `format_workspace_collections.py`
- `format_workspace_globals.py`
- `get_collection.py`
- `get_collections.py`
- `get_profile.py`
- `get_request.py`
- `get_statistics.py`
- `get_team.py`
- `get_user.py`
- `get_workspace.py`
- `recursive_globals_from_search.py`
- `request_to_curl.py`
- `search.py`
- `search_by_page.py`
- `workspace_collections.py`
