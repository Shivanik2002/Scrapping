import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy,4io'

all_mobile_details = []
for page_num in range(1, 6):
    url = f"{base_url}&page={page_num}"
    driver.get(url)
    mobile_details = []

    Names = driver.find_elements(By.CSS_SELECTOR,'._4rR01T')
    Descriptions = driver.find_elements(By.CSS_SELECTOR,'._1xgFaf')
    prices = driver.find_elements(By.CSS_SELECTOR,'._1_WHN1')
    Ratings = driver.find_elements(By.CLASS_NAME,'_3LWZlK')
    Image_urls = driver.find_elements(By.TAG_NAME,'img')

    for Name, Description, price, Rating, Image_url in zip(Names, Descriptions, prices, Ratings,Image_urls):
        Description_text = Description.text
        Camera_quality = Description_text.split('\n')
        Camera_quality = Camera_quality[2]
        Description_text = Description_text.replace(Camera_quality,"").strip()

        # print("__________________",Camera_quality)


        mobile_details.append({
            "Name": Name.text,
            "Description": Description_text,
            "Camera_quality":Camera_quality,
            "Price": price.text,
            "Rating": Rating.text,
            "Image_url": Image_url.get_attribute("src") if Image_url.get_attribute("src") else "No Image",

        })

    # print(f"Mobile details for page {page_num}:")
    print(mobile_details)
    if mobile_details not in all_mobile_details:
        all_mobile_details.extend(mobile_details)

    next_page = driver.find_element(By.CLASS_NAME, '_1LKTO3')
    if next_page.is_enabled():
        next_page.click()
        time.sleep(5)     
    else:
        break 

print(all_mobile_details)
driver.quit()

csv_file = "mobile_details.csv"
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Description", "Camera_quality","Price", "Rating","Image_url"])
    writer.writeheader()
    writer.writerows(all_mobile_details)

print(f"Mobile details have been saved to {csv_file}.")