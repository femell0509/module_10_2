import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self, enemy=100, counter=0):
        print(f'{self.name}, на нас напали!')

        while enemy>0:
            enemy -= self.power
            counter += 1
            time.sleep(1)
            print(f'{self.name} сражается {counter} день(дня), осталось {enemy} воинов.')
        print(f'{self.name} одержал победу спустя {counter} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight =Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')