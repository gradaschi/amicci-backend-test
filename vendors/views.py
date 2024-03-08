from util.APIViewModel import APIViewModel
from .models import Vendor
from .serializers import VendorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class VendorList(APIView):
    def get(self, request):
        description = 'Fornecedores disponíveis'
        error_description = 'Não há fornecedor disponível'
        return APIViewModel.list_all(Vendor, VendorSerializer, description, error_description)

    def post(self, request):
        try:
            data = request.data
            serializer = VendorSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            success_description = f'Criado com sucesso. Id: {
                serializer.data["id"]}'
            return Response({'description': success_description, 'data': serializer.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': 'Objeto Vendor inválido'}, status=status.HTTP_400_BAD_REQUEST)


class VendorDetail(APIView):
    def get(self, request, id):
        description = 'Fornecedor existe'
        error_description = 'Fornecedor não existe'
        return APIViewModel.get_one(Vendor, VendorSerializer, id, description, error_description)

    def put(self, request, id):
        try:
            data = request.data
            description = f'Atualizado com sucesso. Id: {id}'
            error_description = 'Objeto Vendor inexistente'
            return APIViewModel.update(Vendor, VendorSerializer, id, data, description, error_description)

        except Exception as e:
            return Response({'error': 'Erro inesperado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        description = 'Deletado com sucesso'
        error_description = 'Fornecedor não encontrado'
        return APIViewModel.delete(Vendor, id, description, error_description)
