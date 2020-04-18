import requests

SLOT_ENDPOINT = "https://coldstorage.com.sg/checkout/cart/checkdelivery"
zipCode = 528523 # enter zip code
headers = {
  "User-Agent": "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);"
}
getSlot = requests.post(SLOT_ENDPOINT, data={"postal_code":zipCode}, headers=headers)
available = True if len(getSlot.json()["earliest"]) > 0 else False

print("Delivery to {}: {}".format(zipCode, available))
