from random import randint
from time import sleep
import threading


class Bank:
    def __init__(self):
        self.balance = 0
        self.account = threading.Lock()
        self.lock = threading.Lock()

    def _transaction(self, value):
        with self.account:
            if value > 0:
                self.balance += value
                print(f"Пополнение: {value}. Баланс: {self.balance}")
            elif value < 0:
                value = -value
                print(f"Запрос на {value}")
                if self.balance > value:
                    self.balance -= value
                    print(f"Снятие: {value}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")

    def deposit(self):
        for _ in range(100):
            self._transaction(randint(50, 500))
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            if self.lock.locked():
                sleep(0.1)
            take_sum = randint(50, 500)
            if take_sum > self.balance:
                self.lock.acquire(blocking=False)
            self._transaction(-take_sum)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
