//load ver1
// IndexedDB初始化和打开
function initDB(callback) {
    const dbName = "myDatabase";
    const dbVersion = 2; // 确保这个版本号高于任何现有的数据库版本
    const request = indexedDB.open(dbName, dbVersion);

    request.onupgradeneeded = function(event) {
        var db = event.target.result;
        if (!db.objectStoreNames.contains('dataStore1')) {
            db.createObjectStore('dataStore1', { autoIncrement: true });
        }
    };

    request.onsuccess = function(event) {
        console.log("Database initialized successfully");
        const db = event.target.result;
        callback(db); // 调用回调函数，传递数据库实例
    };

    request.onerror = function(event) {
        console.error("Database error: " + event.target.errorCode);
    };
}

// 从IndexedDB载入数据
function loadData(db) {
    // 这里实现从IndexedDB读取并处理数据的逻辑
    console.log("Data loaded successfully.");
    // 例如，从`dataStore1`读取数据...
}

// 添加数据到IndexedDB
function addData(db, data) {
    var transaction = db.transaction(["dataStore1"], "readwrite");
    var store = transaction.objectStore("dataStore1");
    data.forEach(item => {
        store.add(item);
    });

    transaction.oncomplete = function() {
        console.log("All data added successfully!");
    };

    transaction.onerror = function(event) {
        console.error("Transaction error: ", event.target.error);
    };
}

// 初始化数据库并载入数据
initDB(function(db) {
    loadData(db); // 载入初始数据

    // 假设这是通过某种方式从后端接收到的新数据
    // 当然，实际上你可能需要设置事件监听器来响应动态接收的数据
    const rawData = /* 从后端获取的数据 */;
    addData(db, rawData); // 添加新数据到数据库
});









//IndexedDB
// 打开一个IndexedDB数据库
var openRequest = indexedDB.open('myDatabase', 1);

openRequest.onupgradeneeded = function(e) {
    var db = e.target.result;
    if (!db.objectStoreNames.contains('data')) {
        db.createObjectStore('data', {keyPath: 'id'});
    }
};

openRequest.onsuccess = function(e) {
    var db = e.target.result;
    var tx = db.transaction('data', 'readwrite');
    var store = tx.objectStore('data');

    fetch('/path/to/your/data/api')
        .then(response => response.json())
        .then(data => {
            console.log('使用新获取的数据', data);
            // 存储数据到IndexedDB
            store.put({id: 'rawData', value: data});
        })
        .catch(err => console.error('Fetch error:', err));
};

openRequest.onerror = function(e) {
    console.error('IndexedDB error:', e.target.error);
};


















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
