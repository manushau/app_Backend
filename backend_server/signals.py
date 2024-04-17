from django.db.models.signals import post_save
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

# maybe a signal will need to be created here too for Account DELETE, to dlete all instances of that user
# across all tables .