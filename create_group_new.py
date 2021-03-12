import cognitive_face as CF
from global_variables import personGroupId

#BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0'
#CF.BaseUrl.set(BASE_URL)
#Key = 'a7073ac5c5af4f4d9f6c1a609efc3a56'
#CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)
Key = '2c9ae23bb71242cca1eb17e10322fc6a'
CF.Key.set(Key)


res = CF.person_group.create(personGroupId)
print res
