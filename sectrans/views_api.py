from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video, Empresa, Modelo_Equipamento, Carro
from .serializers import VideoSerializers
from django.http import JsonResponse

class VideoRegister(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VideoSerializers(data=request.data)
        if serializer.is_valid():
            video = serializer.save()
            return Response({
                'message': 'Video salvo com sucesso',
                'video_id': video.id
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': "Video já cadastrado",
            'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
class ListarEmpresas(APIView):
    def get(self, request):
        empresas = Empresa.objects.all().order_by('nome').values('id', 'nome')
        return JsonResponse(list(empresas), safe=False)

class ListarModelosEquipamento(APIView):
    def get(self, request):
        modelos = Modelo_Equipamento.objects.all().order_by('modelo').values('id', 'modelo')
        return JsonResponse(list(modelos), safe=False)
    
class ListarCarrosByEmpresaId(APIView):
    def get(self, request, empresa_id):
        carros = Carro.objects.filter(empresa_id=empresa_id).values('id', 'nome')
        return JsonResponse(list(carros), safe=False)