import requests

SLOT_ENDPOINT = "https://www.allforyou.sg/Common/pinCodeSearch"
zipCode = 528523 # enter zip code
headers = {
  "User-Agent": "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);"
}
data = {
  "code": zipCode,
  "pinStatus": 1
}
getSlot = requests.post(SLOT_ENDPOINT, data=data, headers=headers)
available = True if getSlot.json()["result"] != "No more timeslots." else False

print("Delivery to {}: {}".format(zipCode, available))
