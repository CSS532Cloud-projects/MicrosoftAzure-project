import random
import json
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "myConnectionString"

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
client.connect()

random_numbers = [random.randint(1, 100) for _ in range(random.randint(2, 20))]

new_data_structure = [{"data": random_numbers}]

message_content = json.dumps(new_data_structure)
message = Message(message_content)

print(f"Sending: {message_content}")
client.send_message(message)
print("Message sent")

client.disconnect()
print("Device disconnected.")