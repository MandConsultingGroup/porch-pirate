import sys
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def main():
    p = porchpirate()
    print(p.search('bell.ca', 'workspace')) # Search custom indice with keyword
    print(p.search('bell.ca')) # Regular search

if __name__ == "__main__":
    main()