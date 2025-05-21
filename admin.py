from django.contrib import admin
from .models import PostModel


class PostAdmin(admin.ModelAdmin):
    list_display=['name', 'surname', 'age', 'faculty'] #listde nelerin olacagin gosterir
    list_display_links=['name','surname'] #listde neyin link sekilde olmasini gosterir
    list_editable=['age'] #listde neyin edit oluna bilmesin gosterir
    list_filter=['age'] #filterleyir
    readonly_fields=['faculty'] #listde neyin redakte oluna bilmeyeceyin gosterir
    list_per_page= 2 # sehife basi nece obyektin olmasini mueyyenlesdirir
    search_fields=['faculty'] #ne uzre axtarisin olmasini gosterir

    fieldsets=(
        (    'Main part',{
            'fields': ('name','surname')
        }
        ),
        (
            'Second part',{
                'fields': ('age','faculty')
            }
        )
    )


admin.site.register(PostModel,PostAdmin)