import requests



r = requests.get('https://rule34.xxx/index.php?page=post&s=list&tags={}'.format('Ahri222'))
b = r.json()
print(r.status_code)










