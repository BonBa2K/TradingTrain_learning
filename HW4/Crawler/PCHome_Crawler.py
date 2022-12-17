import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import pymongo

search_amount=300

# -----------------------分析區-----------------------------
driver = webdriver.Chrome()
driver.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=電視")  # 更改網址以前往不同網頁
time.sleep(2)
# d_Example = {'prod_name': 3, 'prod_price': 3,'channel': 3, 'created_at': 3, 'modified_at': 3, }
output = []

# scroll to bottom
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    prod_elements = driver.find_elements(By.CLASS_NAME, 'col3f')
    if len(prod_elements) >= search_amount:
        break

for target_prod in prod_elements:
    # 取得名字標籤
    prod_name = (target_prod.find_element(
        By.TAG_NAME, 'img')).get_attribute('title')
    # 取得價格標籤
    prod_price = (target_prod.find_element(
        By.CLASS_NAME, 'value')).get_attribute('innerText')
    # 取得建立日期
    now = datetime.datetime.now()
    created_at = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    # 輸出
    output.append({
        'prod_name': prod_name, 'prod_price': int(prod_price),
        'channel': 'pchome', 'created_at': created_at,
    })

time.sleep(2)


driver.close()  # 關閉瀏覽器視窗


# --------------------存檔區-------------------------
path = 'D:\BomBa2K備檔\上課檔案\日-鎚圈TradingTrain\TradingTrain_learning\HW4\Title_Output.txt'
f = open(path, 'w', encoding="utf-8")
f.close()

# Serializing json
json_object = json.dumps(output, indent=4, ensure_ascii=False)
# Writing to sample.json
with open("D:\BomBa2K備檔\上課檔案\日-鎚圈TradingTrain\TradingTrain_learning\HW4\Crawler\Output.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_object)

path = 'D:\BomBa2K備檔\上課檔案\日-鎚圈TradingTrain\TradingTrain_learning\HW4\Crawler\JSON_Output.txt'
f = open(path, 'w', encoding="utf-8")
f.write(
    (str)(output))
f.close()

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

data = myclient['demoDB']["prods"]


z = data.delete_many({})
x = data.insert_many(output)

# print(x.inserted_ids)
print(z.deleted_count, "個舊檔案已刪除")
