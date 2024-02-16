```python
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

```

```html
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

var rawData = {{ data|safe }};

// 将数据按Data1的值分组
var groupedData = {};
rawData.forEach(function(item) {
    if (!groupedData[item.Data1]) {
        groupedData[item.Data1] = [];
    }
    groupedData[item.Data1].push({date: item.Date, value: item.Data2});
});

// 创建Echarts系列数组
var series = Object.keys(groupedData).map(function(key) {
    // 将每组数据的Date提取出来作为X轴数据，并将Data2作为Y轴数据
    return {
        name: key,
        type: 'line',
        data: groupedData[key].map(function(item) {
            return item.value;
        })
    };
});

// 提取X轴的日期数据（假设每组数据的日期都是相同的，只取第一组的日期作为X轴数据）
var dates = rawData.map(function(item) { return item.Date; });

// 去重并排序（如果后端数据已经排序，这一步可能不需要）
dates = [...new Set(dates)].sort(function(a, b) {
    return new Date(a) - new Date(b);
});

```

