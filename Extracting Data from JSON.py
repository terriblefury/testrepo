import urllib.request, urllib.parse, urllib.error
import json
import ssl
counts=0
sum=0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')


info=json.loads(data)


comments=info['comments']

for item in comments:
    counts=counts+1

    number=item['count']
    sum=sum+int(number)

print('Count:',counts)
print('Sum:',sum)
