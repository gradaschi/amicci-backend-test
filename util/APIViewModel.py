from rest_framework.response import Response
from rest_framework import status


class APIViewModel:
    @staticmethod
    def _get_item_or_404(model, id, error_description):
        try:
            return model.objects.get(id=id)
        except model.DoesNotExist:
            return Response({'error': error_description}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def _serialize_data(serializer_class, data):
        serializer = serializer_class(data=data)
        return serializer

    @staticmethod
    def _handle_serializer_response(serializer, success_description, error_description, status_code):
        if serializer.is_valid():
            serializer.save()
            return Response({'description': success_description, 'data': serializer.data}, status=status_code)
        else:
            return Response({'error': 'Requisição inválida', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def list_all(model, serializer_class, description, error_description):
        try:
            items = model.objects.all()
            if not items:
                return Response({'error': error_description}, status=status.HTTP_404_NOT_FOUND)
            serializer = serializer_class(items, many=True)
            return Response({'description': description, 'data': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({'error': 'Erro inesperado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def get_one(model, serializer_class, id, description, error_description):
        item = APIViewModel._get_item_or_404(model, id, error_description)
        serializer = serializer_class(item, data=item.__dict__)
        return APIViewModel._handle_serializer_response(serializer, description, error_description, status.HTTP_200_OK)

    @staticmethod
    def create(model, serializer_class, data, success_description, error_description):
        serializer = APIViewModel._serialize_data(serializer_class, data)
        return APIViewModel._handle_serializer_response(serializer, success_description, error_description, status.HTTP_201_CREATED)

    @staticmethod
    def update(model, serializer_class, id, data, success_description, error_description):
        item = APIViewModel._get_item_or_404(model, id, error_description)
        serializer = serializer_class(item, data=data, partial=True)
        return APIViewModel._handle_serializer_response(serializer, success_description, error_description, status.HTTP_200_OK)

    @staticmethod
    def delete(model, id, success_description, error_description):
        item = APIViewModel._get_item_or_404(model, id, error_description)
        item.delete()
        return Response({'description': success_description}, status=status.HTTP_200_OK)

    @staticmethod
    def validate_and_serialize(serializer_class, **kwargs):
        serializer = APIViewModel._serialize_data(serializer_class, kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer
