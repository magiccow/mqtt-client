
r.py is an example of a simple MQTT client suitable to send sensor data
from a Python-based IoT device (e.g. Raspberry Pi or Orange Pi) to a MQTT-based cloud service, like ThingSpeak (https://thingspeak.com/)

This example uses the Paho library to access MQTT from Python

On Armbian 5.25 (for the Orange Pi) I had to load a couple of extra Python modules beyond the default install:

pip install setuptools
pip install paho-mqtt


The main things to get right with ThingSpeak are:

1. The URI of the server: mqtt.thinspeak.com
2. The URI in your Publish request:  channel/{channel-id}/publish/{api-key}, where the channel-id and api-key you have to get from your ThingSpeak account.
3. Parameters you set up in your channel settings (field1, field2 etc) are put into the data payload of your MQTT message, and are joined with '&', like the parameters of an HTTP message, e.g. field1=2&field2=6

The channel example I used in the YouTube video (https://youtu.be/yRtc_UKuJuU) can be found here:

https://thingspeak.com/channels/285697/


