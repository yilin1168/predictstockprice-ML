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


from django.http import JsonResponse
from subprocess import Popen

def run_script(request):
    if request.method == "POST" and request.is_ajax():
        # 启动第一个脚本
        Popen(['path/to/your/first_script.bat'], shell=True)
        # 启动第二个脚本
        Popen(['path/to/your/second_script.bat'], shell=True)
        # 可以继续添加更多的Popen调用来运行其他脚本或程序

        return JsonResponse({"message": "Scripts are running."})
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)



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
    <title>Run Script and Display Output</title>
</head>
<body>
    <input type="text" id="script-path" placeholder="Enter path to script">
    <button id="run-script">Run Script</button>
    <textarea id="script-output" rows="10" cols="50">Script output will be displayed here...</textarea>
    <script>
        document.getElementById('run-script').addEventListener('click', function() {
            const scriptPath = document.getElementById('script-path').value;
            fetch('/run-script/', {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ path: scriptPath })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('script-output').value = data.message;
            })
            .catch(error => console.error('Error:', error));
        });
    </script>
</body>
</html>


#views.py again
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from subprocess import Popen, PIPE
import json

@csrf_exempt
def run_script(request):
    if request.method == "POST":
        # 从请求体中获取脚本路径
        data = json.loads(request.body)
        script_path = data.get('path')

        # 对脚本路径进行安全性检查（这里需要实现具体的安全检查逻辑）
        # ...

        # 以管道形式执行脚本并捕获输出
        process = Popen(script_path, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = process.communicate()

        # 将标准输出和错误输出合并为响应消息
        response_message = stdout.decode() + stderr.decode()

        return JsonResponse({"message": response_message})
    else:
        # 如果是GET请求，渲染模板
        return render(request, 'yourapp/template.html')

