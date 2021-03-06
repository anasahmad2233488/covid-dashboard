# Generated by Django 4.0 on 2022-01-09 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('rtk_ag', models.IntegerField()),
                ('pcr', models.IntegerField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state')),
            ],
        ),
        migrations.CreateModel(
            name='MySJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('checkins', models.IntegerField()),
                ('unique_ind', models.IntegerField()),
                ('unique_loc', models.IntegerField()),
                ('checkins_to_ind_ratio', models.IntegerField()),
                ('checkins_to_unique_loc_ratio', models.IntegerField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state')),
            ],
        ),
        migrations.CreateModel(
            name='Clusters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster', models.CharField(max_length=256)),
                ('date_announced', models.DateField(db_index=True)),
                ('date_last_onset', models.DateField(db_index=True)),
                ('category', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=256)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state')),
            ],
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('cases_new', models.IntegerField()),
                ('cases_import', models.IntegerField()),
                ('cases_recovered', models.IntegerField()),
                ('cases_death', models.IntegerField()),
                ('cases_active', models.IntegerField()),
                ('cases_cluster', models.IntegerField()),
                ('cases_unvax', models.IntegerField()),
                ('cases_pvax', models.IntegerField()),
                ('cases_fvax', models.IntegerField()),
                ('cases_boost', models.IntegerField()),
                ('cases_child', models.IntegerField()),
                ('cases_adolescent', models.IntegerField()),
                ('cases_adult', models.IntegerField()),
                ('cases_elderly', models.IntegerField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state')),
            ],
        ),
    ]
