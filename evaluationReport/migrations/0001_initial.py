# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('certification', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characteristic', models.CharField(default='-', max_length=40)),
                ('coordinates', models.CharField(default='-', max_length=4)),
                ('type', models.CharField(default='-', max_length=5)),
                ('limits_type', models.CharField(default='-', max_length=20)),
                ('nominalValue', models.FloatField(default=0)),
                ('lower_limit', models.FloatField(default=0)),
                ('upper_limit', models.FloatField(default=0)),
                ('target_cpk', models.FloatField(default=0)),
                ('sample_size', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_number', models.IntegerField(default=0)),
                ('responsible', models.CharField(default='-', max_length=50)),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evaluationReport.Characteristics')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('date', models.DateField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='certification.RequiredCertificationDocuments')),
            ],
        ),
        migrations.CreateModel(
            name='GroupOfCharacteristics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default='-', max_length=50)),
                ('evaluationreport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluationReport.EvaluationReport')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evaluationReport.Evaluation')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp', models.FloatField(default=0)),
                ('cpk', models.FloatField(default=0)),
                ('average', models.FloatField(default=0)),
                ('min_value', models.FloatField(default=0)),
                ('max_value', models.FloatField(default=0)),
                ('sigma', models.FloatField(default=0)),
                ('amplitude', models.FloatField(default=0)),
                ('result', models.BooleanField(default=False)),
                ('comments', models.CharField(max_length=200, null=True)),
                ('evaluation', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='evaluationReport.Evaluation')),
            ],
        ),
        migrations.AddField(
            model_name='evaluationapproval',
            name='evaluation_result',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='evaluationReport.Results'),
        ),
        migrations.AddField(
            model_name='evaluationapproval',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.EmbracoProfile'),
        ),
        migrations.AddField(
            model_name='characteristics',
            name='evaluationreport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evaluationReport.EvaluationReport'),
        ),
        migrations.AddField(
            model_name='characteristics',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluationReport.GroupOfCharacteristics'),
        ),
    ]
