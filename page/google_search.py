from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Werrione\\Desktop\\Web_test\\resourses\\chromedriver.exe")
class googleMainPage():
    def __init__(self):
        driver.get("https://www.google.com.ua/")

    def search_item(self, item_name):
        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys(item_name)

    def start_search(self):
        search_btn = driver.find_element_by_xpath("//input[@name='btnK']")
        search_btn.submit()

    def ass_result(self):
        result = int(driver.find_element_by_id('result-stats'))
        return result

    def quit(self):
        driver.quit()

    def screenshot_befo(self):
        driver.save_screenshot('before_search.png')

    def screenshot_after(self):
        driver.save_screenshot('after_search.png')


