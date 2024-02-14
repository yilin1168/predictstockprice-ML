```html
{% extends 'base.html' %}
{% load static %}
{% block title %}Display{% endblock %}

{% block css %}
<style>
    .scrollable-div { max-height: 400px; overflow-y: auto; }
    #main { width: 100%; height: 400px; }
</style>
{% endblock %}

{% block breadcrumb %}
<section class="content-header">
    <h1>
        Display
        <small>Your Data Display</small>
    </h1>
    <ol class="breadcrumb">
        <li><a href="#"><i class="fa fa-dashboard"></i> Home</a></li>
        <li class="active">Display</li>
    </ol>
</section>
{% endblock %}

{% block content %}
<section class="content">
    <div class="box">
        <div class="box-header">
            <h3 class="box-title">Choose Aggregate Dimension</h3>
            <form action="" method="get">
                <select name="aggregate_by" onchange="this.form.submit()">
                    <option value="LP" {% if aggregate_by == 'LP' %}selected{% endif %}>LP</option>
                    <option value="Date" {% if aggregate_by == 'Date' %}selected{% endif %}>Date</option>
                    <option value="Deal" {% if aggregate_by == 'Deal' %}selected{% endif %}>Deal</option>
                </select>
            </form>
        </div>
        <div class="box-body">
            <!-- ECharts Container -->
            <div id="main"></div>
        </div>
    </div>
</section>
{% endblock %}

{% block script %}
<script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
<script>


    // // 动态决定xAxis标签
    // var xAxisData;
    // if (aggregate_by === 'Date') {
    //     xAxisData = rawData.map(item => item.Date);
    // } else {
    //     // 如果是按LP或Deal聚合，可能需要其他逻辑来生成xAxisData
    //     xAxisData = rawData.map(item => item[aggregate_by]);
    // }
    // console.log(xAxisData);
    var myChart = echarts.init(document.getElementById('main'));

    var rawData = {{ data|safe }};
    var agg_by ="{{ aggregate_by|safe }}";


    var dates = ['data1','data2','data3','data4'];
    var series = [];
    for (const[key,value] of Object.entries(rawData)) {
        //console.log([key, value[agg_by],value['data1'],value['data2'],value['data3'],value['data4']]);
        series.push({
            name: value[agg_by],
            type: 'line',
            data: [value['data1'],value['data2'],value['data3'],value['data4']],
            endLabel: {
                show: true,
                formatter: function (params) {
                    console.log([params["seriesName"],params["value"]]);
                    return params["seriesName"] + ': ' + params["value"];
                    }
            }
        });
    }
    var option = {
        animationDuration: 3000,
        tooltip: {
            trigger: 'axis'
        },
        xAxis: {
            type: 'category',
            data: dates
        },
        yAxis: {
            type: 'value'
        },
        series: series
    };
    
    // 使用刚指定的配置项和数据显示图表
    myChart.setOption(option);


</script>
{% endblock %}


```




```python
def agg_view(request):

    annotations = {f'data{i}': Sum(f'data{i}') for i in range(1, 5)}

    aggregate_by = request.GET.get('aggregate_by', 'Date')
    if aggregate_by == 'LP':
        data = TableModel.objects.values('LP').annotate(**annotations).order_by('LP')
    elif aggregate_by == 'Deal':
        data = TableModel.objects.values('Deal').annotate(**annotations).order_by('Deal')
    else:  
        data = TableModel.objects.values('Date').annotate(**annotations).order_by('Date')

    # 将日期转换为字符串（如果需要）并准备数据发送到模板
    data_list = list(data)
    for item in data_list:
        if 'Date' in item:
            item['Date'] = item['Date'].strftime('%Y-%m-%d')  # 调整日期格式

    return render(request, 'dash/table_agg_line.html', {'data': data_list, 'aggregate_by': aggregate_by})
```

