import secrets
from selenium.webdriver.common.by import By
from time import sleep
import config

class PostPage:
    def __init__(self, driver, id):
        self.driver = driver
        self.id = id
        self.posts_to_like = config.posts_to_like
        self.posts_to_comment = config.posts_to_comment
        self.comments_good = config.comments_good
        self.comments_bad = config.comments_bad
        self.postUrl = []
        self.likeStatus = ""
        self.commentStatus = False
        self.commentInput = []
        self.commentText = ""
    
    def likePost(self, url="from list"):
        if url == "from list":
            if len(self.posts_to_like) == 0 or self.posts_to_like[0] == "":
                print(f"[Драйвер - {self.id}] Список постов для лайков пуст")
                return 0
            self.postUrl = self.posts_to_like.copy()
        else:
            self.postUrl.append(url)
        # Начало поставления лайка
        for i in range(0, len(self.postUrl)):
            self.driver.get(self.postUrl[i])
            print(f"[Драйвер - {self.id}] Успешный переход по ссылке {self.postUrl[i]}")
            try:
                # Проверка на наличие лайка, после чего ставится сам лайк
                sleep(config.sleep_time)
                try:
                    self.likeStatus = self.driver.find_element(By.CSS_SELECTOR, "._aamw > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)").get_attribute("aria-label")
                except Exception as e:
                    try:
                        self.likeStatus = self.driver.find_element(By.CSS_SELECTOR, "._aamw > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)").get_attribute("aria-label")
                    except Exception as e:
                        print(f"[Драйвер - {self.id}] Не удалось найти состояние кнопки лайка")
                        return 0
                if self.likeStatus == "unlike" or self.likeStatus == "Не нравится":
                    print(f"[Драйвер - {self.id}] Пост {self.postUrl[i]} уже был лайкнут")
                    return 0
                elif self.likeStatus == "like" or self.likeStatus == "Нравится":
                    self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button").click()
                    sleep(config.sleep_time)
            except Exception as e:
                print(e)
                print(f"[Драйвер - {self.id}] Не смог лайкнуть пост {self.postUrl[i]}")
            else:    
                print(f"[Драйвер - {self.id}] Пост успешно лайкнут {self.postUrl[i]}")

    def commentPosts(self, comment="good", url="from list"):
        if url == "from list":
            if len(self.posts_to_comment) == 0 or self.posts_to_comment[0] == "":
                print(f"[Драйвер - {self.id}] Список постов для комментариев пуст")
                return 0
            self.postUrl = self.posts_to_comment.copy()
        else:
            self.postUrl.append(url)
        if comment == "good":
            self.commentText = secrets.choice(config.comments_good)
        elif comment == "bad":
            self.commentText = secrets.choice(config.comments_bad)
        else:
            self.commentText = comment
        # Начало поставления комментария
        for i in range(0, len(self.postUrl)):
            self.driver.get(self.postUrl[i])
            print(f"[Драйвер - {self.id}] Успешный переход по ссылке {self.postUrl[i]}")
            try:
                sleep(config.sleep_time)
                try:
                    self.driver.find_element(By.XPATH, f"//a[contains(@href="+config.login_data[self.id]['username'])
                except Exception:
                    self.commentInput.append(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea"))
                    self.commentInput[0].send_keys(self.commentText)
                    sleep(config.sleep_time)
                    self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button").click()
                else:
                    print(f"[Драйвер - {self.id}] Пост {self.postUrl[i]} уже был прокомментирован")
                sleep(config.sleep_time)
            except Exception:
                print(f"[Драйвер - {self.id}] Не смог прокомментировать пост {self.postUrl[i]}")
            else:
                print(f"[Драйвер - {self.id}] Пост успешно прокомментирован {self.postUrl[i]}")