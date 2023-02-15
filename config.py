PORT = 3000

# name -> secret (32 hex chars)
USERS = {
	"tg":  "e210ca2a26d3d81670ed32899525445b",
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
	#"tls": True
	"tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
# TLS_DOMAIN = "www.google.com"
TLS_DOMAIN = "blog.cloudflare.com"
#PROXY_PROTOCOL = True

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"


METRICS_PORT = 18999
METRICS_WHITELIST = ["127.0.0.1"]
METRICS_EXPORT_LINKS = True