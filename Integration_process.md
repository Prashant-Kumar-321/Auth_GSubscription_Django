# Process to integrate social-account Authentication using ***django-allauth***

1. Install ```django-allauth``` package
```python
    pip install django-allauth

    for social account integration

    pip install "django-allauth[socialaccount]"
```

2. ***Configuring*** ```settings.py```

    A. Specify the ```Context Processors```
    ```python 

    # Specify the context processors as follows:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...

                    # allauth needs this from django
                    'django.template.context_processors.request',
                ],
            },
        },
    ]
    ```

    B. Configuring ```Backend Authentication```
    ```python
        AUTHENTICATION_BACKENDS = [
            # Needed to login by username in Django admin, regardless of `allauth`
            'django.contrib.auth.backends.ModelBackend',

            # `allauth` specific authentication methods, such as login by email
            'allauth.account.auth_backends.AuthenticationBackend',
        ] 
    ```

    C. ```Register allauth App ```
    ```python 
    INSTALLED_APPS = [
        ...
        # The following apps are required (comes by default):
        'django.contrib.auth',
        'django.contrib.messages',

        'allauth',
        'allauth.account',

        # For Social authentication Integration
        'allauth.socialaccount',

        # Add social account specific apps 
        'allauth.socialaccount.providers.apple',
        'allauth.socialaccount.providers.facebook',
        'allauth.socialaccount.providers.github',
        'allauth.socialaccount.providers.google',
        'allauth.socialaccount.providers.linkedin',
        'allauth.socialaccount.providers.microsoft',
        'allauth.socialaccount.providers.telegram',
        'allauth.socialaccount.providers.twitter',
        ...
    ]
    ```
    [other social account provider list](https://docs.allauth.org/en/latest/installation/quickstart.html)

    D. ``` Configure Middleware ```
    ```python 
    MIDDLEWARE = [
        ...

        # Account middleware:
        'allauth.account.middleware.AccountMiddleware'
    ]
    ```

    E. Configure ```Provider specific reuirements```
    ```python 
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:

        SOCIALACCOUNT_PROVIDERS = {
            'google': {
                'APP': {
                    'client_id': '123',
                    'secret': '456',
                    'key': ''
                }
            }, 
            'github': {
                'APP': {
                    'client_id': '123',
                    'secret': 'secret_key',
                    'key': '',
                }, 
                'SCOPE': [
                    'user',
                ]
            },
        }

    ```

    E. ```Integrate``` ```allauth pre-configured urls in you projects urls.py ```

    ```a_core.urls.py```
    ```python
        urlpatterns = [
            ...
            path('accounts/', include('allauth.urls')),
            ...
        ]

    ```

3. ```Post Installation and Configuration ```
```python 
    python manage.py migrate

```


## Configuring the Environment variable in Django
1. Install ```django-environ``` module
2. Create a ```.env``` file in the project directory
3. Add key-value pairs in the .env file 
```python
    ENVIROMENT=development
    DATABSE_URL=...
    SECRET_KEY=...
    .....
```
4. Accessing enviroment variables in ```settings.py``` file
```Python 
    from environ import Env

    env = Env() 

    Env.read_env(path/to/the/env/file)

    # start accessing the enviroment varibales using env object
    ENVIRONMENT = env('ENVIRONMENT', default='production')
    .........
    .........
    .........
```
