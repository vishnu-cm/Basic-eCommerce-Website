# Generated by Django 4.0 on 2022-02-02 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customercheckout_customerpayedproducts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerpayedproducts',
            name='checkout_details',
        ),
        migrations.RemoveField(
            model_name='customerpayedproducts',
            name='customer',
        ),
        migrations.DeleteModel(
            name='CustomerCheckout',
        ),
        migrations.DeleteModel(
            name='customerPayedProducts',
        ),
    ]