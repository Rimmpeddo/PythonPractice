import random as rand

class Tortoise(object):
    def __init__(self):
        self.x = rand.randint(0,10)
        self.y = rand.randint(0,10)

        self.power = 100

    def move(self):
        new_x = self.x + rand.choice([1,2,-1,-2])
        new_y = self.y + rand.choice([1,2,-1,-2])

        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        self.power -= 1
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish(object):
    def __init__(self):
        self.x = rand.randint(0,10)
        self.y = rand.randint(0,10)

    def move(self):
        new_x = self.x + rand.choice([1,-1])
        new_y = self.y + rand.choice([1,-1])

        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        return (self.x, self.y)

tort = Tortoise()
fish = []

for i in range(10):
    new_fish = Fish()
    fish.append((new_fish))

while True:
    if not tort.power:
        print("乌龟生命耗尽,没有吃完所有的鱼")
        break
    if not len(fish):
        print("鱼被吃完了,恭喜你，eat total")
        break

    pos = tort.move()

    for eath_fish in fish[:]:
        if eath_fish.move() == pos:
            tort.eat()
            fish.remove(eath_fish)
            print("乌龟吃了一条鱼")