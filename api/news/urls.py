from django.urls import path
from .views import(NewsListApiView, 
                   NewsCreateApiView, 
                   NewsRestrieveApiView, 
                   NewsUpdateApiView, 
                   DeleteNewsApiView, 
                   CategoryCreateApiView, 
                   CategoryListApiView, 
                   DeleteCategoryApiView,
                   NewsCatUpdateView,
                   TagCreateApiView,
                   TagListApiView,
                   DeleteTagApiView,
                   NewsTagUpdateView,
                   CategoryFilterApiView,
                   TagFilterApiView,
                   SearchApiView)
########  NEWS URLS
urlpatterns = [
    path('list/', NewsListApiView.as_view()),
    path('create/', NewsCreateApiView.as_view()),
    path('retrieve/', NewsRestrieveApiView.as_view()),
    path('update/<int:pk>/', NewsUpdateApiView.as_view()),
    path('delete/<int:pk>/', DeleteNewsApiView.as_view()),
    

]
#########   CATEGORY URLS
urlpatterns +=[
    path('create_cat/',CategoryCreateApiView.as_view()),
    path('list_cat/',CategoryListApiView.as_view()),
    path('del_cat/<int:pk>/',DeleteCategoryApiView.as_view()),
    path('update_cat/<int:pk>/',NewsCatUpdateView.as_view()),
    path('cat_filter/<int:pk>/', CategoryFilterApiView.as_view()),

]
########## TAG URLS
urlpatterns +=[
    path('create_tag/',TagCreateApiView.as_view()),
    path('list_tag/',TagListApiView.as_view()),
    path('delete_tag/',DeleteTagApiView.as_view()),
    path('update_tag/',NewsTagUpdateView.as_view()),
    path('tag_filter/<int:pk>/', TagFilterApiView.as_view())

]

#######  SEARCH URL


urlpatterns +=[
    path('search_news/',SearchApiView.as_view()),
]





