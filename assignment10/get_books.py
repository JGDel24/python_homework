from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time
from pathlib import Path


# Task 3
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)


time.sleep(3)


li_elements = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")
print("Filtered:", len(li_elements), "search results")

results = []


for li in li_elements:
    try:
        
        title = li.find_element(By.CSS_SELECTOR, "span.title-content").text

        
        author_elems = li.find_elements(By.CSS_SELECTOR, "a.author-link")
        authors = "; ".join([a.text for a in author_elems]) if author_elems else "Unknown"

        
        format_year = li.find_element(By.CSS_SELECTOR, "span.display-info-primary").text

       
        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        })
    except Exception as e:
        print("Error processing entry:", e)


df = pd.DataFrame(results)
print(df)


driver.quit()

#task4

df = pd.DataFrame(results)
print(df)

base_dir = Path(__file__).parent.resolve()

csv_path = base_dir / "get_books.csv"
json_path = base_dir / "get_books.json"

df.to_csv(csv_path, index=False)
print(f"CSV {csv_path}")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print(f"JSON to {json_path}")    


