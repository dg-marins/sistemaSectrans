from rest_framework import serializers
from .models import Video

class VideoDataSerializer(serializers.Serializer):
    video_file = serializers.CharField(max_length=255)
    channel = serializers.IntegerField()
    data_video = serializers.DateField()
    hora_video = serializers.TimeField()
    tamanho = serializers.FloatField()
    duracao = serializers.CharField(max_length=10)
    path_arquivo = serializers.CharField(max_length=255)

class VideoRequestSerializer(serializers.Serializer):
    carro = serializers.IntegerField()
    empresa = serializers.IntegerField()
    servidor = serializers.IntegerField()
    videos = VideoDataSerializer(many=True)