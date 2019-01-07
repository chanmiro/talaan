from django.contrib import admin
from .models import Organization, Department, Employee, DocumentType, Uom, ItemType, Item
# Register your models here.

admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(DocumentType)
admin.site.register(Uom)
admin.site.register(ItemType)
admin.site.register(Item)
