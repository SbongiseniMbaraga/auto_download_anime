import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
anime_website = 'https://animixplay.to/'
driver.get(anime_website)

#selects the search bar
anime_name = 'Fumetsu no Anata e'
search_bar = driver.find_element_by_xpath('/html/body/div[3]/div/button[2]/i')
search_bar.click()

#send the name of the anime to the search bar then presses enter
text_bar = driver.find_element_by_xpath('/html/body/div[3]/div/div/input[3]')
text_bar.send_keys(anime_name)
time.sleep(2)
text_bar.send_keys(Keys.ENTER)

#when at the next page it will get the anime you are looking for and check if the anime exists
time.sleep(2)
results = driver.find_elements_by_tag_name('li')

your_anime = False
for i in results:
    if anime_name in i.text:
        your_anime = True
        i.click()
        break

#clicks on the download button
time.sleep(2)
results = driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[2]/i[3]')
results.click()

#downloads page
time.sleep(5)
driver.switch_to_window(driver.window_handles[-1])
results = driver.find_elements_by_class_name('dowload')

#downloads the anime
for all_links in results:
    video_resolution = '1080P'

    if video_resolution in all_links.text:
        print(all_links.text)
        all_links.click()



