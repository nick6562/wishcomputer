import psycopg2
from psycopg2 import Error


CategoryName = input("請輸入您的類別名稱： \n")
# Description = input("請輸入您的類別規格：")

connection = None
CategoryId = None

try:
    # 連線資料庫
    connection = psycopg2.connect(user="admin", password="P@ss!976", host="192.168.100.5", port="5432", database="wishcomputer")
    insert_query = """ INSERT INTO Category (CategoryId, CategoryName) VALUES (%s, %s)"""
    # query = "SELECT * FROM category;"
    # 建立一箇 Cursor 物件, 並且使用該物件
    cursor = connection.cursor()
    print("PostgreSQL server 相關資訊")
    # 取得連線資訊
    print(connection.get_dsn_parameters(), "\n")
    record_to_insert = [(7, CategoryName),]
    for i in record_to_insert:
        cursor.execute(insert_query, i)
        
        connection.commit()
        count = cursor.rowcount
    print(count, "Record inserted successfully into Category table")
    cursor.execute(query)
    category_records = cursor.fetchall()
    for row in category_records:
        print("Category ID =", row[0])
        print("Category Name =", row[1])
        print("Description =", row[2], "\n")


except (Exception, Error) as error:
    print("當連線到 PostgreSQL 資料庫時, 發生錯誤", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL 連線已經中斷")


def insertQuery():
    return

def deleteQuery():
    return

def updateQuery():
    return