from django.shortcuts import render
from rest_framework.generics import (ListAPIView, 
                                     CreateAPIView, 
                                     RetrieveAPIView, 
                                     UpdateAPIView, 
                                     DestroyAPIView, 
                                     ListCreateAPIView, 
                                     RetrieveUpdateDestroyAPIView,
                                     )
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import News, Category, Tag
from .serializer import NewsSerializer, CategorySerializer, TagSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import filters
############## News CRUD
class NewsListApiView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsCreateApiView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsRestrieveApiView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsUpdateApiView(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = News.objects.all()
    serializer_class = NewsSerializer


    def get_queryset(self):
        queryset = News.objects.filter(user = self.request.user, id = self.kwargs['pk'])
        return queryset
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not  instance :
            return Response("Cannot update NEWS", status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(instance)
        
        data ={
            'message':'news is updated'
            
        }
        return Response(data)
    
class DeleteNewsApiView(DestroyAPIView):
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = News.objects.filter(user = self.request.user, id=self.kwargs['pk'])
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not  instance :
            return Response("Cannot delete NEWS", status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        
        data ={
            'message':'news is deleted'
            
        }
        return Response(data)
###############     CATEGORY CRUD
    
class CategoryCreateApiView(CreateAPIView):
    permission_classes = (AllowAny, )
    queryset =   Category.objects.all()
    serializer_class = CategorySerializer  

class CategoryListApiView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteCategoryApiView(DestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )


    def get_queryset(self):
        queryset = Category.objects.filter(id=self.kwargs['pk'])

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not  instance :
            return Response("Cannot delete category", status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        
        data ={
            'message':'category is deleted'
            
        }
        return Response(data)
    

class NewsCatUpdateView(UpdateAPIView):
    
    permission_classes = (AllowAny, )
    serializer_class = CategorySerializer


    def get_queryset(self):
        
        queryset = Category.objects.filter(id = self.kwargs['pk'])
        return queryset
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not  instance :
            return Response("Cannot update Category", status=status.HTTP_400_BAD_REQUEST)
        
        
        else: 
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({"message": "category updated successfully"})

############     TAG CRUD

class TagCreateApiView(CreateAPIView):
    permission_classes = (AllowAny, )
    queryset =   Tag.objects.all()
    serializer_class = TagSerializer


class TagListApiView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Category.objects.all()
    serializer_class = TagSerializer

class DeleteTagApiView(DestroyAPIView):
    serializer_class = TagSerializer
    permission_classes = (AllowAny, )


    def get_queryset(self):
        queryset = Tag.objects.filter(id=self.kwargs['pk'])

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not  instance :
            return Response("Cannot delete category", status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        
        data ={
            'message':'category is deleted'
            
        }
        return Response(data)


class NewsTagUpdateView(UpdateAPIView):
    
    permission_classes = (AllowAny, )
    serializer_class = TagSerializer


    def get_queryset(self):
        
        queryset = Tag.objects.filter(id = self.kwargs['pk'])
        return queryset
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not  instance :
            return Response("Cannot update Category", status=status.HTTP_400_BAD_REQUEST)
        
        
        else: 
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({"message": "category updated successfully"})


####### CATEGORY FILTER
        

class CategoryFilterApiView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class =  NewsSerializer
    
    
    def get(self, request, pk): 
        data = News.objects.filter(category__id=pk)
        serializer = self.serializer_class(data, many=True)
        res = {
            "status": True,
            "data": serializer.data
        }
        return Response(res)
    
######### TAG FILTER
    
class TagFilterApiView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class =  NewsSerializer
    
    
    def get(self, request, pk): 
        data = News.objects.filter(category__id=pk)
        serializer = self.serializer_class(data, many=True)
        res = {
            "status": True,
            "data": serializer.data
        }
        return Response(res)
    
####### SEARCH
    


class SearchApiView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']

    