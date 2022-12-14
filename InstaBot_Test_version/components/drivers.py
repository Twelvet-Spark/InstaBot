from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.PostPage import PostPage
from selenium.webdriver.firefox.options import Options

class Drivers():
    def __init__(self, amount, http, headless=False):
        self.headless = headless
        self.amount = amount
        self.options = Options()
        self.http = http
        self.drivers = []
        self.driver = ""

    def create_drivers(self):
        if self.headless == True:
            self.options.headless = True
        for i in range(0, self.amount):
            self.driver = webdriver.Firefox(options=self.options)
            self.driver.implicitly_wait(5)
            self.drivers.append(self.driver)
        print(f"Создано {self.amount} драйверов, режим headless = {self.options.headless}\n")

    def get_drivers(self):
        return self.drivers

    def get_driver(self, index):
        return self.drivers[index]

    def start_drivers(self):
        for i in range(0, self.amount):
            self.drivers[i].get(self.http)
            print(f"[Драйвер - {i}] Успешный переход по ссылке {self.http}\n")

    def stop_drivers(self):
        for i in range(0, self.amount):
            self.drivers[i].close()
        print(f"Все {self.amount} драйвера закрыты\n")

    def login_drivers(self):
        for i in range(0, self.amount):
            LoginPage(self.drivers[i], i).login()

    def like_posts(self, url="from list"):
        for i in range(0, self.amount):
            PostPage(self.drivers[i], i).likePost(url)

    def comment_posts(self, comment="good", url="from list"):
        for i in range(0, self.amount):
            PostPage(self.drivers[i], i).commentPosts(comment, url)