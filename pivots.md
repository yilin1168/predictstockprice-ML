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
