from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def likePost(self):
        print("Post Liked")