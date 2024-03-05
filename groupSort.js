//group-sort(row-col)
let data = [
    { name: "Item A", column: "tag1", value: 10 },
    { name: "Item B", column: "tag1", value: 20 },
    { name: "Item C", column: "tag1", value: null },
    { name: "Item D", column: "tag1", value: 15 },
    { name: "Item A", column: "tag2", value: 10 },
    { name: "Item B", column: "tag2", value: 20 },
    { name: "Item C", column: "tag3", value: null },
    { name: "Item D", column: "tag3", value: 15 },
    { name: "Item A", column: "tag3", value: null },
    { name: "Item B", column: "tag3", value: 13 },
];

// 分组数据
let groupedData = data.reduce((acc, item) => {
    acc[item.column] = acc[item.column] || [];
    acc[item.column].push(item);
    return acc;
}, {});

Object.keys(groupedData).forEach(column => {
    // 分离含有null值和不含null值的元素
    let nonNullValues = groupedData[column].filter(item => item.value !== null);
    let nullValues = groupedData[column].filter(item => item.value === null);

    // 仅对不含null值的元素进行排序
    nonNullValues.sort((a, b) => a.value - b.value);

    // 重新组合数组，保持null值的原始位置
    let sortedGroup = [...nonNullValues, ...nullValues];

    // 更新排序序号，仅对非null值进行编号
    sortedGroup.forEach((item, index) => {
        if (item.value !== null) {
            item.sortOrder = index + 1; // 添加排序序号，从1开始
        }
    });

    // 更新分组数据
    groupedData[column] = sortedGroup;
});

// 重新组合数据
let sortedData = [].concat(...Object.values(groupedData));

console.log(sortedData);




//group-sort all(row-col)
let data = [
    { name: "Item A", column: "tag1", value: 10 },
    { name: "Item B", column: "tag1", value: 20 },
    { name: "Item C", column: "tag1", value: null },
    { name: "Item D", column: "tag1", value: 15 },
    { name: "Item A", column: "tag2", value: 10 },
    { name: "Item B", column: "tag2", value: 20 },
    { name: "Item C", column: "tag3", value: null },
    { name: "Item D", column: "tag3", value: 15 },
    { name: "Item A", column: "tag3", value: null },
    { name: "Item B", column: "tag3", value: 13 },
];

// 步骤 1: 计算每个name的总和并添加column='all'
let sumsByName = data.reduce((acc, {name, value}) => {
    acc[name] = (acc[name] || 0) + (value || 0);
    return acc;
}, {});

let allSumsData = Object.entries(sumsByName).map(([name, sum]) => ({
    name, column: 'all', value: sum
}));

data = data.concat(allSumsData);

// 步骤 2: 分组数据并计算sortedOrder
let groupedData = data.reduce((acc, item) => {
    acc[item.column] = acc[item.column] || [];
    acc[item.column].push(item);
    return acc;
}, {});

Object.keys(groupedData).forEach(column => {
    let items = groupedData[column];
    // 排除null，计算排序序号
    items
        .filter(item => item.value !== null)
        .sort((a, b) => a.value - b.value)
        .forEach((item, index) => {
            item.sortedOrder = index + 1;
        });
});

// 步骤 3: 将处理过的数据重新组合，可能需要根据需要进行额外的处理，比如移除重复项
let processedData = [].concat(...Object.values(groupedData));

console.log(processedData);

