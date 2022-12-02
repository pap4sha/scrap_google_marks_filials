from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.wheel_input import ScrollOrigin# import requestsdef get_sourse_html(url):





    driver = webdriver.Chrome(executable_path='C:/Users/tat100zmi/PycharmProjects/chrome_webdriver/chromedriver.exe')

    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)
        while True:
            find_more_element = driver.find_element(By.CLASS_NAME, "m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd")
            print (find_more_element)
            if driver.find_elements(By.CLASS_NAME, "HlvSq"):

                with open("test.html", "w", encoding = "utf-8") as file:
                    file.write(driver.page_source)

                break            else:
                delta_y = find_more_element.rect['y']
                # scroll_origin = ScrollOrigin.from_element(find_more_element, 0 -50)                actions2 = ActionChains(driver)
                actions2.key_down(Keys.DOWN, find_more_element).perform()
                time.sleep(3)

    except Exception as ex:
        print (ex)
    finally:
        driver.close()
        driver.quit()


get_sourse_html(url = 'https://www.google.ru/maps/search/%D1%82%D0%B0%D1%82%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC/@55.7335076,48.9299553,8z')
