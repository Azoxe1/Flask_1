import requests

#
# response = requests.post("http://127.0.0.1:5000/ads",
#                          json={"title": "ads",
#                                "description": "qweqwe",
#                                # 'date_of_creation': '12.12.2022',
#                                "owner": "asd"
#                                },
#                          )
#
# print(response.status_code)
# print(response.text)

response = requests.get(
    "http://127.0.0.1:5000/ads/1",
)
print(response.status_code)
print(response.text)
