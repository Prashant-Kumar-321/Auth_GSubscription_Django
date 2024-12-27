from allauth.account.signals import user_signed_up, user_logged_in
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

from .utilities.socialaccount_userdata import RetrieveUserData

@receiver(user_signed_up)
def update_user_profile(request, user, **kwargs):
    user = User.objects.get(username=user)
    
    # check if sign up process took place using social account 
    social_account = SocialAccount.objects.filter(user=user).first()
    if social_account: 
        # Social account signup 
        retrieve_data = RetrieveUserData(social_account)
        user_data = retrieve_data.get_user_data()
        
        # save profile 
        profile = Profile(user=user, avatar=user_data['avatar'], email=user_data['email'], full_name=user_data['full_name'])
        profile.save()
        print(f"User Signed Up using {social_account.provider}: provider")
        ... 

    # Not social account 
    else: 
        print("{user.username} signed up using email and password")
        Profile.objects.create(user=user)

    print("A new user signed up in the application")



@receiver(user_logged_in)
def user_loged_in(request, user, **kwargs): 
    username = user 
    print("A new user loged in ") 
    