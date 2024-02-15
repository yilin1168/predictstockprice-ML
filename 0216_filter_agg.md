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

'''html
{% extends 'base.html' %}
{% load static %}
{% block title %}Display{% endblock %}

{% block content %}
<section class="content">
    <div class="box">
        <div class="box-header">
            <h3 class="box-title">Filter Data</h3>
            <form action="" method="get">
                <select name="deal" onchange="this.form.submit()">
                    <option value="">Select Deal</option>
                    {% for deal in deals %}
                    <option value="{{ deal }}" {% if selected_deal == deal %}selected{% endif %}>{{ deal }}</option>
                    {% endfor %}
                </select>
                <select name="lp" onchange="this.form.submit()">
                    <option value="">Select LP</option>
                    {% for lp in lps %}
                    <option value="{{ lp }}" {% if selected_lp == lp %}selected{% endif %}>{{ lp }}</option>
                    {% endfor %}
                </select>
            </form>
        </div>
        <div class="box-body">
            <div id="main" style="height:400px;"></div>
        </div>
    </div>
</section>
{% endblock %}

{% block script %}
<script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
<script type="text/javascript">
    var myChart = echarts.init(document.getElementById('main'));
    var rawData = {{ data|safe }};
    
    var option = {
        tooltip: { trigger: 'axis' },
        xAxis: {
            type: 'category',
            data: rawData.map(function (item) { return item.date; })
        },
        yAxis: { type: 'value' },
        series: [
            { name: 'Data1', type: 'line', data: rawData.map(function (item) { return item.data1; }) },
            { name: 'Data2', type: 'line', data: rawData.map(function (item) { return item.data2; }) },
            { name: 'Data3', type: 'line', data: rawData.map(function (item) { return item.data3; }) },
            { name: 'Data4', type: 'line', data: rawData.map(function (item) { return item.data4; }) }
        ],
        legend: {
            data: ['Data1', 'Data2', 'Data3', 'Data4']
        },
        toolbox: {
            show: true,
            feature: {
                saveAsImage: { show: true }
            }
        }
    };
    
    myChart.setOption(option);
</script>
{% endblock %}
'''

