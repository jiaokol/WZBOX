import json

# 读取 JSON 文件
with open('tv_channels.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 解析每个电视频道的信息
for channel in data['tv_channels']:
    channel_name = channel['channel_name']
    stream_url = channel['stream_url']
    
    # 打印每个电视频道的信息
    print(f'频道名称: {channel_name}')
    print(f'流媒体URL: {stream_url}')
    print('-' * 50)
