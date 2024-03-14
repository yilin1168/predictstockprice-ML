//TTA Groupby
const rawData = [
    {'lp':'lp1','d1':1,'d2':2,'d3':1,'d4':1},
    {'lp':'lp2','d1':1,'d2':2,'d3':1,'d4':1},
    {'lp':'lp1','d1':1,'d2':2,'d3':1,'d4':1},
    {'lp':'lp2','d1':2,'d2':2,'d3':1,'d4':1},
    {'lp':'lp1','d1':1,'d2':2,'d3':1,'d4':2}
];

// 分组并计算每个组的总和和计数
let groupedData = rawData.reduce((acc, item) => {
    if (!acc[item.lp]) {
        acc[item.lp] = { count: 0, totals: {d1: 0, d2: 0, d3: 0, d4: 0} };
    }
    acc[item.lp].count++;
    acc[item.lp].totals.d1 += item.d1;
    acc[item.lp].totals.d2 += item.d2;
    acc[item.lp].totals.d3 += item.d3;
    acc[item.lp].totals.d4 += item.d4;
    return acc;
}, {});

// 构造最终结果数组
let result = Object.keys(groupedData).map(lp => {
    let averages = {};
    averages.lp = lp;
    Object.keys(groupedData[lp].totals).forEach(key => {
        averages[key] = groupedData[lp].totals[key] / groupedData[lp].count;
    });
    return averages;
});

console.log(result);
