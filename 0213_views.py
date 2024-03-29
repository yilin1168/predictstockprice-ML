from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import get_object_or_404
from .models import TableModel
from django.http import JsonResponse
from django.db.models import Sum
from django.core.serializers.json import DjangoJSONEncoder
import json

def display_view(request):
    data = TableModel.objects.all()
    return render(request, 'dash/table.html', locals() )



#QuerySet-Json-Json in JS



### all below are testing:

from django.db.models import Sum, F, ExpressionWrapper, DecimalField

def agg_view(request):

    # 使用ExpressionWrapper来确保结果有两位小数
    annotations = {
        f'sum_data{i}': ExpressionWrapper(
            Sum(f'data{i}'),
            output_field=DecimalField(max_digits=10, decimal_places=2)
        ) for i in range(1, 5)
        
    }
    
    from some_module import Sum  # 假设 Sum 是从某个模块导入的

# 对于符合 "data1", "data2" 这样命名规则的变量
annotations_data = {f'sum_data{i}': Sum(f'data{i}') for i in range(1, 3)}

# 如果 "price", "t_1", "t_2" 需要不同的处理方式，可以分别创建字典
annotations_price = {'sum_price': Sum('price')}
annotations_t = {f'sum_t_{i}': Sum(f't_{i}') for i in range(1, 3)}

# 合并这些字典
annotations = {}
annotations.update(annotations_data)
annotations.update(annotations_price)
annotations.update(annotations_t)

    aggregate_by = request.GET.get('aggregate_by', 'Date')
    if aggregate_by == 'LP':
        data = TableModel.objects.values('Date', 'LP').annotate(**annotations).order_by('Date', 'LP')
    elif aggregate_by == 'Deal':
        data = TableModel.objects.values('Date', 'Deal').annotate(**annotations).order_by('Date', 'Deal')
    else:  # 默认按Date聚合
        data = TableModel.objects.values('Date').annotate(**annotations).order_by('Date')

    # 将日期转换为字符串（如果需要）并准备数据发送到模板
    data_list = list(data)
    for item in data_list:
        if 'Date' in item:
            item['Date'] = item['Date'].strftime('%Y-%m-%d')  # 调整日期格式

    return render(request, 'dash/table_agg_line.html', {'data': data_list, 'aggregate_by': aggregate_by})





# can run
def agg_view(request):

    annotations = {f'sum_data{i}': Sum(f'data{i}') for i in range(1, 5)}

    aggregate_by = request.GET.get('aggregate_by', 'Date')
    if aggregate_by == 'LP':
        data = TableModel.objects.values('Date', 'LP').annotate(**annotations).order_by('Date', 'LP')
    elif aggregate_by == 'Deal':
        data = TableModel.objects.values('Date', 'Deal').annotate(**annotations).order_by('Date', 'Deal')
    else:  # 默认按Date聚合
        data = TableModel.objects.values('Date').annotate(**annotations).order_by('Date')

    # 将日期转换为字符串（如果需要）并准备数据发送到模板
    data_list = list(data)
    for item in data_list:
        if 'Date' in item:
            item['Date'] = item['Date'].strftime('%Y-%m-%d')  # 调整日期格式

    return render(request, 'dash/table_agg_line.html', {'data': data_list, 'aggregate_by': aggregate_by})




# match table_agg_line0.html success ok!
# def agg_view(request):
#     aggregate_by = request.GET.get('aggregate_by', 'Date')

#     # 假设我们按Date聚合
#     if aggregate_by == 'Date':
#         data = TableModel.objects.values('Date').annotate(
#             sum_data1=Sum('data1'),
#             sum_data2=Sum('data2'),
#             sum_data3=Sum('data3'),
#             sum_data4=Sum('data4'),
#         )
#     elif aggregate_by == 'LP':
#         data =TableModel.objects.values('Date', 'LP').annotate(
#             sum_data1=Sum('data1'),
#             sum_data2=Sum('data2'),
#             sum_data3=Sum('data3'),
#             sum_data4=Sum('data4'),
#         )
#     else:  # Deal
#         data = TableModel.objects.values('Date', 'Deal').annotate(
#             sum_data1=Sum('data1'),
#             sum_data2=Sum('data2'),
#             sum_data3=Sum('data3'),
#             sum_data4=Sum('data4'),
#         )
#     formatted_data = []
#     for item in data:
#         formatted_item = {
#             'Date': item['Date'].strftime('%Y-%m-%d'),  # 将日期转换为字符串
#             'sum_data1': item['sum_data1'],
#             'sum_data2': item['sum_data2'],
#             'sum_data3': item['sum_data3'],
#             'sum_data4': item['sum_data4'],
#         }
#         formatted_data.append(formatted_item)

#     # 使用DjangoJSONEncoder确保其他数据类型也被正确序列化
#     json_data = json.dumps(formatted_data, cls=DjangoJSONEncoder)

#     return render(request, 'dash/table_agg_line.html', {'data': json_data, 'aggregate_by': aggregate_by})
