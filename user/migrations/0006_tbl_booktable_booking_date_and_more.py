# Generated by Django 5.1.3 on 2024-11-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_tbl_booktable_foodtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_booktable',
            name='booking_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tbl_booktable',
            name='bookingdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tbl_booktable',
            name='bookingtime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tbl_booktable',
            name='people',
            field=models.IntegerField(null=True),
        ),
    ]
