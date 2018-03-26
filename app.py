from cloudant import cloudant 

user= "9ef80d52-30b9-4e45-833a-75059db0825c-bluemix"
password= "79d7c792bb13072da32aecc7dc3777e28780d6d11619795d54d717d2abbd62e5"
host= "9ef80d52-30b9-4e45-833a-75059db0825c-bluemix.cloudant.com"
url = 'https://' + host
client = Cloudant(user, password, url=url, connect=True)   

print("*****************")
print ("Gunalan")
