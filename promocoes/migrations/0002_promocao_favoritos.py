# Generated by Django 3.1.3 on 2020-12-04 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promocoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocao',
            name='favoritos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='promocoes.promocao'),
        ),
    ]
