// 原始数据
let rawData = [
    {date: '2023-01-01', value: 10 ,other:'a'},
    {date: '2023-01-02', value: 4 ,other:'a'},
    {date: '2023-01-03', value: 3 ,other:'a'},
    {date: '2023-01-04', value: 4 ,other:'a'},
    {date: '2023-01-05', value: 3 ,other:'a'},
    {date: '2023-01-06', value: 1 ,other:'a'}
  ];
  
  // 计算移动平均值
  function calculateMovingAverage(data, period) {
    let movingAverages = [];
  
    // 从数组的第 'period' 个元素开始计算
    for (let i = period - 1; i < data.length; i++) {
      let sum = 0;
      
      // 计算当前元素和之前 'period' - 1 个元素的总和
      for (let j = 0; j < period; j++) {
        sum += data[i - j].value;
      }
      
      // 计算平均值并存储结果
      let average = sum / period;
      movingAverages.push({date: data[i].date, movingAverage: average});
    }
  
    return movingAverages;
  }
  
  // 计算过去两天的移动平均值
  let movingAverageData = calculateMovingAverage(rawData, 2);
  console.log(movingAverageData);
