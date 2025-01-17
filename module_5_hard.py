from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.user = []
        self.video = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.user:
            if user.nickname == nickname and hash(user, password) == hash(password):
                self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        password = hash(password)
        for user in self.user:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.user.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def __add__(self, *arg):
        for movie in args:
            if movie not in self.video:
                self.video.append(movie)

    def watch_video(self, movie):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for i in range(self.video[j].duration):
            self.video[j].time_now += 1
            self.video[j].time_now = 0
            print(i + 1, end='')
            sleep(1)
        print("Конец видео")

if __name__ == "__main__":

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень програмист?', 10, adult_mode = True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
