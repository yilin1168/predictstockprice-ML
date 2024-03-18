// 检查localStorage是否已缓存数据
let rawData = localStorage.getItem('FdataCache');

if (rawData) {
    // 从localStorage获取数据
    rawData = JSON.parse(rawData);
    console.log('使用缓存数据', rawData);
} else {
    // 使用fetch请求数据
    fetch('/path/to/your/data/api')
        .then(response => response.json())
        .then(data => {
            console.log('使用新获取的数据', data);
            // 缓存数据到localStorage
            localStorage.setItem('FdataCache', JSON.stringify(data));
            // 更新rawData变量
            rawData = data;
        });
}

// Ver1:looks wrong
// 假设你的数据是一个对象，例如从Django模板变量传递过来的
var rawData = {{ Fdata| safe }};

// 定义一个缓存的键名
const DATA_KEY = 'myCachedData';

// 尝试从localStorage中获取数据
var cachedData = localStorage.getItem(DATA_KEY);

if (cachedData) {
    // 如果在localStorage找到了缓存的数据，使用它
    rawData = JSON.parse(cachedData);
} else {
    // 如果没有找到缓存的数据，将从服务器获取的数据保存到localStorage
    localStorage.setItem(DATA_KEY, JSON.stringify(rawData));
}

// 现在 rawData 包含了你需要的数据，无论是从缓存读取的还是直接从服务器加载的
