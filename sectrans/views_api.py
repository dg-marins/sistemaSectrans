from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video, Empresa, Modelo_Equipamento, Carro
from .serializers import VideoDataSerializer, VideoRequestSerializer
from django.http import JsonResponse

from .models import Video, Carro, Empresa, Servidor  # Importe os modelos relacionados

class VideoRegister(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VideoRequestSerializer(data=request.data)
        
        if serializer.is_valid():
            # Extrai dados gerais da requisição
            carro_id = serializer.validated_data['carro']
            empresa_id = serializer.validated_data['empresa']
            servidor_id = serializer.validated_data['servidor']
            
            try:
                carro = Carro.objects.get(id=carro_id)
                empresa = Empresa.objects.get(id=empresa_id)
                servidor = Servidor.objects.get(id=servidor_id)
            except Carro.DoesNotExist:
                return Response({'error': 'Carro não encontrado'}, status=status.HTTP_400_BAD_REQUEST)
            except Empresa.DoesNotExist:
                return Response({'error': 'Empresa não encontrada'}, status=status.HTTP_400_BAD_REQUEST)
            except Servidor.DoesNotExist:
                return Response({'error': 'Servidor não encontrado'}, status=status.HTTP_400_BAD_REQUEST)

            saved_videos = []
            errors = []
            
            # Processa cada vídeo da lista
            for video_data in serializer.validated_data['videos']:
                video_serializer = VideoDataSerializer(data=video_data)
                if video_serializer.is_valid():
                    # Cria uma nova instância de Video no banco de dados
                    video = Video.objects.create(
                        carro=carro,
                        empresa=empresa,
                        servidor=servidor,
                        video_file=video_data['video_file'],
                        channel=video_data['channel'],
                        data_video=video_data['data_video'],
                        hora_video=video_data['hora_video'],
                        tamanho=video_data['tamanho'],
                        duracao=video_data['duracao'],
                        path_arquivo=video_data['path_arquivo']
                    )
                    saved_videos.append({
                        'message': 'Vídeo salvo com sucesso',
                        'video_id': video.id
                    })
                else:
                    errors.append({
                        'video_data': video_data,
                        'errors': video_serializer.errors
                    })
            
            # Retorna a resposta com vídeos salvos e erros, se houver
            return Response({
                'saved_videos': saved_videos,
                'errors': errors
            }, status=status.HTTP_201_CREATED if not errors else status.HTTP_207_MULTI_STATUS)
        
        # Caso a requisição geral esteja inválida
        return Response({
            'message': "Erro na requisição",
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

def get_rota(request, carro_id, data):
    # Aqui você buscaria os dados da rota no banco de dados
    # Este é apenas um exemplo, você precisará adaptar para sua estrutura de dados
    rota = Rota.objects.filter(carro_id=carro_id, data=data).order_by('timestamp')
    
    rota_data = [{'lat': ponto.latitude, 'lng': ponto.longitude} for ponto in rota]
    
    return JsonResponse(rota_data, safe=False)