from rest_framework import serializers
from .models import Song,Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'


class SingerSerializer(serializers.ModelSerializer):
    song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    class Meta:
        model=Singer
        fields=['id','name','gender','song']

