from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ArticleSerializer,ArticleListSerializer,ArticleCreateSerializer

class ArticleView(APIView):
  def get(self, request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
  def post(self, request):
    serializer = ArticleCreateSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

class ArticleDetailView(APIView):
  def get(self, request, article_id):
    article = Article.objects.get(id=article_id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
    
  def put(self, request, article_id):
    pass
  def delete(self, request, article_id):
    pass  


class CommentView(APIView):
  def get(self, request):
    pass
  def post(self, request):
    pass


class CommentDetailView(APIView):
  def put(self, request):
    pass
  
  def delete(self, request):
    pass
  
class LikeView(APIView):
  def post(self, request):
    pass