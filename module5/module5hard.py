import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return self.nickname

    def __eq__(self, other_nickname):
        return self.nickname == other_nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other_title):
        return self.title == other_title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users:
            i = self.users.index(nickname)
            if self.users[i].password == hash(password):
                self.current_user = self.users[i]
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
            return
        self.current_user = User(nickname, password, age)
        self.users.append(self.current_user)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title in self.videos:
                print(f"Видео '{video.title}' уже существует.")
            else:
                self.videos.append(video)

    def get_videos(self, word):
        word = word.lower()
        return [video.title for video in self.videos if word in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        if title not in self.videos:
            print("Видео не найдено.")
            return

        video = self.videos[self.videos.index(title)]

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        while video.time_now < video.duration:
            print(video.time_now + 1, end=' ')
            video.time_now += 1
            time.sleep(1)
        print("Конец видео")
        video.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
