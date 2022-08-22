from urllib import request
from urllib import parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

name = input('请输入您要浏览的贴吧名称：')
name = parse.quote(name)

for page in range(5):
    url = f'https://tieba.baidu.com/f?kw={name}=utf-8&pn={page*50}'
    rq = request.Request(url=url, headers=headers)
    res = request.urlopen(rq)
    content = res.read().decode('utf-8')
    file_path = f'fdupage{page}.html'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('下载完成！')
