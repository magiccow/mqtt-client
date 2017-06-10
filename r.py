import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt.thingspeak.com",1883,60)

channelId = "285697"         # Put your channel ID here,i.e.. the number from the URL, https://thingspeak.com/channels/285697
apiKey = "ZJJKFJNYVRQWJRFD"  # Put the API key here (the Write API Key from the API Keys tab in ThingSpeak)

client.publish("channels/%s/publish/%s" % (channelId,apiKey), "field1=26&field2=1013")
client.loop(2)


