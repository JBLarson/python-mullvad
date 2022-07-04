
import json
from pmHelpers import *
import os


# *** FROM CLI ***
# create a text file with a list of mullvad servers i.e. 


bashServerCommand = 'mullvad relay list >> data/mullvad.txt'

os.system(bashServerCommand)



# save the text file to a python list
currentVpnList = []
with open('data/mullvad.txt') as f:
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
			serverList = []

			print("\nCountry: " + str(vpn))

			vpnCountry = vpn.split(' (')[0]
			vpnCodeSplit = vpn.split(' (')[1]
			vpnCode = vpnCodeSplit.split(')')[0]
			if vpnCountry not in outputList:
				countryDict.update({'countryName': vpnCountry})
				countryDict.update({'countryCode': vpnCode})


		if newCountry == False:
			if newCity == True:
				citySplit = vpn.split(' ')
				cityName0 = citySplit[0].strip()
				cityName = cityName0.replace(',', '')

				try:	cityCode = citySplit[1][1:][:-1]
				except:	cityCode = None


				#print('\nCity: ' + str(cityName) + '\n')


			if newServer == True:
				serverDict = {}
				serverSplit = vpn.split(' ')
				try:
					serverName = serverSplit[0][2:]
				except:
					serverName = None
				try:
					serverIp0 = serverSplit[1]
					serverIp1 = serverIp0.replace('(', '')
					serverIp2 = serverIp1.replace(')', '')
					serverIp = serverIp2.replace(',', '')

				except:
					serverIp = None


				if serverName not in outputList:
					serverDict.update({'host': serverName})
					serverDict.update({'hostIp': serverIp})
					serverDict.update({'cityCode': cityCode})
					serverDict.update({'city': cityName})

				if serverDict not in serverList:
					serverList.append(serverDict)

				print("\nNew Server: " + str(serverDict))

			countryDict.update({'servers': serverList})

		if countryDict not in outputList:
			outputList.append(countryDict)
	


	print('\n' + str(len(outputList)) + ' countries in Mullvad List')

	return outputList






finalVpnList = createVpnDict(currentVpnList)


#print('\nFunction Output')
#print(finalVpnList)



# save structured mullvad data to a json file
try:
	writeVpns = writeJson('data/mullvad.json', finalVpnList)
	print(writeVpns)
except Exception as e:
	print('\nFailed to write to mullvad.json')
	print(e)

