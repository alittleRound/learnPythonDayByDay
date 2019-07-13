import requests
url = 'https://api.douban.com/v2/movie/top250' #豆瓣关闭了api，无法运行咯
r = requests.get(url, params={'start': 1, 'count': 25})
print(r)
res = r.json()
for movie in res['subjects']:
    print(movie['title'])