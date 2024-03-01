function nullToZeroFormatter(row, column, value) {
    // 检查值是否为 null
    if (value === null) {
        return "0"; // 将 null 值替换为字符串 "0"
    }
    return value; // 如果不是 null，则返回原始值
}

    "slice": {
        // 其他切片配置
    },
    "formats": [
        {
            "name": "NullToZero", // 定义一个格式名称
            "nullValue": "0", // 对于 null 值，显示为 "0"
            "formatterFunction": nullToZeroFormatter // 引用上面定义的格式化函数
        }
    ],
    "options": {
        // 其他选项配置
    }


const jsonData = JSON.stringify(rawData);
const sizeInBytes = new TextEncoder().encode(jsonData).length;
const sizeInKilobytes = sizeInBytes / 1024;
console.log(`Approximate size of rawData: ${sizeInKilobytes} KB`);
