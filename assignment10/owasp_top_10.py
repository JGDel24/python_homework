from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By        
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import csv


options = Options()
options.add_argument("--headless") 


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://owasp.org/www-project-top-ten/")


vulns = driver.find_elements(By.XPATH, "//li//a[strong]")

top_10_list = []
for v in vulns:
    title = v.text
    link = v.get_attribute("href")
    top_10_list.append({"title": title, "link": link})

driver.quit()


print(top_10_list)


with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "link"])
    writer.writeheader()
    writer.writerows(top_10_list)
