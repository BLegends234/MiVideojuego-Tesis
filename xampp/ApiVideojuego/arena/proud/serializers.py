from rest_framework import serializers
from proud.models import usuarios, score

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model=usuarios
        fields='__all__'
    

class ScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model=score
        fields='__all__'