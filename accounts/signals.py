from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import *


#  Receiver function for signal

# This POST_SAVE signal example

@receiver(post_save, sender=User)  # <- one way to connect sender and receiver by 
# using decorator
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the UserProfile if not exist...
            UserProfile.objects.create(user=instance)
            
#  Second way to connect
#  post_save.connect(post_save_create_profile_receiver,sender = User)



#  Pre_save signal test.....

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass