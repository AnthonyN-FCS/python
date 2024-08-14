import requests
import pprint

url = "https://api.hypixel.net/skyblock/bazaar"

response = requests.get(url)
data = response.json()

if not data["success"]:
    print("Failure.")

    
filter_products = {}
for key, value in data["products"].items():
    if "ENCHANTMENT" not in key:
        filter_products[key] = value
    continue

def get_data(key):
    key = key.upper()
    pprint.pprint(filter_products[key])

    buy_summary = filter_products[key]["buy_summary"]
    sell_summary = filter_products[key]["sell_summary"]
    quick_status = filter_products[key]["quick_status"]
    product_id = filter_products[key]["product_id"]

    '''
    buyMovingWeek = quick_status["buyMovingWeek"]
    buyOrders = quick_status["buyOrders"]
    avgBuyPrice = quick_status["buyPrice"]
    buyVolume = quick_status["buyVolume"]

    sellMovingWeek = quick_status["sellMovingWeek"]
    sellOrders = quick_status["sellOrders"]
    avgSellPrice = quick_status["sellPrice"]
    sellVolume = quick_status["sellVolume"]
    '''
    def quick_data():
        s = ""
        for key, value in quick_status.items():
            s += f"     {key.upper()}: {value}\n"
        return s
    def orders(sell):
        s = ""
        for order in filter_products[key][sell+"_summary"]:
            s += f"      Price: {order['pricePerUnit']}   Amount: {order['amount']}   Orders: {order['orders']}\n"
        return s
    
    print(f"""PRODUCT DATA FOR: {product_id}
    Quick Data:
{quick_data()}
    Sell Orders:
{orders("sell")}
    Buy Orders:
{orders("buy")}

    
    """)

    return 

get_data("rough_opal_gem")