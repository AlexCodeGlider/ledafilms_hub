from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Contracts, Windows, Titles
from .serializers import ContractSerializer, WindowSerializer, TitleSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contracts.objects.order_by('-creation_date')
    serializer_class = ContractSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = [
        'contract_code',
        'licensor',
        'distributor',
        'additional_terms',
        'windows__title__name',
        'windows__title__aka_1',
        'windows__title__aka_2',
    ]
    filterset_fields = {
        'contract_type': ['exact'],
        'status': ['exact'],
        'deal_status': ['exact'],
        'deal_type': ['exact'],
        'creation_date': ['exact', 'lt', 'gt'],
        'fully_executed': ['exact', 'lt', 'gt'],
        'mg': ['exact', 'lt', 'gt'],
    }


class WindowViewSet(viewsets.ModelViewSet):
    queryset = Windows.objects.all()
    serializer_class = WindowSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitleSerializer
