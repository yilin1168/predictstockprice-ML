```python
# urls.py
from django.urls import path
from assets import views
app_name = 'assets'
urlpatterns = [
    path('report/', views.report, name='report'),
    path('report_spark/', views.report_spark, name='report_spark'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('detail/<int:asset_id>/', views.detail, name='detail'),
    path('display', views.display_data, name='display_data'),
    path('', views.dashboard),
]

#assets_handler.py
import json
from assets import models

class NewSpark(object):
    def __init__(self, request, data):
        self.request = request
        self.data = data

    def add_to_table(self):
        defaults = {
            'Deal': self.data.get('Deal'),
            'LP': self.data.get('LP'),
            'Date': self.data.get('Date'),
            'data1': self.data.get('data1'),
            'data2': self.data.get('data2'),
            'data3': self.data.get('data3'),
            'data4': self.data.get('data3'),
        }
        models.YourModel.objects.update_or_create(Deal=self.data['Deal'], defaults=defaults)
        return 'added to table'

        
# views.py
@csrf_exempt
def report_spark(request):
    if request.method == 'POST':
        spark_data = request.POST.get('spark')
        database = request.POST.get('database')
        data = json.loads(spark_data)

        if not data:
            return HttpResponse('没有数据！')
        if not issubclass(dict, type(data)):
            return HttpResponse('数据必须为字典格式！')

        print(data)
        print(type(data))
        Deal = data.get('Deal', None)
        print(Deal)

        if Deal:
            obj = asset_handler.NewSpark(request, data)
            response = obj.add_to_table()
            return HttpResponse(response)
            # asset_obj = models.Asset.objects.filter(Deal=Deal)  
            # if asset_obj:
            #     update_asset = asset_handler.UpdateAsset(request, asset_obj[0], data)
            #     return HttpResponse('资产数据已经更新。')
            # else:
            #     obj = asset_handler.NewAsset(request, data)
            #     response = obj.add_to_new_assets_zone()
            #     return HttpResponse(response)
        else:
            return HttpResponse('没有Deal number，请检查数据内容！')

    return HttpResponse('200 ok')

    
# Client/conf/settings.py
import os

# 远端接收数据的服务器
Params = {
   # "server": "192.168.0.100",
    "server": "192.168.50.82",
    "port": 8000,
    'url': '/assets/report/',
    'url_spark':'/assets/report_spark/',
    'request_timeout': 30,
}
PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')

# Client/core/info_collection.py
import sys
import platform
import pandas as pd
import json

class NewData(object):
    @staticmethod
    def build_report_data():
        # 留下一个接口，方便以后增加功能或者过滤数据
        df = pd.read_excel("/Users/elainegui/Desktop/send01.xlsx")
        df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
        json_list = json.loads(df.to_json(orient='records'))

        return json_list


# Client/core/handler.py
    @staticmethod
    def report_spark():

        spark_data = info_collection.NewData.build_report_data()
        for spark_data1 in spark_data:
            data = {'spark': json.dumps(spark_data1), 'database': 'A'}
            url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url_spark'])
            print('正在将数据发送至： [%s]  ......' % url)
            try:
                data_encode = urllib.parse.urlencode(data).encode()
                response = urllib.request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
                print("\033[31;1m发送完毕！\033[0m ")
                message = response.read().decode()
                print("返回结果：%s" % message)
            except Exception as e:
                message = '发送失败' + "   错误原因：  {}".format(e)
                print("\033[31;1m发送失败，错误原因： %s\033[0m" % e)
            # 记录发送日志
            with open(settings.PATH, 'ab') as f:  # 以byte的方式写入，防止出现编码错误
                log = '发送时间：%s \t 服务器地址：%s \t 返回结果：%s \n' % (time.strftime('%Y-%m-%d %H:%M:%S'), url, message)
                f.write(log.encode())
                print("日志记录成功！")
```
