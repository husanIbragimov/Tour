# Generated by Django 4.2.14 on 2024-07-23 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_country_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Shahar', 'verbose_name_plural': 'Shaharlar'},
        ),
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.ImageField(blank=True, null=True, upload_to='flags/', verbose_name='Bayroq'),
        ),
        migrations.AlterField(
            model_name='country',
            name='image',
            field=models.ImageField(blank=True, help_text="Rasm hajmi 1700x1133 px bo'lishi kerak. Havola: https://pexels.com/", null=True, upload_to='countries/', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='country',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'parent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='common.country', verbose_name='Parent'),
        ),
    ]
