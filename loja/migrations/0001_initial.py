# Generated by Django 2.2.1 on 2019-05-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=150)),
                ('cartao', models.IntegerField()),
                ('pagamento', models.CharField(choices=[('av', 'Pagamento á vista'), ('p2', 'Pagamento em 2 vezes'), ('p3', 'Pagamento em 3 vezes'), ('p4', 'Pagamento em 4 vezes'), ('p5', 'Pagamento em 5 vezes')], default='av', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('em_estoque', models.BooleanField(default=True)),
            ],
        ),
    ]
