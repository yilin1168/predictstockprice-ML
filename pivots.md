```javascript
$.fn.colorCells = function() {
  this.find(".pvtVal").each(function() {
    var value = $(this).data("value");
    if(value < 0) {
      $(this).css("background-color", "red");
    } else if(value > 0) {
      $(this).css("background-color", "green");
    }
  });
  return this; // 使其可链式调用
};

$("#output").pivotUI(input, pivotOptions)
    .colorCells(); // 对生成的PivotTable调用colorCells函数


```


```javasript
let lastFilterResults = []; // 用来存储首次过滤的结果

document.getElementById('filter').addEventListener('submit', function(event) {
  event.preventDefault(); // 阻止表单的默认提交行为

  const lpValue = document.getElementById('lpSelect').value;
  const dateValue = document.getElementById('dateInput').value;
  // 更新首次过滤结果
  lastFilterResults = filterResults(lpValue, dateValue);
});

function filterResults(lpValue, dateValue, productValue = null) {
  // 根据参数进行过滤逻辑
  // 这里返回过滤结果作为示例
  return []; // 假设返回的过滤结果
}

document.addEventListener('DOMContentLoaded', () => {
  const tablinks = document.querySelectorAll('.tablinks');
  tablinks.forEach(button => {
    button.addEventListener('click', function() {
      // 移除所有Tabs上的active类
      tablinks.forEach(tab => {
        tab.classList.remove('active');
      });

      // 给被点击的Tab添加active类
      this.classList.add('active');

      const productValue = this.getAttribute('data-product');
      // 假设lpValue和dateValue在全局范围内仍可访问
      const lpValue = document.getElementById('lpSelect').value;
      const dateValue = document.getElementById('dateInput').value;
      
      // 使用首次过滤的结果和当前Tab的值进行二次过滤
      const secondFilterResults = filterResults(lpValue, dateValue, productValue);
      
      // 使用secondFilterResults来更新界面
    });
  });
});
```
