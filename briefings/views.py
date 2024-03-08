from util.APIViewModel import APIViewModel
from .models import Briefing
from .serializers import BriefingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BriefingList(APIView):
    def get(self, request):
        description = 'Briefings disponíveis'
        error_description = 'Não há briefing disponível'
        return APIViewModel.list_all(Briefing, BriefingSerializer, description, error_description)

    def post(self, request):
        try:
            data = request.data
            serializer = BriefingSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            success_description = f'Criado com sucesso. Id: {
                serializer.data["id"]}'
            return Response({'description': success_description, 'data': serializer.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': 'Objeto Briefing inválido'}, status=status.HTTP_400_BAD_REQUEST)


class BriefingDetail(APIView):
    def get(self, request, id):
        description = 'Briefing existe'
        error_description = 'Briefing não encontrado'
        return APIViewModel.get_one(Briefing, BriefingSerializer, id, description, error_description)

    def put(self, request, id):
        try:
            data = request.data
            description = f'Atualizado com sucesso. Id: {id}'
            error_description = 'Briefing inexistente'
            return APIViewModel.update(Briefing, BriefingSerializer, id, data, description, error_description)

        except Exception as e:
            return Response({'error': 'Erro inesperado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        description = 'Deletado com sucesso'
        error_description = 'Briefing não encontrado'
        return APIViewModel.delete(Briefing, id, description, error_description)
