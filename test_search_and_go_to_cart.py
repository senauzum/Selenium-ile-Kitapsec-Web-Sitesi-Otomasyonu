from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep
chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
video_url="https://www.kitapsec.com/"
driver.get(video_url)
wait = WebDriverWait(driver, 10)

print(f"Bulunduğunuz sayfanın linki:{driver.current_url}")
print(f"Sayfa Başlığı:{driver.title}")
driver.maximize_window()

search_input=wait.until(EC.element_to_be_clickable((By.ID,"yeniAramaInput")))
search_input.send_keys("Kürk Mantolu Madonna")

search_button=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"ARA")))
search_button.click()

selected_book=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Kürk Mantolu Madonna Yapı Kredi Yayınları")))
selected_book.click()

driver.execute_script("window.scrollBy(0,250)")

wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Sepete Ekle"))).click()

wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.sweet-overlay")))
wait.until(EC.element_to_be_clickable((By.ID, "sptHdCountText"))).click()

sleep(2)
driver.quit()