from django.contrib import admin
from .models import Author  # Import the model from models.py


class AuthorAdmin(admin.ModelAdmin):  # Use a relevant name
    list_display = ('name', 'email', 'age', 'created_at', 'updated_at')  
    search_fields = ('name', 'email')  
    list_filter = ('created_at',)  

admin.site.register(Author, AuthorAdmin)




