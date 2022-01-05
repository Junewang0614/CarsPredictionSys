# 1. 向数据库批量导入数据
import os
import pandas as pd
import requests
from django.http import HttpResponse
from usermanage.models import Factory
from bs4 import BeautifulSoup

def createpath(filename):
    filepath = './static/loacaldata'
    datafile = os.path.join(filepath, filename)
    return datafile

def importfacs(request):
    # 访问本地静态
    # F:\ydddd\pyprojects\CarsPredictionSys\usermanage
    filename = 'factories.csv'
    datafile = createpath(filename)
    fdata = pd.read_csv(datafile,encoding = "utf-8")
    fdata = fdata[['name','logo']]

    fdata = tuple(zip(fdata['name'],fdata['logo']))
    names = []
    for name,logo in fdata:
        if name not in names:
            Factory.objects.create(fname=name,flogo=logo)
        names.append(name)

    return HttpResponse("factories info imported successfully")

# 2. 从本地读取新闻内容
def readnews():
    filename = "车辆新闻爬取.csv"
    datafile = createpath(filename)
    dataset = pd.read_csv(datafile, encoding="utf-8")
    dataset = tuple(zip(dataset['title'], dataset['link']))
    return dataset

# 3. 网页爬取新闻内容
def get_news_list(url, num):
    r = requests.get(url)
    bfs = BeautifulSoup(r.text)

    result = bfs.select(".opinion>.box-b")[0]
    ress = result.contents[1].select("li")
    newslist = []
    ourl = url.replace("list_1.html", "")

    for i in range(num):
        nurl = ourl + ress[i].a["href"]
        title = ress[i].find("span", "cont").text
        newslist.append((title, nurl))

    return newslist

def get_all_news():
    urls = ["http://www.caam.org.cn/chn/4/cate_30/list_1.html", "http://www.caam.org.cn/chn/8/cate_82/list_1.html",
            "http://www.caam.org.cn/chn/8/cate_83/list_1.html", "http://www.caam.org.cn/chn/8/cate_86/list_1.html"]
    all_news = []

    for i, url in enumerate(urls):
        # 第一个爬4个
        if (i == 0):
            all_news.extend(get_news_list(url, 4))
        else:
            all_news.extend(get_news_list(url, 2))
    return all_news