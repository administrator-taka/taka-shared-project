from myapp.serializer import VideoDetailSerializer, ChannelDetailSerializer


def insert_video_detail(data):
    video_detail_serializer = VideoDetailSerializer(data=data)
    if video_detail_serializer.is_valid():
        video_detail_serializer.save()
    else:
        print(video_detail_serializer.errors)

def insert_channel_detail(data):
    channel_detail_serializer = ChannelDetailSerializer(data=data)
    if channel_detail_serializer.is_valid():
        channel_detail_serializer.save()
    else:
        print(channel_detail_serializer.errors)
