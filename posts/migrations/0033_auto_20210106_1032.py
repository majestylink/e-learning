# Generated by Django 3.1.4 on 2021-01-06 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0032_auto_20210105_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subcategory',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subcat', to='posts.subcat'),
        ),
    ]
