import requests

STORE_ENDPOINT = \
    "https://website-api.omni.fairprice.com.sg/api/serviceable-area?city=Singapore&pincode={}"
SLOT_ENDPOINT = \
    "https://website-api.omni.fairprice.com.sg/api/slot-availability?address[pincode]={}&storeId={}"
zipCode = 528523 # enter zip code
headers = {
  "User-Agent": "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);"
}
getStoreId = requests.get(STORE_ENDPOINT.format(zipCode), headers=headers)
storeId = getStoreId.json()["data"]["store"]["id"]
getSlot = requests.get(SLOT_ENDPOINT.format(zipCode, storeId), headers=headers)
available = getSlot.json()["data"]["available"]

print("Delivery to {}: {}".format(zipCode, available))
