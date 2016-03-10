# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('is_canceled', models.BooleanField(default=False, verbose_name='cancelado')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_person', to='crm.Person', verbose_name='contratante')),
            ],
            options={
                'verbose_name': 'contrato',
                'verbose_name_plural': 'contratos',
                'ordering': ['proposal'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('priority', models.CharField(choices=[('a1', 'Urgente'), ('a2', 'Alta'), ('a3', 'Normal'), ('a4', 'Baixa')], default='a3', max_length=2, verbose_name='prioridade')),
                ('category', models.CharField(choices=[('orc', 'orçamento'), ('cc', 'concorrência'), ('cn', 'consulta'), ('ct', 'cotação'), ('e', 'extra'), ('g', 'global'), ('p', 'particular'), ('ou', 'outros')], default='orc', max_length=4, verbose_name='categoria')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('is_entry', models.BooleanField(default=False, verbose_name='dado entrada')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_person', to='crm.Person', verbose_name='contato')),
            ],
            options={
                'verbose_name': 'entrada',
                'verbose_name_plural': 'entradas',
                'ordering': ['priority', 'created'],
            },
        ),
        migrations.CreateModel(
            name='NumLastProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_last_prop', models.PositiveIntegerField(verbose_name='número')),
            ],
            options={
                'verbose_name': 'número último orçamento',
                'verbose_name_plural': 'número último orçamento',
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('num_prop', models.PositiveIntegerField(verbose_name='número')),
                ('prop_type', models.CharField(choices=[('R', 'R'), ('OP', 'OP')], default='R', max_length=20, verbose_name='tipo de orçamento')),
                ('num_prop_type', models.PositiveIntegerField(default=0, verbose_name='número da revisão')),
                ('category', models.CharField(choices=[('orc', 'orçamento'), ('cc', 'concorrência'), ('cn', 'consulta'), ('ct', 'cotação'), ('e', 'extra'), ('g', 'global'), ('p', 'particular'), ('ou', 'outros')], default='or', max_length=4, verbose_name='categoria')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('status', models.CharField(choices=[('c', 'cancelado'), ('elab', 'em elaboração'), ('p', 'pendente'), ('co', 'concluido'), ('a', 'aprovado')], default='elab', max_length=4)),
                ('date_conclusion', models.DateTimeField(blank=True, null=True, verbose_name='data de conclusão')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='valor')),
                ('obs', models.TextField(blank=True, verbose_name='observação')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposal_employee', to='crm.Employee', verbose_name='orçamentista')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposal_person', to='crm.Person', verbose_name='contato')),
            ],
            options={
                'verbose_name': 'orçamento',
                'verbose_name_plural': 'orçamentos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='endereço')),
                ('complement', models.CharField(blank=True, max_length=100, verbose_name='complemento')),
                ('district', models.CharField(blank=True, max_length=100, verbose_name='bairro')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='cidade')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('name_work', models.CharField(max_length=100, unique=True, verbose_name='obra')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_person', to='crm.Person', verbose_name='contato')),
            ],
            options={
                'verbose_name': 'obra',
                'verbose_name_plural': 'obras',
                'ordering': ['name_work'],
            },
        ),
        migrations.AddField(
            model_name='proposal',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposal_work', to='proposal.Work', verbose_name='obra'),
        ),
        migrations.AddField(
            model_name='entry',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_work', to='proposal.Work', verbose_name='obra'),
        ),
        migrations.AddField(
            model_name='contract',
            name='proposal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contract_proposal', to='proposal.Proposal', verbose_name='orçamento'),
        ),
    ]
