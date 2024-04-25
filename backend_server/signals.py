from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import warehouse, acc_details


# Every time a new user is created in warehouse model (where the request is sent to), 
# the email and username values are passed there too. Those will not de editable so can be sent once.
@receiver(post_save, sender=warehouse)
def create_table2_entry(sender, instance, created, **kwargs):
    if created:
        acc_details.objects.create(
            email=instance.email,
            username=instance.username,
        )

# when we terminate the account, the details are deleted in the warehouse table, as well as from the acc_details table or any table
# that we want to add in the future
@receiver(post_delete, sender=warehouse)
def delete_table2_entry(sender, instance, **kwargs):
    try:
        acc_detail_object = acc_details.objects.get(email=instance.email)
        acc_detail_object.delete()
    except acc_detail_object.DoesNotExist:
        pass

# maybe a signal will need to be created here too for Account DELETE, to dlete all instances of that user
# across all tables .