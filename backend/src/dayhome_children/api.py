from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from .schemas import DayHomeChildrenListSchema, DayHomeChildrenDetailSchema
from .models import DayHomeChildren

router = Router()

@router.get("", response=List[DayHomeChildrenListSchema])
def list_children(request):
    qs = DayHomeChildren.objects.all()
    return qs

@router.get("{child_id}/", response=DayHomeChildrenDetailSchema)
def get_child_details(request, child_id: int):
    obj = get_object_or_404(DayHomeChildren, id=child_id)
    return obj