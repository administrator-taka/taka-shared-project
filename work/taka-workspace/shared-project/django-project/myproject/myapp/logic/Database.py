from myapp.serializer import VideoDetailSerializer


def insert_video_detail(data):
    video_detail_serializer = VideoDetailSerializer(data=data)
    if video_detail_serializer.is_valid():
        video_detail_serializer.save()
    else:
        print(video_detail_serializer.errors)
