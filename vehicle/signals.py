# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import History

@receiver(post_save, sender=History)  # Replace with your actual model
def history_post_save(sender, instance, created, **kwargs):
    if created:
        # Code to run when a new instance is created
        instance.slot_cost = instance.slot.cost
        instance.save()

    # else:
    #     # Code to run when an existing instance is updated
    #     print(f"{sender.__name__} instance updated with id: {instance.id}")
