#!/bin/bash


# TODO automate changing VPNs
# it may be easier to do the thinking in python and use a simple bash script that accepts parameters for country and city



# cycle between us, uk, and canada

for country in us gb ca
do
	connVpn= mullvad relay set location $country
	$connVpn || echo 'failed to execute vpn connector'

	sleep 2

	echo
	mullvad status
	echo

done
