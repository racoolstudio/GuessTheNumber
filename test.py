from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/racool/Desktop/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)
movie = "black panther"
driver.get("https://www.rottentomatoes.com/search")

time(2)
print("got")
searchBar = driver.find_element(By.CLASS_NAME, "search-text")
searchBar.send_keys(movie)
print("entered")

time(2)
searchBar.send_keys(Keys.RETURN)
time(10)
# driver.quit()
