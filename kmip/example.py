from kmip.pie.client import ProxyKmipClient

client = ProxyKmipClient(
    hostname='172.21.0.1',
    port=5696,
    cert='/etc/pykmip/certs/server.crt',
    key='/etc/pykmip/certs/server.key',
    ca='/etc/pykmip/certs/server.crt',
    ssl_version='PROTOCOL_SSLv23',
    username='user',
    password='password',
    config='client'
)
