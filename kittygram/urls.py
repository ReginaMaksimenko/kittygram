from django.urls import include, path

# 4 вариант для вью сетов
from cats.views import CatViewSet
from rest_framework.routers import DefaultRouter

# Создаётся роутер
router = DefaultRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
    path('', include(router.urls), name='api-root'),
] 


# # 3 вариант
# from rest_framework import generics

# # 3 variant
# from cats.views import CatList, CatDetail

# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ] 


# 2 варинат
# from cats.views import APICat

# urlpatterns = [
#     path('cats/', APICat.as_view()),
# ] 

# 1 вариант
# from cats.views import cat_list

# urlpatterns = [
#    path('cats/', cat_list),
# ]


