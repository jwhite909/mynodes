from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import Edge, Node, Vizualisation

class EdgeResource(resources.ModelResource):
    src = fields.Field(
    column_name='src',
    attribute='src',
    widget=ForeignKeyWidget(Node, 'ip'))

    dest = fields.Field(
    column_name='dest',
    attribute='dest',
    widget=ForeignKeyWidget(Node, 'ip'))


    class Meta:
        model = Edge

class EdgeAdmin(ImportExportModelAdmin):
    resource_class = EdgeResource

class NodeResource(resources.ModelResource):

    class Meta:
        model = Node

class NodeAdmin(ImportExportModelAdmin):
    resource_class = NodeResource

admin.site.register(Edge, EdgeAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Vizualisation)