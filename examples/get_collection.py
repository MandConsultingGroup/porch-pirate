import sys
sys.path.append('../src/porch-pirate')
from porchpirate import porchpirate

def main():
    p = porchpirate()
    print(p.collection('2052387-7555e373-ccca-41df-bc62-13c1b3cf393b'))
    
if __name__ == "__main__":
    main()