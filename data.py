import csv
import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By

db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Kash!1998",
    database="Scrap_db"
)
cursor = db_connection.cursor()

for mobile_detail in all_mobile_details:
    sql = "INSERT INTO your_table_name (Name, Description, Camera_quality, Price, Rating, Image_url) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (mobile_detail["Name"], mobile_detail["Description"], mobile_detail["Camera_quality"], mobile_detail["Price"], mobile_detail["Rating"], mobile_detail["Image_url"])
    cursor.execute(sql, val)

db_connection.commit()
cursor.close()
db_connection.close()

print(f"Mobile details have been saved to MySQL database.")