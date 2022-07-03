
import json
from pmHelpers import *

# *** FROM CLI ***
# create a text file with a list of mullvad servers i.e. mullvad relay list >> data/vpns.txt


# save the text file to a python list
currentVpnList = []
with open('data/vpns.txt') as f:
	for content in f:
		currentVpnList.append(content)





# create json structured data from the python list of server data
def createVpnDict(vpnList):
	outputList = []

	for vpn in vpnList[0:]:

		newCountry = vpn[0].isalpha()
		try:    newCity = vpn[4].isalpha()
		except: newCity = None
		try:
			if "(rented)" in vpn or "(owned)" in vpn:
				newServer = True
			else:
				newServer = False
		except:
			newServer = None

		if newCountry == True:
			countryDict = {}
			cityList, serverList = [], []

			print("\nCountry: " + str(vpn))

			vpnCountry = vpn.split(' (')[0]
			vpnCodeSplit = vpn.split(' (')[1]
			vpnCode = vpnCodeSplit.split(')')[0]
			if vpnCountry not in outputList:
				countryDict.update({'countryName': vpnCountry})
				countryDict.update({'countryCode': vpnCode})


		if newCountry == False:
			cityDict = {}


			#print(vpn)

			if newCity == True:
				citySplit = vpn.split(' ')
				cityName = citySplit[0].strip()

				try:	cityCode = citySplit[1][1:][:-1]
				except:	cityCode = None


				print('\nCity: ' + str(cityName) + '\n')
				if cityName not in outputList:
					cityDict.update({'cityName': cityName})
					cityDict.update({'cityCode': cityCode})

				if cityName not in cityList:
					cityList.append(cityDict)

			if newServer == True:
				serverDict = {}
				serverSplit = vpn.split(' ')
				try:
					serverName = serverSplit[0][2:]
				except:
					serverName = None
				try:
					serverIp = serverSplit[1]
				except:
					serverIp = None
				try:
					serverProtocol = hostSplit[3]
					#print(cityCode)
				except:
					serverProtocol = None

				if serverName not in outputList:
					serverDict.update({'serverName': serverName})
					serverDict.update({'serverIp': serverIp})
					serverDict.update({'serverProtocol': serverProtocol})

				if serverDict not in serverList:
					serverList.append(serverDict)


				print("\nNew Server: " + str(serverDict))

			#print(cityList)

			countryDict.update({'cities': cityList})
			countryDict.update({'servers': serverList})

		if countryDict not in outputList:
			outputList.append(countryDict)
	


	print('\nCountries in Mullvad List: ' + str(len(outputList)))

	return outputList






finalVpnList = createVpnDict(currentVpnList)


#print('\nFunction Output')
#print(finalVpnList)



# save structured mullvad data to a json file
try:
	writeVpns = writeJson('data/vpns.json', finalVpnList)
	print(writeVpns)
except Exception as e:
	print('\nFailed to write to vpns.json')
	print(e)

