# https://github.com/P3TERX/GeoLite.mmdb/releases

import maxminddb
import requests


# get the latest version
url = "https://api.github.com/repos/P3TERX/GeoLite.mmdb/releases/latest"

res = requests.get(url)
res.raise_for_status()
assets = res.json()["assets"]

download_urls = []

for i in assets:
    if i["name"].endswith(".mmdb"):
        download_urls.append(i["browser_download_url"])

# download the latest version
for i in download_urls:
    res = requests.get(i)
    res.raise_for_status()
    file_path = f"layer/{i.split('/')[-1]}"
    with open(file_path, "wb") as f:
        f.write(res.content)

# test mmdb
