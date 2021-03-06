ALLOWED_HOSTS = ['raju-blog.herokuapp.com']

DEBUG = False

CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = 'https://'
SECURE_PROXY_SSl_HEADER = ('HTTP_X_FORWARD_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1000000
SECURE_FRAME_DENY = True
