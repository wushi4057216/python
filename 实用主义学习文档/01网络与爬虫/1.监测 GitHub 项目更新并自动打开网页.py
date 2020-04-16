# api https://api.github.com/repos/channelcat/sanic
# web_page https://github.com/channelcat/sanic

import requests
import webbrowser
import time

api = 'https://api.github.com/repos/channelcat/sanic'
web_page = "https://github.com/channelcat/sanic"
last_update = '2019-01-30T20:40:51Z'
all_info = requests.get(api).json()
print(all_info)
cur_update = all_info['updated_at']
print(cur_update)

while True:
    if not last_update:
        last_update = cur_update

    if last_update < cur_update:
        webbrowser.open(web_page)
        time.sleep(600)

