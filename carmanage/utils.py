import os
import pandas as pd
from django.http import HttpResponse
from usermanage.models import Factory
from carmanage.models import Series,Sale
import datetime as dt
from django.conf import settings

def createpath(filename):
    filepath = './static/loacaldata'
    datafile = os.path.join(filepath, filename)
    return datafile

# 打包函数
def zip_data(file_name, cols):
    datas = pd.read_csv(file_name, encoding='utf-8', engine='python')
    datas = datas[cols]
    result = []
    col_len = len(cols)
    row_len = len(datas)
    for i in range(row_len):
        df = datas.iloc[i]
        df = df.values.tolist()
        result.append(df)
    return result
# 1. 导入车型信息
#  全是上汽大众
#  01.06导入比亚迪

def importcars(request):
    # 设置访问路径
    filename = os.path.join('比亚迪','比亚迪所有车型及类别.csv')
    datafile = createpath(filename)
    try:
        data = pd.read_csv(datafile,encoding = 'utf-8')
    except Exception as e:
        print("===============ERROR====================")
        print(e)
        return HttpResponse('---readfile si error---')
    # 数据为data
    try:
        data = tuple(zip(data['name'],data['type'],data['para_link']))
    except Exception as e:
        print("===============ERROR====================")
        print(e)
        return HttpResponse('---CSV si error---')
    # 外键也ok
    try:
        factory = Factory.objects.filter(fname='比亚迪')[0]
    except Exception as e: #万一没有厂商
        print("===============ERROR====================")
        print(e)
        return HttpResponse('---厂商 si error---')
    names = []
    for name,type,info in data:
        if name not in names:
            Series.objects.create(sname=name,stype=type,sinfo=info,factory=factory)
            names.append(name)

    return HttpResponse('import series is ok')

# 2.导入销量

def import_sales_data(path):
    try:
        df = pd.read_csv(path + '\\' + '上汽大众所有车型及类别.csv', encoding='utf-8', engine='python', names=['1','2','3','4','5','6','7','8'])
    except Exception as e:
        print("===============ERROR====================")
        print(e)
        return HttpResponse('---readfile si error---')
    data = df.values
    size = len(data)
    list = []
    # 获取数据
    for i in range(size):
        array = []
        name = data[i][1]
        train_path = path + "\\" + "上汽大众所有车型月销量" + "\\" + name + '.csv'
        try:
            df = pd.read_csv(train_path, encoding='utf-8', engine='python')
        except Exception as e:
            print("===============ERROR====================")
            print(e)
            return HttpResponse('---readfile si error---')
        df = df[['月份', '月销量']]
        num = len(df)

        train_data = df.values.tolist()
        for i in range(num):
            if train_data[i][1] == '--':
                train_data[i][1] = 0
        list.append([name, train_data])
    return list

def importsales(request):
    filepath = './static/loacaldata/上汽大众'
    # Sale.objects.all().delete()
    dataset = import_sales_data(filepath)
    # print(dataset)
    for car,sales in dataset:
        #确定car
        series = Series.objects.filter(sname=car)[0]
        # 导入sales
        for sale in sales:
            # str = '2020-03'
            # d1 = datetime.datetime.strtime(str,'%Y-%m')
            # d1 = d1.date() # 转为date类型
            date = dt.datetime.strptime(sale[0],'%Y-%m')
            date = date.date() # 日期搞定
            number = sale[1] # 销量

            Sale.objects.create(date=date,series=series,number=number)

    return HttpResponse('import sales is ok')

#3. 导入指定车厂的图片
def importcimages(request,factory):
    # 文件路径
    filename = os.path.join(factory,'IMAGE.csv')
    datafile = createpath(filename)
    datas = zip_data(datafile,['name','link'])
    # print(datas)
    for name,link in datas:
        result = Series.objects.filter(sname=name)
        if not result.exists():
            print("%s不存在数据库中"%name)
        else:
            car1 = result[0]
            car1.simage = link
            car1.save()
    return HttpResponse('import imgs is ok')