#!/home/pi/.venv/bin/python
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

import argparse
import json
import os
import paho.mqtt.client as mqtt

CHANNEL="home/picam/bedroom"

parser = argparse.ArgumentParser()

parser.add_argument("--file", "-f",
                    default=None,
                    help="The new image or movie filename")
parser.add_argument("--num", "-n",
                    default=None,
                    help="Number indicating file type")

parser.add_argument("--image", "-i",
                    dest='image', action='store_true',
                    default=False,
                    help="Boolean indicating this is an image file")
parser.add_argument("--movie", "-m",
                    dest='movie', action='store_true',
                    default=False,
                    help="Boolean indicating this is a movie")


def on_publish(client, userdata, result):
    print("Data published %s" % userdata)
    pass


client = mqtt.Client()
client.on_publish = on_publish
client.connect("192.168.1.44", 1883, 60)

args = parser.parse_args()
file = os.path.basename(os.path.normpath(args.file))
data = {'file_name': args.file,
        'file_type': args.num,
        'image_type': args.image,
        'movie_type': args.movie,
        'url': "http://hemna.mynetgear.com/motion/%s" % file}
event_json = json.dumps(data)
print("publishing event %s" % event_json)
client.publish(CHANNEL, event_json)
