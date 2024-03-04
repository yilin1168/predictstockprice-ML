# views.py
from django.http import HttpResponse
from subprocess import Popen

def run_script(request):
    # 启动第一个脚本
    Popen(['path/to/your/first_script.bat'], shell=True)
    # 启动第二个脚本
    Popen(['path/to/your/second_script.bat'], shell=True)
    # 可以继续添加更多的Popen调用来运行其他脚本或程序
    
    return HttpResponse("Scripts are running.")

#urls.py
from django.urls import path
from .views import run_script

urlpatterns = [
    path('run-script/', run_script, name='run-script'),
]

#html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Run Script</title>
</head>
<body>
    <button id="run-script">Run Script</button>
    <script>
        document.getElementById('run-script').addEventListener('click', function() {
            fetch('/run-script/')
            .then(response => response.text())
            .then(text => alert(text))
            .catch(error => console.error('Error:', error));
        });
    </script>
</body>
</html>
