from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep
chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
video_url="https://www.kitapsec.com/"
driver.get(video_url)
wait = WebDriverWait(driver, 10)
driver.maximize_window()

children_book_menu=wait.until( EC.element_to_be_clickable((By.LINK_TEXT,"ÇOCUK KİTABI")))
children_book_menu.click()
world_classics_category=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Dünya Klasikleri")))
world_classics_category.click()

driver.execute_script("window.scrollBy(0,1300)")

is_bankasi_kultur=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"İş Bankası Kültür Yayınları (45)")))
is_bankasi_kultur.click()

driver.execute_script("window.scrollBy(0,1600)")

min_price=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div[1]/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/table[2]/tbody/tr[4]/td/div/table/tbody/tr/td[1]/select')))
min_price.click()
min_price = Select(driver.find_element(By.NAME, "FiyatBaslangic"))
min_price.select_by_value("50")

max_price=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div[1]/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/table[2]/tbody/tr[4]/td/div/table/tbody/tr/td[3]/select')))
max_price.click()
max_price = Select(driver.find_element(By.NAME, "FiyatBitis"))
max_price.select_by_value("100")

price_filter_search_button=wait.until(EC.element_to_be_clickable((By.NAME,"B1")))
price_filter_search_button.click()

driver.execute_script("window.scrollBy(0,250)")

selected_book=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Peter Pan J.M.Barrie İş Bankası Kültür Yayınları")))
selected_book.click()

driver.execute_script("window.scrollBy(0,250)")

increase_quantity_button=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"+")))
increase_quantity_button.click()
add_to_cart_button=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Sepete Ekle")))
add_to_cart_button.click()

sleep(2)
driver.quit()