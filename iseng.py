import requests

try:
    print('hello world')
    r = requests.get('https://g oogle.com')
    print (r.status_code)
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('ada kesalahan di :',e)
