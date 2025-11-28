import threading
import time

def create_subscriber_system(channel_name):
    """创建订阅系统，返回操作函数"""
    state = {
        'latest_aud_message': None,
        'lock': threading.Lock(),
        'running': True,
        'thread': None
    }
    
    def subscribe_worker(channel):
        # 这里需要替换为你实际使用的消息系统
        # 以下是用Redis的示例
        try:
            import redis
            r = redis.Redis()
            pubsub = r.pubsub()
            pubsub.subscribe(channel)
            
            for message in pubsub.listen():
                if not state['running']:
                    break
                    
                if message['type'] == 'message':
                    msg_data = message['data'].decode('utf-8')
                    
                    if msg_data.startswith('AUD'):
                        with state['lock']:
                            state['latest_aud_message'] = msg_data
                        print(f"收到AUD消息: {msg_data}")
        except ImportError:
            # 模拟消息接收（用于测试）
            print(f"模拟订阅频道: {channel}")
            msg_count = 0
            while state['running']:
                time.sleep(2)
                msg_count += 1
                mock_msg = f"AUD_Message_{msg_count}"
                with state['lock']:
                    state['latest_aud_message'] = mock_msg
                print(f"模拟收到: {mock_msg}")
    
    def init_subscriber():
        """初始化订阅"""
        state['thread'] = threading.Thread(
            target=subscribe_worker,
            args=(channel_name,),
            daemon=True
        )
        state['thread'].start()
        print(f"已订阅频道: {channel_name}")
        return True
    
    def get_latest_message():
        """获取最新AUD消息"""
        with state['lock']:
            return state['latest_aud_message']
    
    def stop_subscriber():
        """停止订阅"""
        state['running'] = False
        print("订阅已停止")
    
    def reset_message():
        """重置消息（可选）"""
        with state['lock']:
            state['latest_aud_message'] = None
    
    # 返回所有操作函数
    return {
        'init': init_subscriber,
        'get_latest': get_latest_message,
        'stop': stop_subscriber,
        'reset': reset_message
    }