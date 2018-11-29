import NameGenerator

class Entity():
    components = []

def makeCharacter():
    character = Entity()
    return character

def main():
    tim = Entity()
    for i in range(10):
        print(hash(tim))

main()