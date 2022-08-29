from encodings import search_function
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from django.http import JsonResponse


class CategoryListView(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('-url')

@api_view(['GET'])
def categoryList(request):
    if request.method == 'GET':
        category =  Category.objects.all()
        serializer = CategorySerializer(category, many = True)
        return JsonResponse({'category':serializer.data})

@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def detailCategory(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['PUT'])
def updateCategory(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteCategory(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        category.delete()
    return Response('category deleted successfully')

    






# class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     model = Category
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()
#     lookup_field = 'url'


# class CategoryIdView(generics.RetrieveUpdateDestroyAPIView):
#     model = Category
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()
#     lookup_field = 'pk'


# class LocationListView(generics.ListCreateAPIView):
#     model = Location
#     serializer_class = LocationSerializer
#     queryset = Location.objects.all().order_by('-url')


# class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
#     model = Location
#     serializer_class = LocationSerializer
#     queryset = Location.objects.all()
#     lookup_field = 'url'


# class LocationIdView(generics.RetrieveUpdateDestroyAPIView):
#     model = Location
#     serializer_class = LocationSerializer
#     queryset = Location.objects.all()
#     lookup_field = 'pk'


# class CatListView(generics.ListCreateAPIView):
#     model = Cat
#     serializer_class = CatSerializer
#     queryset = Cat.objects.all().order_by('-posted')


# class CatDetailView(generics.RetrieveUpdateDestroyAPIView):
#     model = Cat
#     serializer_class = CatSerializer
#     queryset = Cat.objects.all()
#     lookup_field = 'pk'


# class SearchCatView(generics.ListCreateAPIView):
#     model = Cat
#     serializer_class = CatSerializer
#     search_term = 'lions'
#     queryset = Cat.objects.all()
#     lookup_field = Cat.search_by_category(search_term)


# def index(request):
#     categories = Category.objects.order_by('-url')
#     locations = Location.objects.order_by('-url')
#     latest_cats = Cat.objects.order_by('-posted')[:8]
#     title = "Visit the Den of Africas' Big Cats"
#     # template = 'den/index.html'

#     context = {
#         'title': title,
#         'locations': locations,
#         'categories': categories,
#         'latest_cats': latest_cats,
#     }

#     return render(request, context)


# def detail(request, category_name, cat_id):
#     cat = Cat.objects.filter(id=cat_id).first()
#     categories = Category.objects.order_by('-url')
#     category = Category.objects.get(url=category_name)
#     locations = Location.objects.order_by('-url')
#     title = f'{cat.title}'
#     template = 'den/detail.html'

#     if category.id == cat.category:
#         category_name = category.url

#     context = {
#         'cat': cat,
#         'title': title,
#         'locations': locations,
#         'categories': categories,
#         'category_name': category_name
#     }

#     return render(request, template, context)


# def category(request, category_name):
#     category = Category.objects.get(url=category_name)
#     cats_by_category = Cat.objects.filter(
#         category_id=category.id).order_by('-posted')
#     categories = Category.objects.order_by('-url')
#     locations = Location.objects.order_by('-url')

#     title = f'{category.title}: {category.genus}'
#     template = 'den/category.html'

#     if category.id == cats_by_category:
#         category_name = category.url

#     context = {
#         'title': title,
#         'category': category,
#         'locations': locations,
#         'categories': categories,
#         'cats': cats_by_category,
#     }

#     return render(request, template, context)


# def locations(request):
#     locations = Location.objects.order_by('-url')
#     categories = Category.objects.order_by('-url')
#     title = 'Locations'
#     template = 'den/locations.html'

#     context = {
#         'title': title,
#         'locations': locations,
#         'categories': categories,
#     }

#     return render(request, template, context)


# def location(request, location_name):
#     location = Location.objects.get(url=location_name)
#     cats_by_location = Cat.objects.filter(
#         location_id=location.id).order_by('-posted')
#     locations = Location.objects.order_by('-url')
#     categories = Category.objects.order_by('-url')

#     title = f'{location.title}'
#     template = 'den/location.html'

#     if location.id == cats_by_location:
#         location_name = location.url

#     context = {
#         'title': title,
#         'location': location,
#         'locations': locations,
#         'categories': categories,
#         'cats': cats_by_location,
#     }

#     return render(request, template, context)


# def search(request):
#     locations = Location.objects.order_by('-url')
#     categories = Category.objects.order_by('-url')

#     if 'search' in request.GET and request.GET['search']:
#         search_term = request.GET['search']
#         searched_cats = Cat.search_by_category(search_term)
#         title = f'{search_term}'
#         template = 'den/search.html'

#         context = {
#             'title': title,
#             'locations': locations,
#             'categories': categories,
#             'searched_cats': searched_cats
#         }

#         return render(request, template, context)

#     else:
#         title = 'No Big Cat'
#         template = 'den/search.html'

#         context = {
#             'title': title,
#             'locations': locations,
#             'categories': categories,
#         }

        # return render(request, template, context)