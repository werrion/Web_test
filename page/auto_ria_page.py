from selenium import webdriver

class googleMainPage():
    def __init__(self):
        self.driver = webdriver.Chrome("C:\Users\Werrione\Desktop\Web_test\resourses\chromedriver.exe")
        self.driver.get("https://www.google.com.ua/")

    def search_item(self, item_name):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear
        self.search_field.send_keys(item_name)

    def start_search(self):
        self.search_btn = self.driver.find_element_by_css_selector("gNO89b")
        self.search_btn.click()