'''python
from django.shortcuts import render
from .models import TableModel
from django.db.models import F

def chart_view(request):
    # 获取URL参数
    selected_deal = request.GET.get('deal', '')
    selected_lp = request.GET.get('lp', '')
    # 获取Deal和LP的所有唯一值用于下拉菜单
    deals = TableModel.objects.values_list('Deal', flat=True).distinct()
    lps = TableModel.objects.values_list('LP', flat=True).distinct()
    # 根据选择筛选数据
    queryset = TableModel.objects.all()
    if selected_deal:
        queryset = queryset.filter(Deal=selected_deal)
    if selected_lp:
        queryset = queryset.filter(LP=selected_lp)
    # 准备Echarts所需的数据格式
    data = list(queryset.annotate(date=F('Date'), data1=F('Data1'), data2=F('Data2'), data3=F('Data3'), data4=F('Data4'))
                 .values('date', 'data1', 'data2', 'data3', 'data4').order_by('date'))
    context = {
        'deals': deals,
        'lps': lps,
        'selected_deal': selected_deal,
        'selected_lp': selected_lp,
        'data': data,
    }
    return render(request, 'your_template.html', context)

'''
