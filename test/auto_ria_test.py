from page.google_search import googleMainPage
import time

page = googleMainPage()
page.screenshot_befo()
page.search_item("some text")
page.start_search()
time.sleep(2)
assert page.ass_result != "0"
page.screenshot_after()
page.quit()