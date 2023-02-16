PORT = 3000

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00000000000000000000000000000001",
    "tg1":  "3c09c680b76ee91a4c25ad51f742267d",
    
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.cloudflare.com"
MASK_HOST="blog.cloudflare.com"
PREFER_IPV6=False

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"
USER_OPERATION_HOST="127.0.0.1"
USER_OPERATION_PORT=80

CENTER_SERVER_HOST = "143.198.133.169"
CENTER_SERVER_PORT = 9035
# MY_DOMAIN 如果用本服务器做了域名解析的话，就把这个字段设置为对应的域名
#MY_DOMAIN="test.mtproxy.cc"