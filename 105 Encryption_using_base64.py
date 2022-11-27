import base64
message=input("Enter a message:")
message_bytes=message.encode('ascii')
base64_bytes=base64.b64encode(message_bytes)
base64_message=base64_bytes.decode('ascii')
print(base64_message)

#decode
base64_bytes=base64_message.encode('ascii')
message_bytes=base64.b64decode(base64_bytes)
message=message_bytes.decode('ascii')
print("Decoded message is: ",message)