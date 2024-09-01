from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Base64 strings of the key and IV
base64_key = "dF3luZxgMqMjdv26DTzAZqhRHyQsLOiQCajdl6IapdE="
base64_iv = "Yf1YXfocPY/iDTpVUsfklA=="

# Read the encrypted file
with open('flag.enc', 'rb') as enc_file:
    encrypted_data = enc_file.read()

# Decode the Base64-encoded key and IV
key = base64.b64decode(base64_key)
iv = base64.b64decode(base64_iv)

# Create the AES cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the data
decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

# Save the decrypted data to a file
with open('flag.jpg', 'wb') as dec_file:
    dec_file.write(decrypted_data)

print("flag.jpg has been saved.")
