# Python-Mullvad
Unofficial CLI for the Mullvad VPN - Written with Shell Scripting and Python

1. Pipe available Mullvad relays to a .txt file with
>>mullvad relay list >> data/vpns.txt
2. Wrangle unstructured .txt data into JSON w [fetchServers.py](fetchServers.py)
3. Use this data to analyze the mullvad network, automate vpn protection, and who knows what else.
