from page.google_search import googleMainPage

page = googleMainPage()
page.search_item("some text")
page.start_search()
assert page.ass_result != "0"
page.quit()