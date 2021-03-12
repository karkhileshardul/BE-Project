import cognitive_face as CF
from global_variables import personGroupId
import sys


#BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0'
#CF.BaseUrl.set(BASE_URL)
#Key = '9747107c8dd844dd97f909ea9aae4587'
#CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)
Key = '2c9ae23bb71242cca1eb17e10322fc6a'
CF.Key.set(Key)
#CF.person.lists(personGroupId)

personGroups = CF.person_group.lists()
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print (personGroupId + "already exists.")
        sys.exit()

res = CF.person_group.create(personGroupId)

print (res)

