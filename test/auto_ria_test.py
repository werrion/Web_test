from page.auto_ria_page import googleMainPage

page = googleMainPage()
page.search_item("some_text")
page.click()
assert page.get_amount_of_found() < 0
