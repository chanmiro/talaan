from django.shortcuts import render
from .models import Organization, Department, Employee, DocumentType, Item, ItemType

# Create your views here.

def home(request):
    organizations = Organization.objects.all().order_by('-created')[:5]
    departments = Department.objects.all().order_by('-created')[:5]
    employees = Employee.objects.all().order_by('-created')[:5]
    doc_types = DocumentType.objects.all().order_by('-created')[:5]
    items = Item.objects.all().order_by('-created')[:5]
    item_types = ItemType.objects.all().order_by('-created')[:5]

    return render(request, 'masterlist/home.html', {'organizations': organizations, 'departments': departments,
                                                    'employees': employees, 'doc_types': doc_types, 'items': items,
                                                    'item_types': item_types}
    )