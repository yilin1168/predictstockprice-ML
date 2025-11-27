你可以使用多线程来实现这个需求。以下是几种实现方案：

方案1：使用 threading + queue (推荐)

```python
import threading
import queue
import time
import redis  # 或者你使用的其他消息库

class MessageSubscriber:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.message_queue = queue.Queue()
        self.latest_aud_message = None
        self.lock = threading.Lock()
        self.running = True
        
    def start_subscribing(self):
        """在后台线程中持续订阅消息"""
        def subscribe_worker():
            # 这里以Redis为例，替换成你实际使用的消息系统
            r = redis.Redis()
            pubsub = r.pubsub()
            pubsub.subscribe(self.channel_name)
            
            for message in pubsub.listen():
                if not self.running:
                    break
                    
                if message['type'] == 'message':
                    msg_data = message['data'].decode('utf-8')
                    
                    # 过滤以AUD开头的消息
                    if msg_data.startswith('AUD'):
                        with self.lock:
                            self.latest_aud_message = msg_data
                        self.message_queue.put(msg_data)
        
        self.subscribe_thread = threading.Thread(target=subscribe_worker, daemon=True)
        self.subscribe_thread.start()
    
    def get_latest_aud_message(self):
        """获取最新的AUD消息"""
        with self.lock:
            return self.latest_aud_message
    
    def stop(self):
        self.running = False
```

方案2：在主程序中使用

```python
def get_latest_aud_message_function(subscriber):
    """你的函数 - 获取最新的AUD消息"""
    latest_message = subscriber.get_latest_aud_message()
    
    if latest_message:
        print(f"获取到最新AUD消息: {latest_message}")
        # 处理消息逻辑
        return latest_message
    else:
        print("暂无AUD消息")
        return None

# 主程序
def main():
    # 在while循环前subscribe一次
    subscriber = MessageSubscriber("your_channel_name")
    subscriber.start_subscribing()
    
    print("开始监听消息...")
    
    try:
        while True:
            # 主循环的其他逻辑
            time.sleep(1)  # 防止CPU占用过高
            
            # 在需要的时候调用函数获取最新AUD消息
            latest_aud = get_latest_aud_message_function(subscriber)
            
            if latest_aud:
                # 处理消息
                process_message(latest_aud)
                
    except KeyboardInterrupt:
        print("停止监听...")
        subscriber.stop()

def process_message(message):
    """处理消息的函数"""
    print(f"处理消息: {message}")
    # 你的消息处理逻辑

if __name__ == "__main__":
    main()
```

方案3：使用 threading.Event 控制

```python
import threading
import time
import redis

class AudMessageMonitor:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.latest_message = None
        self.message_event = threading.Event()
        self.lock = threading.Lock()
        self.running = True
        
    def start_monitoring(self):
        def monitor_worker():
            r = redis.Redis()
            pubsub = r.pubsub()
            pubsub.subscribe(self.channel_name)
            
            for message in pubsub.listen():
                if not self.running:
                    break
                    
                if message['type'] == 'message':
                    msg_data = message['data'].decode('utf-8')
                    
                    if msg_data.startswith('AUD'):
                        with self.lock:
                            self.latest_message = msg_data
                        self.message_event.set()  # 通知有新消息
        
        self.monitor_thread = threading.Thread(target=monitor_worker, daemon=True)
        self.monitor_thread.start()
    
    def wait_for_aud_message(self, timeout=None):
        """等待新的AUD消息"""
        if self.message_event.wait(timeout=timeout):
            self.message_event.clear()
            with self.lock:
                return self.latest_message
        return None
    
    def get_latest_aud_message(self):
        """立即获取最新的AUD消息（不等待）"""
        with self.lock:
            return self.latest_message
    
    def stop(self):
        self.running = False
        self.message_event.set()

# 使用示例
def main():
    monitor = AudMessageMonitor("your_channel")
    monitor.start_monitoring()
    
    try:
        while True:
            # 方式1: 等待新消息（阻塞）
            # new_message = monitor.wait_for_aud_message(timeout=5.0)
            
            # 方式2: 立即获取最新消息（非阻塞）
            new_message = monitor.get_latest_aud_message()
            
            if new_message:
                print(f"处理消息: {new_message}")
                # 重置消息，避免重复处理
                with monitor.lock:
                    if monitor.latest_message == new_message:
                        monitor.latest_message = None
            
            time.sleep(0.1)  # 短暂休眠
            
    except KeyboardInterrupt:
        monitor.stop()
        print("程序退出")
```

方案4：使用 asyncio (Python 3.7+)

```python
import asyncio
import redis.asyncio as redis  # 异步redis客户端

class AsyncAudMessageMonitor:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.latest_message = None
        self.new_message_event = asyncio.Event()
        
    async def start_monitoring(self):
        """启动消息监控"""
        r = redis.Redis()
        pubsub = r.pubsub()
        await pubsub.subscribe(self.channel_name)
        
        async for message in pubsub.listen():
            if message['type'] == 'message':
                msg_data = message['data'].decode('utf-8')
                
                if msg_data.startswith('AUD'):
                    self.latest_message = msg_data
                    self.new_message_event.set()
    
    async def get_latest_aud_message(self):
        """获取最新的AUD消息"""
        return self.latest_message
    
    async def wait_for_new_aud_message(self):
        """等待新的AUD消息"""
        await self.new_message_event.wait()
        self.new_message_event.clear()
        return self.latest_message

# 异步主程序
async def main():
    monitor = AsyncAudMessageMonitor("your_channel")
    
    # 启动监控任务
    monitor_task = asyncio.create_task(monitor.start_monitoring())
    
    try:
        while True:
            # 获取最新消息
            latest_message = await monitor.get_latest_aud_message()
            if latest_message:
                print(f"处理消息: {latest_message}")
            
            await asyncio.sleep(1)  # 异步休眠
            
    except KeyboardInterrupt:
        monitor_task.cancel()
        print("程序退出")

# asyncio.run(main())
```

关键要点：

1. 一次性订阅：在while循环前初始化并启动订阅
2. 线程安全：使用锁保护共享数据
3. 最新消息：总是获取最新的AUD消息
4. 资源清理：正确处理线程停止
5. 性能考虑：避免在循环中频繁创建连接

选择哪种方案取决于你的具体需求和使用的消息系统。方案1和2是最通用和稳定的选择。