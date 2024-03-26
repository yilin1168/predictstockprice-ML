<script type="application/json" id="Fdata">
    {{ Fdata|safe }}
</script>


document.addEventListener("DOMContentLoaded", function() {
    // 假定Fdata已经是一个JavaScript对象数组
    const Fdata = JSON.parse(document.getElementById('Fdata').textContent);

    // 数据库信息
    const dbName = "myDatabase";
    const dbVersion = 1;

    // 打开数据库
    let db;
    const request = indexedDB.open(dbName, dbVersion);

    // 数据库升级或首次创建
    request.onupgradeneeded = function(event) {
        db = event.target.result;
        if (!db.objectStoreNames.contains('dataStore')) {
            db.createObjectStore('dataStore', {keyPath: 'id'});
        }
    };

    // 成功打开数据库
    request.onsuccess = function(event) {
        db = event.target.result;
        console.log("Database initialized successfully");
        // 添加数据
        addData(Fdata);
    };

    // 打开数据库失败
    request.onerror = function(event) {
        console.error("Database error: " + event.target.errorCode);
    };

    // 添加数据到IndexedDB
    function addData(data) {
        const transaction = db.transaction(["dataStore"], "readwrite");
        const store = transaction.objectStore("dataStore");

        data.forEach(item => {
            store.add(item);
        });

        transaction.oncomplete = function() {
            console.log("All data added successfully!");
            // 也许在这里你会想获取数据来验证或其他用途
            getData(data => console.log("Retrieved data:", data));
        };

        transaction.onerror = function(event) {
            console.error("Transaction error: ", event.target.error);
        };
    }

    // 从IndexedDB获取数据
    function getData(callback) {
        const transaction = db.transaction(["dataStore"]);
        const store = transaction.objectStore("dataStore");
        const request = store.getAll(); // 获取所有数据

        request.onsuccess = function(event) {
            callback(event.target.result); // 使用回调函数返回结果
        };

        request.onerror = function(event) {
            console.error("Request error: ", event.target.error);
        };
    }
});
