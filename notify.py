#!/usr/bin/python
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

import paho.mqtt.client as mqtt
import json


CHANNEL="home/picam/bedroom"


def on_publish(client, userdata, result):
    print("Data published")
    pass


client = mqtt.Client()
client.on_publish = on_publish
client.connect("192.168.1.44", 1883, 60)

data = {}
client.publish(CHANNEL, data)
