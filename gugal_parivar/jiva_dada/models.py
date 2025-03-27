from django.db import models

class Son_of_jivadada(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Son_of_dada(models.Model):
    son_of_jivadada = models.ForeignKey(Son_of_jivadada,on_delete=models.CASCADE)
    dada_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dada_name

class Son_of_uncle(models.Model):
    son_of_dada = models.ForeignKey(Son_of_dada,on_delete=models.CASCADE)    
    uncle_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.uncle_name

