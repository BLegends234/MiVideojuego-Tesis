from django.contrib import admin
from proud.models import usuarios,score

# Register your models here.
class usuarioAdmin(admin.ModelAdmin):
    list_display=['id','NombreUsuario','Correo','Password']

class scoreAdmin(admin.ModelAdmin):
    list_display=['id','Puntos','Usuario']


admin.site.register(usuarios,usuarioAdmin)   
admin.site.register(score, scoreAdmin)   
     
     