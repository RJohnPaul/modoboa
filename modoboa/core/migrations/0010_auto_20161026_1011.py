# Generated by Django 1.9.5 on 2016-10-26 08:11
from django.db import migrations, models


def set_parameter(store, parameter):
    """Add parameter to the specified store."""
    app, name = parameter.name.split(".")
    if app not in store:
        store[app] = {}
    # decode value
    value = parameter.value.decode("unicode_escape")
    if value == "yes":
        value = True
    elif value == "no":
        value = False
    elif value.isdigit():
        value = int(value)
    store[app][name.lower()] = value


def move_parameters(apps, schema_editor):
    """Move global and user parameters."""
    Parameter = apps.get_model("lib", "Parameter")
    LocalConfig = apps.get_model("core", "LocalConfig")
    parameters = {}
    for parameter in Parameter.objects.all():
        set_parameter(parameters, parameter)
    LocalConfig.objects.all().update(_parameters=parameters)

    User = apps.get_model("core", "User")
    for user in User.objects.prefetch_related("userparameter_set"):
        for parameter in user.userparameter_set.all():
            set_parameter(user._parameters, parameter)
        user.save()


def clear_parameters(apps, schema_editor):
    """Reverse operation."""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20161026_1003'),
        ('lib', '0005_auto_20160416_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='localconfig',
            name='_parameters',
            field=models.JSONField(default=dict),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='_parameters',
            field=models.JSONField(default=dict),
            preserve_default=False,
        ),
        migrations.RunPython(move_parameters, clear_parameters)
    ]
