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
url = '/taserver/pages/gettask.cgi?taskname={}&nocomplete=true'
method = 'GET'

taskName = input('Enter the name of task: ')

username = 'admin'
password = 'xvmaster'

currentDirectory = os.path.dirname(__file__)
fullPath = os.path.join(currentDirectory, ipConfigFile)
file = open(fullPath) 
ipValue = file.read()

connection = HTTPConnection(ipValue, port=port)
authKey = b64encode((username+":"+password).encode('utf-8')).decode('utf-8')
headers = {"Authorization":"Basic " + authKey}
connection.request(method, url.format(taskName), headers=headers)
response = connection.getresponse()
fileContent = response.read().decode()

print("http://" + ipValue + ":" + str(port) + url.format(taskName))

print(fileContent)

fullPath = os.path.join(currentDirectory, '{}.xml'.format(taskName))
file = open(fullPath, 'w+')
fileContent = fileContent.replace('\r', '')
fileContent = fileContent.replace('TAGMAN DATA: ', '')
file.write(fileContent)
file.close()





