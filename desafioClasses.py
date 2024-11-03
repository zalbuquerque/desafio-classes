class Hero:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def atacar(self):
        if self.type == "mago":
            attack = "magia"
        elif self.type == "guerreiro":
            attack = "espada"
        elif self.type == "monge":
            attack = "artes marciais"
        elif self.type == "ninja":
            attack = "shuriken"
        else:
            attack = "ataque desconhecido"
        
        print(f"o {self.type} atacou usando {attack}")


def main():
    heroes = [
        Hero("Morgana", 35, "mago"),
        Hero("Garen", 30, "guerreiro"),
        Hero("Lee Sin", 25, "monge"),
        Hero("Akali", 28, "ninja"),
        Hero("Caitlyn", 29, "atirador")
    ]
    
    for hero in heroes:
        hero.atacar()

if __name__ == "__main__":
    main()
