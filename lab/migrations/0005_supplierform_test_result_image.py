# Generated by Django 4.2.3 on 2023-07-09 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_remove_user_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierform',
            name='test_result_image',
            field=models.ImageField(blank=True, upload_to='result/'),
        ),
    ]
