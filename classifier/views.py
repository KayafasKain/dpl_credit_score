from rest_framework_mongoengine import viewsets
from .serializers import ScoringDataSerializer
from .models import ScoringData
from .permission import IsStaffOrReadOnly
from .classify_model import ClassifyClient
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings

class ScoringDataViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    model = ScoringData
    queryset = ScoringData.objects.all()
    serializer_class = ScoringDataSerializer
    permission_classes = (IsStaffOrReadOnly,)

    def create(self, request, *args, **kwargs):
        prepeared_data = request.data
        cls = ClassifyClient(settings.BASE_DIR + '/classifier/credit_score.pkl')
        prepeared_data['status_ml'] = cls.classify_client(prepeared_data)[0]
        print("prepeared_data['status_ml']")
        print(prepeared_data['status_ml'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return ScoringData.objects.all()