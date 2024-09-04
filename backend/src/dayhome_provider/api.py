from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from .schemas import DayHomeProviderListSchema, DayHomeProviderDetailSchema
from .models import DayHomeProvider

router = Router()

@router.get("", response=List[DayHomeProviderListSchema])
def list_providers(request):
    qs = DayHomeProvider.objects.all()
    return qs

@router.get("{provider_id}/", response=DayHomeProviderDetailSchema)
def get_provider_details(request, provider_id: int):
    obj = get_object_or_404(DayHomeProvider, id=provider_id)
    return obj