from random import randint
from threading import Thread, Lock
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return self.name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.guests_queue = Queue()
        self.free_tables_queue = Queue(maxsize=len(tables))
        self.occupied_tables_queue = Queue(maxsize=len(tables))
        self.lock = Lock()
        for table in self.tables:
            self.free_tables_queue.put(table)

    def __exists_guest(self):
        return not self.guests_queue.empty() or not self.occupied_tables_queue.empty()

    def guest_arrival(self, *guests):
        """Прибытие гостей"""
        for guest in guests:
            if not self.free_tables_queue.empty():
                table = self.free_tables_queue.get()
                table.guest = guest
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
                self.occupied_tables_queue.put(table)
                guest.start()
            else:
                self.guests_queue.put(guest)
                print(f"{guest.name} в очереди")

    def __guests_stand_up(self):
        while self.__exists_guest():
            with self.lock:
                if not self.occupied_tables_queue.empty():
                    table = self.occupied_tables_queue.get()
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        table.guest = None
                        self.free_tables_queue.put(table)
                        print(f"Стол номер {table.number} свободен")
                    else:
                        self.occupied_tables_queue.put(table)  # возвращаем занятый столик в конец очереди
            sleep(0.1)

    def __guests_sit_down(self):
        while not self.guests_queue.empty():
            with self.lock:
                if not self.guests_queue.empty() and not self.free_tables_queue.empty():
                    guest = self.guests_queue.get()
                    table = self.free_tables_queue.get()
                    table.guest = guest
                    self.occupied_tables_queue.put(table)
                    print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    guest.start()
            sleep(0.1)

    def discuss_guests(self):
        """Обслужить гостей"""
        sit_down_thread = Thread(target=Cafe.__guests_sit_down, args=(self,))
        stand_up_thread = Thread(target=Cafe.__guests_stand_up, args=(self,))
        sit_down_thread.start()
        stand_up_thread.start()
        sit_down_thread.join()
        stand_up_thread.join()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
