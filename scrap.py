from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.apple.com/in/shop/buy-iphone/iphone-15/6.1%22-display-128gb-blue?afid=p238%7Cskw5a74om-dc_mtid_187079nc38483_pcrid_674224198452_pgrid_153710578779_pntwk_g_pchan_online_pexid__&cid=aos-IN-kwgo-pla-iphone--slid---product-MTP43HN%2FA-IN')

name = driver.find_element(By.CLASS_NAME,'fwl')
# name = name.text
# print(name)

price = driver.find_elements(By.CLASS_NAME,'rc-price')
# for i in price:
#     price = i.text
#     print(price)
#     print("---------------------")

deatails = price[1].text
Details = deatails.split('\n')
mrp_price = Details[4].split('or')[1]

data = {"Name" : name.text , "Price" : mrp_price,"details": price}
print(data)

driver.quit()

