
from time import strftime, sleep
import subprocess
import json





def mullvadStatus():

	statusDict = {}
	dtRn = str(strftime("%x") + " " + strftime("%X"))
	statusDict.update({'dt': dtRn})

	# check mullvad vpn status
	# returns bytes-like object but that's not problem
	b_mvResponse = subprocess.check_output(['mullvad', 'status'])

	encoding = 'utf-8'
	mvResponse = b_mvResponse.decode(encoding)
	mvRezSplit = mvResponse.split(' ')
	country = mvRezSplit[5].replace('\n', '')
	city = mvRezSplit[4].replace(',', '')
	#print(mvRezSplit)

	if 'Connected' in mvRezSplit[0]:
		statusDict.update({'connected': True})
		statusDict.update({'host': mvRezSplit[2]})
		statusDict.update({'country': country})
		statusDict.update({'city': city})

	else:
		statusDict.update({'connected': False})
		statusDict.update({'errorMsg': mvResponse})


	return statusDict








def writeJson(jsonOutAddr, jsonData):
	try:
		with open(jsonOutAddr, 'w') as fp1: json.dump(jsonData, fp1)
		functionOutput = ("\nSuccess Creating JSON at: " + str(jsonOutAddr) + "\n")

	except Exception as e:
		functionOutput = "\nFailed to create JSON. Error msg:\n" + str(e)

	return functionOutput



def readJson(jsonInAddr):
	with open(jsonInAddr, 'r') as r:
		jsonOutputDict = json.load(r)
	return jsonOutputDict






