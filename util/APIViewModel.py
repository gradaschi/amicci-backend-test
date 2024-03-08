from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class APIViewModel:
    @staticmethod
    def list_all(model, serializer_class, description):
        try:
            items = model.objects.all()
            serializer = serializer_class(items, many=True)
            return Response({'description': description, 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def get_one(model, serializer_class, id, description):
        try:
            item = get_object_or_404(model, id=id)
            serializer = serializer_class(item)
            return Response({'description': description, 'data': serializer.data})
        except Exception as e:
            return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def create(model, serializer_class, data, success_description, error_description):
        try:
            serializer = serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'description': success_description, 'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': error_description, 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def update(model, serializer_class, id, data, success_description):
        try:
            item = get_object_or_404(model, id=id)
            serializer = APIViewModel.validate_and_serialize(
                serializer_class, instance=item, data=data)
            return Response({'description': success_description}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def delete(model, id, success_description):
        try:
            item = get_object_or_404(model, id=id)
            item.delete()
            return Response({'description': success_description}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:

            return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def validate_and_serialize(serializer_class, **kwargs):
        serializer = serializer_class(**kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer
