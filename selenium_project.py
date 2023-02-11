import selenium
import time
import loginInfo
import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

adres_kelimeleri = ("SOK", "sok.", "mah.", "MAH.", "CAD", "cad", "caddesi", "mahallesi", "Mahallesi",
                    "CD", "cd", "bulvarı", "BULVARI", "Apartmanı", "apartmanı", "apt", "CADDESİ", "BLOK", "Blok", "Binası", "cad.", "CAD.", "Bulvarı", "Sok.", "sok.", "sokağı", "salonu", "girişi", "binası", "BİNASI", "BLOK", "Apt.", "Apt", "apt", "apt.", "Mah.", "Mah", "Blv.", "BLV", "APARTMANI", "HATAY", "Hatay", "hatay", "Maraş", "Kahramanmaraş", "KAHRAMANMARAŞ", "Mersin", "MERSİN", "blok", "sitesi", "Sitesi", "SİTESİ", "BLOK", "Blok")


def deprem_adresi_bul():
    subject = "ses var"
    Tweets = []
    refinedTweets = list()
    service = Service(executable_path="/Users/apple/Downloads/geckodriver")

    with webdriver.Firefox(service=service) as driver:
        # navigate to the url
        driver.get('https://twitter.com')
        # find element by xpath
        login = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span')
        login.click()
        time.sleep(5)
        username = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(loginInfo.username)
        next = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
        next.click()
        time.sleep(5)
        password = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(loginInfo.password)
        time.sleep(1)
        finish_login = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        finish_login.click()
        time.sleep(5)
        searchArea = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
        searchArea.send_keys("ses geliyor")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
        articles = driver.find_elements(
            By.XPATH, "//article[@data-testid='tweet']")
        while True:
            tweet = {

                "UserTags": '',
                "TimeStamps": '',
                "Body": ''

            }
            # insert a dict here instead of a list
            for article in articles:
                UserTag = driver.find_element(
                    By.XPATH, ".//div[@data-testid='User-Names']").text
                tweet["UserTags"] = UserTag

                TimeStamp = driver.find_element(
                    By.XPATH, ".//time").get_attribute('datetime')
                tweet["TimeStamps"] = TimeStamp

                Tweet_body = driver.find_element(
                    By.XPATH, ".//div[@data-testid='tweetText']").text
                tweet["Body"] = Tweet_body
            if tweet["TimeStamps"][8] == '1':
                Tweets.append(tweet)

            driver.execute_script(
                'window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(3)
            articles = driver.find_elements(
                By.XPATH, "//article[@data-testid='tweet']")
            print("a")
            if len(Tweets) > 10:
                break

        for tweet in Tweets:
            temp_list = tweet['Body'].split(" ")
            print(temp_list)
            for i in temp_list:

                i = i.replace('\n', '')
                print(i)
                if i in adres_kelimeleri:
                    print('c')
                    refinedTweets.append(tweet)
                    break
    print(Tweets)
    print(refinedTweets)
    return (refinedTweets)


if __name__ == "__main__":
    deprem_adresi_bul()
