from urllib import request
from urllib import parse
import json

#https://movie.douban.com/top250?start=0&filter=
#https://movie.douban.com/top250?start=50&filter=
base_url = 'https://movie.douban.com/top250?start={}&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
for p in range(0,10):
    url = base_url.format(p*25)
    rq = request.Request(url=url, headers=headers)
    res = request.urlopen(rq)
    content = res.read().decode('utf-8')
    json_obj = json.loads(content)
    film_list = json_obj['data']
    for film_dict in film_list:
        title = film_dict['title']
        rate = film_dict['rate']
        print(f'电影名：{title}， 评分：{rate}')
