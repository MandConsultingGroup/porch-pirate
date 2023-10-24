import sys, json
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def _show_formatted_user_collections(userprofile):
    for entity in userprofile['data']['collections']:
        entity_id = entity['entityId']
        entity_type = entity['entityType']
        entity_name = entity['name']
        entity_profile_name = entity['publisherInfo']['publicHandle']
        print(entity_id, entity_type, entity_name, entity_profile_name)

def _show_formatted_user_workspaces(userprofile):
    for entity in userprofile['data']['workspaces']:
        entity_id = entity['entityId']
        entity_type = entity['entityType']
        entity_name = entity['name']
        entity_profile_name = entity['publisherInfo']['publicHandle']
        print(entity_id, entity_type, entity_name, entity_profile_name)

def _show_formatted_user_teams(userprofile):
    for entity in userprofile:
        friendly = entity['friendly']
        is_public = entity['is_public']
        public_url = entity['public_url']
        teams_id = entity['id']
        print(friendly, is_public, public_url, teams_id)

def main():
    p = porchpirate()
    # Profile Information
    profile = json.loads(p.profile('redacted'))

    collections = json.loads(p.user_collections(profile['entity_id']))
    _show_formatted_user_collections(collections)

    # Load & Print Workspaces
    workspaces = json.loads(p.user_workspaces(profile['entity_id']))
    _show_formatted_user_workspaces(workspaces)

    # Print Teams
    teams = profile['info']['teams']
    _show_formatted_user_teams(teams)
    


if __name__ == "__main__":
    main()