from rest_framework import serializers
from articles.models import Article,Comment



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self,obj):
      return obj.user.email
    class Meta:
      model = Comment
      exclude = ("article",)
      
      
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
      model = Comment
      fields = ("content",)

  
class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comment_set = CommentSerializer(many=True)
    likes = serializers.StringRelatedField(many=True)
    
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
    likes_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    
    def get_user(self,obj):
      return obj.user.email
    
    def get_likes_count(self, obj):
      return obj.likes.count()
    
    def get_comment_count(self, obj):
      return obj.comment_set.count()
    
    class Meta:
        model = Article
        fields = ('pk','title','content','user','created_at', 'likes_count', 'comment_count')

