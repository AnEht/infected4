import os
from Crypto.Cipher import AES

# Read the encryption key from README@qjao.114514
with open(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'README@qjao.114514'), 'rb') as f:
    key = f.read()

# Decrypt files on desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
for filename in os.listdir(desktop):
    if filename.endswith('.114514'):
        try:
            with open(os.path.join(desktop, filename), 'rb') as f:
                nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            os.remove(os.path.join(desktop, filename))
            with open(os.path.join(desktop, filename[:-7]), 'wb') as f:
                f.write(data)
        except:
            pass  # Skip error

# Decrypt files on computer
for root, dirs, files in os.walk('C:\\'):
    if root.startswith(('C:\\ProgramData', 'C:\\Intel', 'C:\\WINDOWS',
                        'C:\\Program Files', 'C:\\Program Files (x86)',
                        'C:\\AppData\\Local\\Temp', 'C:\\Local Settings\\Temp')):
        continue
    for filename in files:
        if filename.endswith('.114514'):
            try:
                with open(os.path.join(root, filename), 'rb') as f:
                    nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
                cipher = AES.new(key, AES.MODE_EAX, nonce)
                data = cipher.decrypt_and_verify(ciphertext, tag)
                os.remove(os.path.join(root, filename))
                with open(os.path.join(root, filename[:-7]), 'wb') as f:
                    f.write(data)
            except:
                pass  # Skip error
