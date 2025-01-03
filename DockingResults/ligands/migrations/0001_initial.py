# Generated by Django 5.1.4 on 2024-12-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ligand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='ligand_images/')),
                ('analysis', models.ImageField(upload_to='ligand_analyses/')),
                ('description', models.TextField()),
                ('pdb_file', models.FileField(upload_to='ligand_pdb_files/')),
                ('report', models.FileField(upload_to='ligand_reports/')),
            ],
        ),
    ]
