import requests, time
r = requests.post('http://requestbin.fullcontact.com/sfegltsf', data={"ts":time.time()})

# r = requests.get('http://requestbin.fullcontact.com/sfegltsf')
# r = requests.get('http://ec2-34-220-183-172.us-west-2.compute.amazonaws.com/11qb8y91')

print(r.status_code)
print(r.content)
