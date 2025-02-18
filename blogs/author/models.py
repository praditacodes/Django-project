from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)  
    email = models.EmailField()  
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # 
 

    def __str__(self):
        return self.name  


