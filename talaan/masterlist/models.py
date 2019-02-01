import datetime
from django.db import models

# Create your models here.


class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Organization(BaseModel):

    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Department(BaseModel):

    name = models.CharField(max_length=50)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="organizations"
    )

    objects = models.Manager()

    def __str__(self):
        return self.name


class Employee(BaseModel):

    id = models.PositiveIntegerField(verbose_name="ID Number", primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="departments"
    )
    is_active = models.BooleanField(default=True)
    date_deactivated = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def get_company_name(self):
        return self.department.organization.name

    def get_company_id(self):
        return self.department.organization

    def save(self, *args, **kwargs):
        if self.date_deactivated is None and not self.is_active:
            self.date_deactivated = datetime.datetime.now()
        if self.date_deactivated is not None and self.is_active:
            self.date_deactivated = None
        super(Employee, self).save(*args, **kwargs)


class DocumentType(BaseModel):

    short_name = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_short_name(self):
        return self.short_name


class Uom(BaseModel):

    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=25)

    objects = models.Manager()

    def __str__(self):
        return self.name


class ItemType(BaseModel):

    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=35)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Item(BaseModel):

    code = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=36)
    uom = models.ForeignKey("Uom", on_delete=models.CASCADE)
    type = models.ForeignKey("ItemType", on_delete=models.CASCADE)
    organization = models.ManyToManyField(Organization, related_name="items")
    slug = models.SlugField(max_length=50, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
