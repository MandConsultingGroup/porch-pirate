import sys
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def main():
    p = porchpirate()
    print(p.search_stats('bell.ca'))

if __name__ == "__main__":
    main()