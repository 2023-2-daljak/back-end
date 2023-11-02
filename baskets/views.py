from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Basket
from .serializers import BasketSerializer


class Baskets(APIView):
    def get(self, request):
        all_categories = Basket.objects.all()
        serializer = BasketSerializer(
            all_categories,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = BasketSerializer(data=request.data)
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(
                BasketSerializer(updated_category).data,
            )
        else:
            return Response(serializer.errors)


class BasketDetail(APIView):
    def get_object(self, pk):
        try:
            return Basket.objects.get(pk=pk)
        except Basket.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        serializer = BasketSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = BasketSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(BasketSerializer(updated_category).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
