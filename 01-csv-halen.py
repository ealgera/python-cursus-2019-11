import requests

# Copy 'link address van: https://insights.stackoverflow.com/survey
# Via F12 nagaan welke url wordt gebruikt
url = r"https://drive.google.com/uc?authuser=0&id=1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV&export=download"


r = requests.get(url)
print(r.status_code)

open('data.zip', 'wb').write(r.content)
