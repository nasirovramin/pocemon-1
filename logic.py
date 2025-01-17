from random import randint
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.last_feed_time = datetime.now()
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(50,100)
        self.power = randint(10,20)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["sprites"]["other"]["dream_world"]["front_default"])
        else:
            return "https://kartinki.pics/82041-pokemon-pikachu-kartinki.html"
        

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        

def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"


    # Метод класса для получения информации
def info(self):
        return f"""Имя твоего покеомона: {self.name}
Здоровье покемона: {self.hp}
Сила покемона: {self.power}"""

    # Метод класса для получения картинки покемона
def show_img(self):
        return self.img


def attack(self, enemy):
    if isinstance(enemy,Wizard):
        chanche = randint(1,5)
        if chanche == 1:
            return "Покемон волшебник примянил шит"
    if enemy.hp > self.power:
        enemy.hp -= self.power
        return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
    else:
        enemy.hp = 0
        return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    



class Wizard(Pokemon):
    def feed(self):
        return super().feed(hp_increase = 20)



class Wizard(Pokemon):
    def info(self):
        return "У тебя покемон волшебник" + super().info()


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5, 15)
        self_power = self_power
        result = super().attack(enemy)
        self.power = super_power
        return result + f"Бэст пременил суператаку с силой {super_power}"
    


    def feed(self):
        return super().feed(hp_iterval = 10)
    

    def info(self):
        return "У тебя покемон боец" + super().info()
    

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))    

