import requests
import datetime
import pymongo
import logging

# initialization
logging.basicConfig(filename="crawler_report.log", encoding="utf-8", level=logging.DEBUG)
target_db = pymongo.MongoClient("mongodb://localhost:27017/")
collection = target_db["demoDB"]["prods"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

# data get function
def search_pc_prods(search_word, search_amount):
    loop_round = 1
    inserted_amount= 0
    while True:
        output=[]
        url = f"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={search_word}&page={str(loop_round)}&sort=sale/dc"
        products = requests.get(url).json()
        for prod in products["prods"]:
            try:
                # check if pords enough
                if inserted_amount >= search_amount:
                    logging.info(f'append success')
                    collection.insert_many(output)
                    return 0

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
                inserted_amount+=1
            except:
                logging.error(f'append failed ,inserted_amount == {str(inserted_amount)}')
                break

        #如果資料量不足就跳出去
        if products["totalRows"] < search_amount:
            collection.insert_many(output)
            logging.info(f'關鍵字: {search_word} 資料量不足{search_amount}')
            break

        collection.insert_many(output)
        logging.info(f'page {loop_round}, insert success')
        loop_round+=1

if __name__=='__main__':
    collection.delete_many({})
    # input_word="鐵獸式強襲機動兵裝改"
    input_word="電視"
    input_num=302
    
    logging.info(f'==== 查詢關鍵字:{input_word}, 查詢數量:{input_num} ====')
    search_pc_prods(search_word=input_word, search_amount=input_num)
    logging.info(f'==== 資料爬取完成 ====')
