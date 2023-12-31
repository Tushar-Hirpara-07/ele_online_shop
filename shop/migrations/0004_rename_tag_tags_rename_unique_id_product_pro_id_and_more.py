# Generated by Django 4.1.6 on 2023-10-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_tag_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Tags',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='unique_id',
            new_name='Pro_ID',
        ),
        migrations.RemoveField(
            model_name='filter_price',
            name='price',
        ),
        migrations.AddField(
            model_name='filter_price',
            name='price_range',
            field=models.CharField(choices=[('1000 To 10000', '1000 To 10000'), ('10000 To 20000', '10000 To 20000'), ('20000 To 30000', '20000 To 30000'), ('30000 To 40000', '30000 To 40000'), ('40000 To 50000', '40000 To 50000')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brands',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Old', 'Old')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(choices=[('In Stock', 'In Stock'), ('Out Of Stock', 'Out Of Stock')], max_length=20),
        ),
    ]
