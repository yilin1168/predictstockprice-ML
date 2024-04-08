async function fetchData(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        rawData = data['data'];
        console.log(rawData); // 在这里，rawData 已经更新
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

fetchData('你的URL');
// 任何依赖 rawData 更新后的代码都应该放在 fetchData 调用之后或者在 fetchData 内部的 .then() 块中
