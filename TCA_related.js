
// TCA Aggregate to T 
let rawData = [
    { name: "Item A", t1: 10 },
    { name: "Item B", t2: 20 },
    { name: "Item C", t3: null },
    { name: "Item D", t4: 15 },
];

// 预期处理多达40个t值
const processData = (data) => {
    let processedData = [];
    data.forEach((item, index) => {
        for (let i = 1; i <= 40; i++) {
            let key = `t${i}`;
            if (item.hasOwnProperty(key)) {
                processedData.push({
                    name: item.name,
                    T: key,
                    value: item[key],
                    order: index + 1
                });
                // 假设每个项只有一个t值，找到后即跳出循环
                break;
            }
        }
    });
    return processedData;
};

let resultData = processData(rawData);
console.log(resultData);
