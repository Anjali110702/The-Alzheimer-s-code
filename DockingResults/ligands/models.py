from django.db import models

class Ligand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ligand_images/')
    analysis = models.ImageField(upload_to='ligand_analyses/')
    description = models.TextField()
    pdb_file = models.FileField(upload_to='ligand_pdb_files/')
    report = models.FileField(upload_to='ligand_reports/')

    def __str__(self):
        return self.name
