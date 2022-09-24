from time import sleep
import config
from components.drivers import Drivers
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from selenium import webdriver
from selenium.webdriver.common.by import By

# Drivers(Количество ботов, ссылка на соц. сеть, режим без открытия окна браузера(headless))
# Количество ботов зависит от количества аккаунтов, которые прописаны в config.py
# Поддерживается только www.instagram.com
# Режим headless - обеспечивает работу ботов без открытия окна браузера

browser_drives = Drivers((len(config.login_data)), 'https://www.instagram.com/', False)
browser_drives.create_drivers()
browser_drives.start_drivers()
browser_drives.login_drivers()
browser_drives.like_posts()
browser_drives.comment_posts("good")
print("Драйвера закончили работу, нажмите Enter для выключения")
input()
browser_drives.stop_drivers()

# TODO:
# Сделать проверку на существование комментария под постом от имени драйвера