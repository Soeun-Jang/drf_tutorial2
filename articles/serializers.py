from rest_framework import serializers
from articles.models import Article,Comment



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Comment
      fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
      model = Comment
      fields = ("content",)

  
class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    #obj 인스턴스의 user속성에서 email값 추출하여 반환해서 user필드에 추가
    def get_user(self,obj):
      return obj.user.email
    class Meta:
        model = Article
        fields = '__all__'
        
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "image", "content")
        
class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self,obj):
      return obj.user.email
    
    class Meta:
        model = Article
        fields = ('pk','title','content','user','created_at')

