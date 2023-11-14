from datetime import datetime

import requests

# response = requests.post("http://127.0.0.1:5000/owners",
#                          json={"email": "adsxcz",
#                                "password": "123"
#                                },
#                          )
#
# print(response.status_code)
# print(type(response))
# print(response.text)

#
# response = requests.post("http://127.0.0.1:5000/ads",
#                          json={"title": "adssaa",
#                                "description": "qweqweas",
#                                "date_of_creation": (datetime.now()).isoformat(),
#                                "owner_id": "1",
#                                },
#                          )
#
# print(response.status_code)
# print(response.text)

response = requests.get(
    "http://127.0.0.1:5000/owners/1",
)
print(response.status_code)
print(response.text)

# response = requests.get(
#     "http://127.0.0.1:5000/ads/2",
# )
# print(response.status_code)
# print(response.text)

# response = requests.delete(
#     "http://127.0.0.1:5000/ads/2",
# )
# print(response.status_code)
# print(response.text)

# response = requests.get(
#     "http://127.0.0.1:5000/ads/2",
# )
# print(response.status_code)
# print(response.text)
#
# response = requests.patch("http://127.0.0.1:5000/ads/3",
#                           json={"title": "adsqweqwe"}
#                           )
#
# print(response.status_code)
# print(response.text)
#
# response = requests.get(
#     "http://127.0.0.1:5000/ads/2",
# )
# print(response.status_code)
# print(response.text)
