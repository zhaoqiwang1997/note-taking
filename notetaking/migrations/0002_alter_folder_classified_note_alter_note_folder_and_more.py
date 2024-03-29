# Generated by Django 4.1.7 on 2023-04-22 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notetaking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='classified_note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='folders', to='notetaking.note'),
        ),
        migrations.AlterField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notes_in_folder', to='notetaking.folder'),
        ),
        migrations.AlterField(
            model_name='note',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notes_in_tag', to='notetaking.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='featured_note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags', to='notetaking.note'),
        ),
    ]
