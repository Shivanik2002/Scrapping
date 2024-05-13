import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy,4io')

Names = driver.find_elements(By.CSS_SELECTOR,'._4rR01T')
# for name in Names:
#     print("Product_name:",name.text)

print("____________________________________________________________")

Descriptions = driver.find_elements(By.CSS_SELECTOR,'._1xgFaf')
# for Description in Descriptions:
#     print("Description;",Description.text)    

print("____________________________________________________________")

prices = driver.find_elements(By.CSS_SELECTOR,'._1_WHN1')
# for price in prices:
#     print("Price:",price.text)

print("____________________________________________________________")

Ratings = driver.find_elements(By.CLASS_NAME,'_3LWZlK')
# for Rating in Ratings:
#     print("Rating:",Rating.text)


print("____________________________________________________________")

mobile_details = []
for Name,Description, price ,Rating in zip(Names,Descriptions,prices,Ratings):
    mobile_details.append({"Name" : Name.text , "Description" : Description.text , "Price" : price.text,"Rating" : Rating.text})

print(mobile_details)

# Name= driver.find_element(By.CSS_SELECTOR,'._4rR01T')
# Name = Name.text
# print("Name:",Name)
# print("____________________________________________________________")

# Description = driver.find_element(By.CSS_SELECTOR,'._1xgFaf')
# Description = Description.text
# print("Description:",Description)
# print("____________________________________________________________")

# Price = driver.find_element(By.CLASS_NAME,'_1_WHN1')
# Price = Price.text
# print("Price:",Price)
# print("____________________________________________________________")

driver.quit()

csv_file = 'mobile.details.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Description", "Price", "Rating"])
    writer.writeheader()
    writer.writerows(mobile_details)
    
print(f"Mobile details have been saved to {csv_file}.")
