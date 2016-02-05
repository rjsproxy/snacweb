from .base import *

DEBUG = False

# Request HTTP strict-transport-security for 7 days.
#SECURE_HSTS_SECONDS = 604800
# setting to 5 mins initially.
#SECURE_HSTS_SECONDS = 300

# Adds the includeSubDomains tag to HSTS header.
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Set "X-Content-Type-Options: nosniff" header on all responses.
SECURE_CONTENT_TYPE_NOSNIFF = True

# Set "X-XSS-Protection: 1; mode=block" header on all responses.
SECURE_BROWSER_XSS_FILTER = True

# Redirect all non-HTTPS requests to HTTPS.  Apache will do this.
SECURE_SSL_REDIRECT = True

# Request browser send cookie under HTTPS.
SESSION_COOKIE_SECURE = True

# Request browser send cookie under HTTPS.
CSRF_COOKIE_SECURE = True

# Use HttpOnly flag on the CSRF cookie.
CSRF_COOKIE_HTTPONLY = True

# Block the resource from loading in a frame.
X_FRAME_OPTIONS = 'DENY'

# Expire session when browser closes.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
