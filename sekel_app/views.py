from rest_framework.response import Response
from rest_framework import viewsets

from sekel_app.models import Category, Product
from sekel_project.serializers import CategorySerializer, ProductSerializer


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = Category.objects.all()
        return category

    # perform updation for category Section
    def put(self, request, *args, **kwargs):
        category_obj = Category.objects.get()

        data = request.data

        category_obj.cate_name = data["cate_name"]

        category_obj.save()

        serialize = CategorySerializer(category_obj)
        return Response(serialize.data)
    # End

class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.all()
        return product

    # POST METHOD START
    def create(self, request, *args, **kwargs):
        data = request.data  # Extract the data from Request

        new_product = Product.objects.create(name=data["name"], price=data["price"])

        new_product.save()

        for category in data["categories"]:
            category_obj = Category.objects.get(cate_name=category["name"])
            new_product.categories.add(category_obj)

        serializer = ProductSerializer(new_product)
        return Response(serializer.data)

    # POST METHOD END

    # UPDATE METHOD START
    def update(self, request, *args, **kwargs):
        # product_obj = Product.objects.get()
        product_obj = self.get_object()
        data = request.data

        cate_name = Category.objects.get(cate_name=data["cate_name"])

        product_obj.cate_name = cate_name

        product_obj.name = data["name"]
        product_obj.price = data["price"]

        product_obj.save()

        serialize = ProductSerializer(product_obj)
        return Response(serialize.data)

    # UPDATE METHOD END
