#  Copyright 2017 Presys Instrumentos e Sistemas Ltda.

#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

__author__ = "Renato José da Silva"
__credits__ = ["Renato José da Silva, Ricardo Lopes de Goes"]
__version__ = "1.0.0"
__maintainer__ = "Renato José da Silva"
__email__ = "renato@presys.com.br"

from http.client import HTTPConnection
from base64 import b64encode
import os

ipConfigFile = 'ip_address_config.txt'
port = 5000
url = '/taserver/pages/setinputtype.cgi?newInput={}'
method = 'GET'

print('Select the desired input:')
print('1 - Current(mA)')
print('2 - miliVoltage(mV)')
print('3 - Resistance(ohms)')
print('4 - Termocouple')
print('5 - RTD')
print('6 - Switch')
print('7 - None')

option = input('')

constructorString = ""
if option == '1':	
	constructorString = 'General:mA'
elif option == '2':
	constructorString = 'General:mV'
elif option == '3':
	numfios = input("Number of wires?")
	constructorString = "Resistance:{}".format(int(numfios) - 2)
elif option == '4':
	type = input("Themocouple type (J, K, T, B, R, S, E, N, U, L or C)?")
	scale = input("Temperature Scale (ITS-90 or IPTS-68)?")
	cjcType = input("CJC type (Internal or Manual)?")
	cjcValue = 0;
	if cjcType == 'Manual':
		cjcValue = input("CJC Value?")	
	constructorString = "ThermoCouple:TC-{}|{}:{}:{}".format(type, scale, cjcType.upper(), cjcValue)
elif option == '5':
	type = input("RTD type (Pt-100 (IEC), Pt-1000, Cu-10 or Ni-100)?")
	numberOfWires = input("Number of Wires (2, 3 or 4)?")	
	scale = input("Temperature Scale (ITS-90 or IPTS-68)?")			
	constructorString = "Thermoresistance:{}|{}:{}".format(type, scale, int(numberOfWires) - 2)	
elif option == '6':
	constructorString = "Switch"
elif option == '7':
	constructorString = "General:NO"
	
print("Constructor String: " + constructorString)

username = 'admin'
password = 'xvmaster'

currentDirectory = os.path.dirname(__file__)
fullPath = os.path.join(currentDirectory, ipConfigFile)
file = open(fullPath) 
ipValue = file.read()

connection = HTTPConnection(ipValue, port=port)
authKey = b64encode((username+":"+password).encode('utf-8')).decode('utf-8')
headers = {"Authorization":"Basic " + authKey}
connection.request(method, url.format(constructorString), headers=headers)
response = connection.getresponse()

print("http://" + ipValue + ":" + str(port) + url.format(constructorString))

print(response.read().decode())




