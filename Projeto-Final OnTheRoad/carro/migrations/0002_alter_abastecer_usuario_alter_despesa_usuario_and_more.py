# Generated by Django 4.1 on 2022-10-03 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abastecer',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='troca_oleo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='tipo_combustivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carro.tipocombustivel'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='veiculos', to=settings.AUTH_USER_MODEL),
        ),
    ]
