from django.db import models

class Projet(models.Model):
    id=models.AutoField(primary_key=True)
    compagnie=models.CharField(max_length=255, null=True)
    nom=models.CharField(max_length=255, null=True)
    dateDebut=models.DateTimeField(auto_now_add=True)
    dateFin=models.DateTimeField(auto_now_add=True)
    projetNum=models.CharField(max_length=100, null=True)
    notes=models.CharField(max_length=255, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    # class Meta:
    #     managed = False
    #     db_table = 'Projet'

# Create your models here.
class FormCovid(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=255, null=True)
    compagnie=models.CharField(max_length=255, null=True)
    nom=models.CharField(max_length=255, null=True)
    dateEntre=models.DateTimeField(auto_now_add=True)
    notes=models.CharField(max_length=255, null=True)
    projet_id=models.ForeignKey(Projet, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    # class Meta:
    #     managed = False
    #     db_table = 'FormCovid'
