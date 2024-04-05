```html
<input type="date" id="startDate" name="startDate">
<input type="date" id="endDate" name="endDate">
<button onclick="loadData()">Load Data</button>

```


```javascript
function loadData() {
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    
    // 构造请求的URL，包括查询参数
    const url = `/your-endpoint?startDate=${startDate}&endDate=${endDate}`;
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // 在这里处理和显示数据
            console.log(data);
        })
        .catch(error => console.error('Error loading data:', error));
}
```

```python
from django.http import JsonResponse
from django.shortcuts import render

def your_view(request):
    start_date = request.GET.get('startDate')
    end_date = request.GET.get('endDate')
    
    # 假设你有一个模型Model，你可以根据日期范围查询数据
    # data = Model.objects.filter(date__range=[start_date, end_date])
    
    # 这里仅为示例，实际上你应该返回查询到的数据
    data = {'message': f'Data from {start_date} to {end_date}'}
    
    return JsonResponse(data)
```

