import os
from datetime import timedelta


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

if cors_origins := os.getenv('CORS_ALLOWED_ORIGINS'):
    CORS_ALLOWED_ORIGINS = [
        origin.strip() for origin in cors_origins.split(',')
    ]
else:
    CORS_ALLOWED_ORIGINS = []

CORS_ALLOWED_ORIGIN_REGEXES = [
    r'^http://localhost(:[0-9]+)?',
]

SPECTACULAR_SETTINGS = {
    "TITLE": "{{cookiecutter.project_slug}} API",
    "DESCRIPTION": "Documentation of API endpoints of {{cookiecutter.project_slug}}",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ("rest_framework.permissions.IsAdminUser",),
    "SERVERS": [
        {
            "url": "http://127.0.0.1:8000",
            "description": "Local Development server",
        },
        {
            "url": "https://example.com",
            "description": "Production server",
        },
    ],
}

SIMPLE_JWT = {
    'ROTATE_REFRESH_TOKENS': True,
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=600),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('JWT',),
}
