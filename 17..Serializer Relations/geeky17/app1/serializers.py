from rest_framework import serializers
from .models import Song,Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']


class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True,read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # song = serializers.HyperlinkRelatedField(many=True,read_only=True, view_name='song-detail')
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field ='duration')
    # song = serializers.HyperlimkedIdentityField(view_name='song-detail')
    class Meta:
        model = Singer
        # fields = '__all__'
        fields = ['id','name','gender','song']
        