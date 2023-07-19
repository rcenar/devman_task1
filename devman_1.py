import requests

url_template = "https://wttr.in/{}?nTqu&lang=ru"
locations = ["Лондон", "Шереметьево", "Череповец"]
for location in locations:
    r = requests.get(f"https://wttr.in/{location}?MTnq&lang=ru")
    print(r.text)
