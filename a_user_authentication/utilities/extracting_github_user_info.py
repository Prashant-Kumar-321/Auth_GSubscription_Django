from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
import json

def get_user_data(user): 
    try: 
        user_socialaccount  = SocialAccount.objects.get(user=user, provider='github')
        extra_data = user_socialaccount.extra_data # Contains All Fetched data 
        pretty_json = json.dumps(extra_data, indent=4, sort_keys=True)
        print(pretty_json)

        # Retrieve all userful user data 
        data = {}
        data['username'] = extra_data.get('login', 'unknown')
        data['email'] = extra_data.get('email', 'no email')
        data['profile_pic'] = extra_data.get('avatar_url')

        print(data)
        return data
    
    except SocialAccount.DoesNotExist:
        print(f"There is no github data available for the {user.username}") 
        return None

