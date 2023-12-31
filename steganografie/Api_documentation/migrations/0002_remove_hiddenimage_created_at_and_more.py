# Generated by Django 4.2.2 on 2023-06-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_documentation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hiddenimage',
            name='created_at',
        ),
        migrations.AddField(
            model_name='hiddenimage',
            name='encrypted_image_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hiddenimage',
            name='num_encrypted_images',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hiddenimage',
            name='image',
            field=models.ImageField(upload_to='hidden_images/'),
        ),
        migrations.AlterField(
            model_name='hiddenimage',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
