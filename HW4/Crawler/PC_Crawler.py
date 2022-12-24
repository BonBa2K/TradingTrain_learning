import requests
import datetime
import pymongo

# initialize header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

# parse url & data get function
def parse_url(keyword, page):
    url = f"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={keyword}&page={str(page)}&sort=sale/dc"
    return url


def search_prods(search_word, search_amount):
    output = []
    loop_round = 1
    while True:
        url = parse_url(keyword=search_word, page=loop_round)
        temp = requests.get(url)
        products = temp.json()
        for prod in products["prods"]:
            now = datetime.datetime.now()
            created_at = now.strftime("%Y-%m-%dT%H:%M:%SZ")
            output.append(
                {
                    "prod_name": prod["name"],
                    "prod_price": prod["price"],
                    "channel": "PChome",
                    "created_at": created_at,
                }
            )
        loop_round += 1
        if len(output) >= search_amount:
            loop_round = 1
            break
    return output


result = search_prods(search_word="電視", search_amount=300)

# --------------------存檔區-------------------------
# Writing to MongoDB
target_db = pymongo.MongoClient("mongodb://localhost:27017/")
collection = target_db["demoDB"]["prods"]

z = collection.delete_many({})
x = collection.insert_many(result)

print(z.deleted_count, "個舊檔案已刪除")
