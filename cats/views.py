from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cat
from .serializers import CatSerializer

# 4 вариант вьюсеты
from rest_framework import viewsets 

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer 




# 3 вариант
# from rest_framework import generics


# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer 


# 2 varian
# class APICat(APIView):
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




# Обратите внимание на декоратор @api_view, 
# именно он настраивает обычную view-функцию для работы с API: 
# например, в нём указываются типы запросов, которые должна обрабатывать view-функция.
# В качестве аргумента декоратору передают список типов HTTP-запросов, которые должна обрабатывать эта функция
# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         #Данные в запросе приходят в формате JSON, 
#         # преобразуются в Python-словарь, 
#         # доступ к которому можно получить через объект request.data. 
#         # Этот словарь и передаётся в сериализатор через именованный параметр data.
#         # Чтобы сериализатор был готов принять список объектов, 
#         # в конструктор сериализатора нужно передать именованный параметр many=True
#         serializer = CatSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             # сохраним запись в БД при помощи метода save() 
#             # и в качестве подтверждения вернём в ответе созданный объект и статус-код, 
#             # соответствующий успешному выполнению операции;
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # если валидация не пройдена — вернём в ответе объект serializer.errors. 
#         # В этом объекте сериализатор автоматически создаёт словарь с перечнем ошибок, 
#         # возникших при валидации. Вместе с перечнем ошибок вернём и статус-код, 
#         # соответствующий неудачному результату выполнения операции.
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # Получаем все объекты модели
#     cats = Cat.objects.all()
#     # Передаём queryset в конструктор сериализатора
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)
