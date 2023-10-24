import sys, json
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def _show_formatted_team_collections(userprofile):
    for entity in userprofile['data']['collections']:
        entity_id = entity['entityId']
        entity_type = entity['entityType']
        entity_name = entity['name']
        entity_profile_name = entity['publisherInfo']['publicHandle']
        print(entity_id, entity_type, entity_name, entity_profile_name)

def _show_formatted_team_workspaces(userprofile):
    for entity in userprofile['data']['workspaces']:
        entity_id = entity['entityId']
        entity_type = entity['entityType']
        entity_name = entity['name']
        entity_profile_name = entity['publisherInfo']['publicHandle']
        print(entity_id, entity_type, entity_name, entity_profile_name)

def main():
    p = porchpirate()
    # Profile Information
    profile = json.loads(p.profile('telus-aiops'))
    collections = json.loads(p.team_collections(profile['entity_id']))
    workspaces = json.loads(p.team_workspaces(profile['entity_id']))
    #_show_formatted_team_collections(collections)
    #_show_formatted_team_workspaces(workspaces)
    print(json.dumps(profile))


if __name__ == "__main__":
    main()