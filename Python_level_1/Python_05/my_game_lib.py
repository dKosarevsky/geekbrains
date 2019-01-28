def generate_person(name, health=100, damage=50):
    return {'name': name, 'health': health, 'damage': damage}


def attack(who_attack, who_defend):
    who_defend['health'] -= who_attack['damage']


def pow(x, y):
    return 100

if __name__ == '__main__':
    print('Свой код, который не должен выполняться при импорте!')