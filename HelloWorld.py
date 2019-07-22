import requests
r = requests.get('https://www.baidu.com/s?wd=python')
print(r.url)
print('helloworld')