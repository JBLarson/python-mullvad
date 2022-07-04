
import json
from pmHelpers import *
from datetime import datetime, date
from time import strftime, sleep
import os






time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")




# rebuild fetchServers.py at the beginning of this script

# or

# use OS library to automatically create / update mullvad.json



mullvadRelays = readJson('data/mullvad.json')






def createServerList(mullvadRelayList):

	allServers = []
	cityDict, countryDict = {}, {}
	cityList, countryList = [], []
	cityCount, countryCount = 0, 0




	for relay in mullvadRelayList:
		currentServerList = relay['servers']

		for serverObj in currentServerList:

			currentCountry, currentCountryCode = relay['countryName'], relay['countryCode']
			currentCity, currentCityCode = serverObj['city'], serverObj['cityCode']
			
			if currentCountry not in countryList:
				countryCount += 1
				countryList.append(currentCountry)
			

			if currentCountry not in countryDict:
				countryDict.update({currentCountry: 1})
			elif currentCountry in countryDict:
				countryDict[currentCountry] += 1


			if currentCity not in cityDict:
				cityDict.update({currentCity: 1})
			elif currentCity in cityDict:
				cityDict[currentCity] += 1




			serverDict = {'country': currentCountry, 'countryCode': currentCountryCode,
						  'city': None, 'cityCode': None,
						  'host': None, 'hostIp': None
						 }

			serverDict['host'], serverDict['hostIp'] = serverObj['host'], serverObj['hostIp']
			serverDict['city'], serverDict['cityCode'] = serverObj['city'], serverObj['cityCode']


			if serverObj['city'] not in cityList:
				cityCount += 1
				cityList.append(serverObj['city'])




			allServers.append(serverDict)

	serverListOutput = {'allServers': allServers,
						'countries': countryCount,
						'cities': cityCount,
						'countryDict': countryDict,
						'cityDict': cityDict
						}


	return serverListOutput


mvServers = createServerList(mullvadRelays)








countryDict = mvServers['countryDict']
preSortCountries = sorted(countryDict.items(), key=lambda x:x[1], reverse=True)
sortedCountries = dict(preSortCountries)
sortedCountryList = list(sortedCountries.keys())





cityDict = mvServers['cityDict']
preSortCountries = sorted(cityDict.items(), key=lambda x:x[1], reverse=True)
sortedCountries = dict(preSortCountries)
sortedCityList = list(sortedCountries.keys())









#print('\nFunction Output')
#for server in mvServers:	print(server)




print('\n------------------------')
print('------------------------')
print('  Python-Mullvad v0.1')
print('------------------------')
print('------------------------\n')

print("Updated data at: " + str(justTime) + " on: " + str(justDate) + "\n")

print('Active Servers: ' + str(len(mvServers['allServers'])))
print('Active Countries: ' + str(mvServers['countries']))
print('Active Cities: ' + str(mvServers['cities']))


print('\n--------------------')
print('Country Stats')
print('--------------------\n')

for country in sortedCountryList[:9]:
	currentCountryCount = countryDict[country]
	print(country + "  " + str(currentCountryCount))


print('\n--------------------')
print('City Stats')
print('--------------------\n')

for city in sortedCityList[:9]:
	currentCityCount = cityDict[city]
	print(city + "  " + str(currentCityCount))




print('\n--------------------')
print('Individual Stats')
print('--------------------\n')



statusRn = mullvadStatus()
print('\nMullvad Connection Status')
print(statusRn)






time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
#print("\nCompleted script on: " + str(justDate) + " at: " + str(justTime) + "\n")



print('\n')
