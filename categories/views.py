from util.APIViewModel import APIViewModel
from .models import Category
from .serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategoryList(APIView):
    def get(self, request):
        description = 'Categorias disponíveis'
        error_description = 'Não há categoria disponível'
        return APIViewModel.list_all(Category, CategorySerializer, description, error_description)

    def post(self, request):
        try:
            data = request.data
            serializer = CategorySerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            success_description = f'Criado com sucesso. Id: {
                serializer.data["id"]}'
            return Response({'description': success_description, 'data': serializer.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': 'Objeto Categoria inválido'}, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    def get(self, request, id):
        description = 'Categoria existe'
        error_description = 'Categoria não existe'
        return APIViewModel.get_one(Category, CategorySerializer, id, description, error_description)

    def put(self, request, id):
        try:
            data = request.data
            description = f'Atualizado com sucesso. Id: {id}'
            error_description = 'Objeto Categoria inexistente'
            return APIViewModel.update(Category, CategorySerializer, id, data, description, error_description)

        except Exception as e:
            return Response({'error': 'Erro inesperado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        description = 'Deletado com sucesso'
        error_description = 'Categoria não encontrado'
        return APIViewModel.delete(Category, id, description, error_description)
