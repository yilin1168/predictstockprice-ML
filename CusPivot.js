function aggregateData(rawData, pivotX, pivotY, pivotFunction, pivotValue) {
    // 初始化结果对象
    const result = {};

    // 遍历原始数据进行聚合
    rawData.forEach(row => {
        const xValue = row[pivotX];
        const yValue = row[pivotY];

        // 确保结果对象有正确的结构
        if (!result[xValue]) {
            result[xValue] = {};
        }
        if (!result[xValue][yValue]) {
            result[xValue][yValue] = [];
        }

        // 将聚合值添加到数组中，稍后计算
        result[xValue][yValue].push(row[pivotValue]);
    });

    // 根据选择的聚合函数处理聚合值
    for (const x in result) {
        for (const y in result[x]) {
            if (pivotFunction === 'sum') {
                result[x][y] = result[x][y].reduce((acc, val) => acc + val, 0);
            } else if (pivotFunction === 'count') {
                result[x][y] = result[x][y].length;
            }
        }
    }

    return result;
}


//change to tabulator input format
function transformPivotedDataForTabulator(pivotedData, pivotX, pivotY) {
    let tableData = [];
    Object.entries(pivotedData).forEach(([xValue, yValues]) => {
        Object.entries(yValues).forEach(([yValue, value]) => {
            let row = {
                [pivotX]: xValue,
                [pivotY]: yValue,
                value: value,
            };
            tableData.push(row);
        });
    });
    return tableData;
}

//动态生成 Tabulator 列配置
function generateColumnsForTabulator(pivotX, pivotY) {
    return [
        {title: pivotX, field: pivotX},
        {title: pivotY, field: pivotY},
        {title: "Value", field: "value", formatter: "number", formatterParams: {thousandSeparator: ","}},
    ];
}


// 假定 pivotX, pivotY, pivotFunction, pivotValue 是根据用户的选择确定的
// const pivotedData = aggregateData(rawData, pivotX, pivotY, pivotFunction, pivotValue);

// // 转换聚合数据为 Tabulator 可接受的格式
// const tableData = transformPivotedDataForTabulator(pivotedData, pivotX, pivotY);

// // 生成列配置
// const columns = generateColumnsForTabulator(pivotX, pivotY);

// // 初始化 Tabulator
// const table = new Tabulator("#example-table", {
//     data: tableData,
//     columns: columns,
// });



// 示例原始数据
const rawData = [
    { lp: 'LP1', dateMonth: '2021-01', trader: 'Trader1', orderType: 'Type1', volume: 100, time: 2 },
    { lp: 'LP1', dateMonth: '2021-01', trader: 'Trader1', orderType: 'Type2', volume: 150, time: 3 },
    // 更多数据...
];

// 调用函数示例
const pivotX = 'lp'; // 或 'dateMonth'
const pivotY = 'trader'; // 或 'orderType'
const pivotFunction = 'sum'; // 或 'count'
const pivotValue = 'time'; // 或 'time'
const pivotedData = aggregateData(rawData, pivotX, pivotY, pivotFunction, pivotValue);

console.log(pivotedData);
console.log(transformPivotedDataForTabulator(pivotedData, pivotX, pivotY));
console.log("Tabulator columns!");
console.log(generateColumnsForTabulator(pivotX, pivotY));
