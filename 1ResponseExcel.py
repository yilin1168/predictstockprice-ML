from django.http import HttpResponse
import os

def download_excel(request):
    # 文件路径，假设文件存储在项目根目录的 `files` 文件夹下
    file_path = os.path.join('files', 'example.xlsx')

    # 打开文件并读取内容
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # 返回文件作为HttpResponse
    response = HttpResponse(file_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="example.xlsx"'

    return response