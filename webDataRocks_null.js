{
  "dataSource": {
    // 数据源配置
  },
  "slice": {
    // 切片配置
  },
  "options": {
    // 其他选项配置
  },
  "calculatedValues": [
    {
      "name": "Calculated Measure",
      "formula": "IF(ISNULL('MeasureName'), 0, 'MeasureName')",
      "format": "currency"
    }
  ]
}






// 假设这是你的原始数据
let rawData = [
    { category: "Fruit", type: "Apple", sales: 100 },
    { category: "Fruit", type: "Banana", sales: 150 },
    // 注意这里没有 "Fruit" 类别下的 "Orange"
    { category: "Vegetable", type: "Carrot", sales: 50 }
];

// 假设我们知道每个类别都应该有 Apple, Banana, 和 Orange
let expectedTypes = ["Apple", "Banana", "Orange"];

// 预处理数据，确保所有组合都存在
let processedData = [];
rawData.forEach(item => {
    expectedTypes.forEach(type => {
        if (type === item.type) {
            processedData.push(item);
        }
    });
});

// 检查并添加缺失的组合
expectedTypes.forEach(type => {
    rawData.forEach(item => {
        if (!processedData.find(d => d.type === type && d.category === item.category)) {
            processedData.push({ category: item.category, type: type, sales: 0 });
        }
    });
});

// 现在 processedData 包含所有组合，缺失的部分已用销售额为 0 填充
