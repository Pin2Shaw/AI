from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

user= "9ef80d52-30b9-4e45-833a-75059db0825c-bluemix"
password= "79d7c792bb13072da32aecc7dc3777e28780d6d11619795d54d717d2abbd62e5"
host= "9ef80d52-30b9-4e45-833a-75059db0825c-bluemix.cloudant.com"
url = 'https://' + host
client = Cloudant(user, password, url=url, connect=True)
client.connect()
print("***************** Connection Done *********************")
db = client['nwaveoutput']
doc = db['nwave'] 
result_collection = Result(db.all_docs)
print ("Retrieved minimal document:\n{0}\n".format(result_collection[0]))

print ("#### END ####")
