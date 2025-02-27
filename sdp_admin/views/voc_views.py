from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from core.permissions import IsSdpStaff
from sdp_admin.models import Voc
from sdp_admin.serializers.voc_serializers import VocSerializer
class VocViewSet(viewsets.ModelViewSet):
    """
    voc 의견 보내는 api
    """
    queryset = Voc.objects.all()
    serializer_class=VocSerializer
    permission_classes = [IsSdpStaff]

    @swagger_auto_schema(operation_id='api_sdp_admin_voc_post')
    def create(self, request):
        customer = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=customer)
            return Response({
                'status': 'Success',
                'data': serializer.data,
                },status=status.HTTP_200_OK)
        else:
            return Response({
                    'status': 'fail',
                    'data': serializer.errors,
                }, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_id='api_sdp_admin_voc_get')
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({
            'status': 'Success',
            'data': response.data,
            },status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_id='api_sdp_admin_voc_get')
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'status': 'Success',
            'data': response.data,
            },status=status.HTTP_200_OK)
        