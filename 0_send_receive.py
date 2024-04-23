import socket

# 配置接收端的IP地址和端口
host = '192.168.1.100'
port = 5001

# 创建一个socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
s.connect((host, port))

# 发送数据
message = "hello from python"
s.sendall(message.encode('utf-8'))

# 关闭socket
s.close()

