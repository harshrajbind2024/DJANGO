from django.contrib import admin
from .models import rajReview,rajvarity,rajCertificate, store
#add
from .models import rajvarity

# Register your models here.
# admin.site.register(rajvarity) #add

class rajReviewInline(admin.TabularInline):
    model=rajReview
    extra=2


class  rajvarityAdmin(admin.ModelAdmin):
    list_display=('name','type', 'date_added') 
    inlines=[rajReviewInline]   

class storeAdmin(admin.ModelAdmin):
    list_display=('location', 'name')
    filter_horizontal=('raj_varieties',)
    
class ceritificateAdimin(admin.ModelAdmin):
    list_display=('raj','certificate_number')
    


admin.site.register(rajvarity, rajvarityAdmin) #add
admin.site.register(store, storeAdmin) #add
admin.site.register(rajCertificate, ceritificateAdimin) #add    