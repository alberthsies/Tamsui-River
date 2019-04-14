# Generated by Django 2.2 on 2019-04-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='certificate',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='origin',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='password',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='product',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='company',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='farmer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='item',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='company',
            table=None,
        ),
        migrations.AlterModelTable(
            name='farmer',
            table=None,
        ),
        migrations.AlterModelTable(
            name='request',
            table=None,
        ),
    ]
