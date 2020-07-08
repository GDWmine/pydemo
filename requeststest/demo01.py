import requests

ip = 'http://192.144.148.91:2333'


index_url = '{}/get_title_img'.format(ip)
res = requests.get(index_url)
print(res.text)