from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient
import json

# appneta login credentials
email = 'xxx@yyy.zzz'
password = 'password'

# appneta PVC shard instance
instance = 'demo'
instance_host = '%s.pathviewcloud.com' % (instance,)

http_client = RequestsClient()
http_client.set_basic_auth(instance_host, email, password)

with open('swagger.json') as f:
    spec = json.load(f)
client = SwaggerClient.from_spec(spec, 'https://%s' % (instance_host,), http_client=http_client)

# per https://demo.pathviewcloud.com/pvc-data/swagger/
print client.organization.all().result()



# note that some client generators can access the .json file directly from a URL
# however, bravado (and perhaps others) enforce presence of info=>title attribute,
# which is not present in AppNeta-hosted swagger.json and has been added to the
# version in this respository

#swagger_spec_url = 'https://%s/pvc-data/swagger.json' % (instance_host,)
#client = SwaggerClient.from_url(swagger_spec_url, http_client=http_client)
