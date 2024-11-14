from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video, Empresa, Modelo_Equipamento, Carro
from .serializers import VideoDataSerializer, VideoRequestSerializer
from django.http import JsonResponse
from django.db.models import Max
from datetime import datetime
from collections import defaultdict
from collections import defaultdict, Counter
from itertools import groupby

from .models import Video, Carro, Empresa, Servidor  # Importe os modelos relacionados

class VideoRegister(APIView):

    def is_video_registred(self, video_file, channel, carro_id, data_video):

        video_exists = Video.objects.filter(
            video_file = video_file,
            channel = channel,
            carro_id = carro_id,
            data_video = data_video
        ).exists()

        return video_exists
        

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
                    if self.is_video_registred(video_data['video_file'],
                                        video_data['channel'],
                                        carro_id,
                                        video_data['data_video']):
                        errors.append({
                        'video_data': video_data,
                        'errors': "Vídeo já registrado no banco de dados."
                            })
                        continue
                    
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
        modelos = Modelo_Equipamento.objects.all().order_by('modelo').select_related('modelo').values('id', 'modelo__modelo')
        return JsonResponse(list(modelos), safe=False)
    
class ListarCarrosByEmpresaId(APIView):
    def get(self, request, empresa_id):
        carros = Carro.objects.filter(empresa_id=empresa_id).select_related('modelo').values('id', 'nome', 'modelo')
        return JsonResponse(list(carros), safe=False)

class ListarCamsByEmpresaId(APIView):
    def get(self, request, empresa_id):
        empresa = get_object_or_404(Empresa, id=empresa_id)
    
        # Filtra os vídeos pela empresa e calcula o máximo de channel
        max_channel = Video.objects.filter(empresa=empresa).aggregate(Max('channel'))['channel__max']
        
        # Retorna o valor em JSON
        return JsonResponse({'empresa_id': empresa_id, 'max_channel': max_channel}) 

class ListarDadosRelatorioCores(APIView):
    def post(self, request):
        empresa_id = request.data.get('empresa_id')
        channel = request.data.get('channel')
        data_inicio = datetime.strptime(request.data.get('data_inicio'), "%Y-%m-%d")
        data_fim = datetime.strptime(request.data.get('data_fim'), "%Y-%m-%d")

        # Obter lista de carros com uma consulta para garantir o formato
        carros = list(Carro.objects.filter(empresa_id=empresa_id)
                      .select_related('modelo')
                      .values('id', 'nome', 'modelo__modelo'))

        # Mapeamento de IDs dos carros para nomes e modelos
        carro_info = {carro['id']: {"car": carro['nome'], "model": carro['modelo__modelo']} for carro in carros}

        # Consulta única para obter todos os vídeos filtrados
        videos = Video.objects.filter(
            empresa_id=empresa_id,
            channel=channel,
            data_video__range=[data_inicio, data_fim]
        ).values('carro_id', 'data_video')

        # Contagem dos vídeos por carro e data
        contagem_data = defaultdict(lambda: defaultdict(int))
        for video in videos:
            contagem_data[video['carro_id']][video['data_video'].strftime("%Y-%m-%d")] += 1

        # Construção do JSON final
        data = {
            "data": [
                {
                    "car": carro_info[carro_id]["car"],
                    "model": carro_info[carro_id]["model"],
                    "dates": [{"date": date, "files": count} for date, count in dates.items()]
                }
                for carro_id, dates in contagem_data.items()
            ]
        }

        return JsonResponse(data, safe=False)
