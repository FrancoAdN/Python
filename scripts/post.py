# https://twitter.com/sessions

# session[username_or_email]: nehudinapoli
# session[password]: nehu753159852456
import requests
# url = 'https://twitter.com/sessions'
# r = requests.post(url, allow_redirects=True, data={
#     'session%5Busername_or_email%5D': 'nehudinapoli',
#     'session%5Bpassword%5D': 'nehu75852456'
# })

# print r.url
url = 'https://elizalde.alexia.com.ar/ACWeb/WS_Data/WSLogOn.asmx/Validar'
send = {"token":"fe51e861-1d39-4207-af20-bceda1620e29","nickname":"S.cano","password":"42904558"}

r = requests.post(url, allow_redirects=True, data = send)
print r