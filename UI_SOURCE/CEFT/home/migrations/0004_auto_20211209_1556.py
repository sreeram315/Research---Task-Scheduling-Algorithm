# Generated by Django 2.2 on 2021-12-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211209_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='saliencyimage',
            name='contour1_size',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='saliencyimage',
            name='contour2_size',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='saliencyimage',
            name='contour3_size',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='saliencyimage',
            name='contour4_size',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
