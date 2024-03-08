from util.APIViewModel import APIViewModel
from .models import Retailer
from .serializers import RetailerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RetailerList(APIView):
    def get(self, request):
        description = 'Varejistas disponíveis'
        error_description = 'Não há varejista disponível'
        return APIViewModel.list_all(Retailer, RetailerSerializer, description, error_description)

    def post(self, request):
        try:
            data = request.data
            serializer = RetailerSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            success_description = f'Criado com sucesso. Id: {
                serializer.data["id"]}'
            return Response({'description': success_description, 'data': serializer.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': 'Objeto Varejista inválido'}, status=status.HTTP_400_BAD_REQUEST)


class RetailerDetail(APIView):
    def get(self, request, id):
        description = 'Varejista existe'
        error_description = 'Varejista não existe'
        return APIViewModel.get_one(Retailer, RetailerSerializer, id, description, error_description)

    def put(self, request, id):
        try:
            data = request.data
            description = f'Atualizado com sucesso. Id: {id}'
            error_description = 'Objeto Varejista inexistente'
            return APIViewModel.update(Retailer, RetailerSerializer, id, data, description, error_description)

        except Exception as e:
            return Response({'error': 'Erro inesperado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        description = 'Deletado com sucesso'
        error_description = 'Varejista não encontrado'
        return APIViewModel.delete(Retailer, id, description, error_description)
