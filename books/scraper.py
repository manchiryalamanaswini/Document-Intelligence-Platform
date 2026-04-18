from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_books():
    driver = webdriver.Chrome()
    driver.get("https://books.toscrape.com/")

    books = []

    items = driver.find_elements(By.CLASS_NAME, "product_pod")

    for item in items[:5]:
        title = item.find_element(By.TAG_NAME, "h3").text
        price = item.find_element(By.CLASS_NAME, "price_color").text

        books.append({
            "title": title,
            "author": "Unknown",
            "description": price,
            "url": "https://books.toscrape.com/"
        })

    driver.quit()
    return books