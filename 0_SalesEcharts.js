<!DOCTYPE html>
<html>
<head>
    <title>ECharts Line Chart with Dual Y Axes</title>
    <!-- 引入 ECharts -->
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.2.2/dist/echarts.min.js"></script>
</head>
<body>
    <!-- 定义一个具有一定尺寸的 DOM 容器 -->
    <div id="chart" style="width: 800px; height: 400px;"></div>

    <script>

    // 假设 rawData1 和 rawData2 是你的两组原始数据
    var rawData1 = [
        { date: '2024-05-01', value: 10 },
        { date: '2024-05-02', value: 20 },
        { date: '2024-05-03', value: 30 }
    ];
    
    var rawData2 = [
        { date: '2024-05-01', value: 100 },
        { date: '2024-05-02', value: 200 },
        { date: '2024-05-03', value: 300 },
        { date: '2024-05-04', value: 400 },
        { date: '2024-05-05', value: 500 }
    ];
    
    // 创建一个空数组用于存储 rawData2 中与 rawData1 中日期对应的数据
    var extractedData = [];
    
    // 遍历 rawData1
    rawData1.forEach(function(data1) {
        // 在 rawData2 中查找与当前日期相同的数据
        var correspondingData2 = rawData2.find(function(data2) {
            return data2.date === data1.date;
        });
        
        // 如果找到了对应日期的数据，则将其加入 extractedData
        if (correspondingData2) {
            extractedData.push({
                date: data1.date,
                value1: data1.value, // rawData1 中的值
                value2: correspondingData2.value // rawData2 中的值
            });
        }
    });
    
    // 输出提取的数据
    console.log(extractedData);

        // 基于准备好的 DOM，初始化 ECharts 实例
        var myChart = echarts.init(document.getElementById('chart'));

        // 指定图表的配置项和数据
        var option = {
            // 设置图表标题
            title: {
                text: 'ECharts Line Chart with Dual Y Axes'
            },
            // 设置图例
            legend: {
                data:['Series 1', 'Series 2']
            },
            // 定义两个 Y 轴
            yAxis: [
                {
                    type: 'value', // 第一个 Y 轴
                    name: 'Y1',
                    position: 'left',
                    axisLabel: {
                        formatter: '{value}'
                    }
                },
                {
                    type: 'value', // 第二个 Y 轴
                    name: 'Y2',
                    position: 'right',
                    axisLabel: {
                        formatter: '{value}'
                    }
                }
            ],
            // 定义 X 轴
            xAxis: {
                type: 'category',
                data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
            },
            // 定义系列
            series: [
                {
                    name: 'Series 1',
                    type: 'line',
                    yAxisIndex: 0, // 指定该系列使用第一个 Y 轴
                    data: [5, 20, 36, 10, 10, 20, 5]
                },
                {
                    name: 'Series 2',
                    type: 'line',
                    yAxisIndex: 1, // 指定该系列使用第二个 Y 轴
                    data: [111115, 121100, 131146, 141120, 141120, 111130, 111115]
                }
            ]
        };

        // 使用刚指定的配置项和数据显示图表
        myChart.setOption(option);



    </script>
</body>
</html>






