import sys, json
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def main():
    p = porchpirate()
    profile = json.loads(p.profile('redacted'))
    print(profile)

if __name__ == "__main__":
    main()