# Generated by Django 4.1 on 2022-10-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0007_alter_abastecer_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abastecer',
            name='odometro',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Odômetro'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='odometro',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Odômetro'),
        ),
        migrations.AlterField(
            model_name='troca_oleo',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='odometro',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Odômetro'),
        ),
    ]
