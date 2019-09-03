from requests import Request, Session
from bs4 import BeautifulSoup
# # nickname: "S.cano"
# # password: "42904558"
# # token: "36557d4e-a8a3-40b9-a42b-432c567309ae"

login_data = {
    'nickname': 'S.cano',
    'password': '42904558'
}
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
# # }
# # with requests.Session() as s: 
# #     url = 'https://elizalde.alexia.com.ar/ACWeb/WS_Data/WSLogOn.asmx/Validar'
# #     r = s.get(url, headers=headers)

# #     r = s.post(url, data=login_data, allow_redirects=True, headers=headers)
# #     print r.text
url = 'https://elizalde.alexia.com.ar/ACWeb/LogOn.aspx'
s = Session()
r = s.get(url)

soup = BeautifulSoup(r.content,features="html.parser")
login_data['token']= soup.find('input', attrs={'name':'Token'})['value']
print login_data
req = Request('POST', url, data=login_data)
prepped = req.prepare()
print req.status_code