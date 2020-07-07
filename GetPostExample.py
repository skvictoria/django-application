import requests as req

URL= 'http://httpbin.org/get'
resp = req.get(URL)
print(resp.status_code)
print(resp.text)
print(resp.url)

payload = {'key1':'value1', 'key2':'value2'}
resp = req.get(URL, params = payload)
print(resp.url)
print(resp.text)

resp = req.get('https://api.github.com/events')
print(resp.text)

datas = resp.json()[0]

for key in datas.keys():
    print('key:{}, values:{}\n'.format(key, datas[key]))
    
datas['id']

URL='http://httpbin.org/post'
data= {'key':'value', 'key_x':'value_x'}
resp = req.post(URL, data = data)

print(resp.status_code)
print(resp.text)
print(resp.url)

datas = resp.json()
print(type(datas))
for key in datas.keys():
    print("key:{}, values:{}\n".format(key, datas[key]))
