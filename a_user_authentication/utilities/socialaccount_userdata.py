class RetrieveUserData:
    def __init__(self, social_account):
        self._provider = social_account.provider
        self._data = social_account.extra_data
    
    @property 
    def data(self): 
        return self._data 

    @property 
    def provider(self): 
        return self._provider

    # interface exposed to public 
    def get_user_data(self): 
        print("get user data called")
        if self.provider == "github": 
            return self._get_github_data()
        elif self.provider == "google": 
            return self._get_google_data()

    # Retrieve {email, avatar, fullname} from github social account
    def _get_github_data(self): 
        print("get github data called ")
        user_data = {}
        user_data['email'] = self.data.get('email', None)
        user_data['avatar'] = self.data.get('avatar_url', None)
        user_data['full_name'] = self.data.get('name', None)

        return user_data

    # Retrieve {email, avatar, fullname} from google social account 
    def _get_google_data(self): 
        user_data = {}
        user_data['email'] = self.data.get('email', None)
        user_data['avatar'] = self.data.get('picture', None)
        user_data['full_name'] = self.data.get('name', None)

        return user_data
