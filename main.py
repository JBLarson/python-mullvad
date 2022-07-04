
import json
from pmHelpers import *


mullvadRelays = readJson('data/vpns.json')


allServers = []

for relay in mullvadRelays[0:]:


	currentServerList = relay['servers']

	for serverObj in currentServerList:

		currentCountry, currentCountryCode = relay['countryName'], relay['countryCode']

		serverDict = {'country': currentCountry, 'countryCode': currentCountryCode,
					  'city': None, 'cityCode': None,
					  'host': None, 'hostIp': None
					 }

		#print(serverObj)


		#hostName, hostIp = serverObj['hostName'], serverObj['hostIp']
		serverDict['host'], serverDict['hostIp'] = serverObj['host'], serverObj['hostIp']
		serverDict['city'], serverDict['cityCode'] = serverObj['city'], serverObj['cityCode']

		#print(serverDict)

		allServers.append(serverDict)



print('\nAll Mullvad servers')

for server in allServers:
	print(server)



print("\nMullvad currently offers: " + str(len(allServers)) + " servers in " + str(len(mullvadRelays)) + " countries")



