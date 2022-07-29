import ctypes, requests
from threading import Thread

threadc = 250

useridz = open('userids.txt','r',errors='ignore').read().splitlines()
total = len(useridz)

done = 0
output = []

def thread():
    global done
    while useridz:
        userids = useridz.pop(0)
        try:
            r = requests.get(f'https://www.roblox.com/users/{userids}').url
            if 'www.roblox.com/users/' in r:
                userid = r.split('/')[-2]
                name = requests.get(f'https://users.roblox.com/v1/users/{userid}').json()['name'].split(',')[0]
                output.append(f'{name}\n')
            done += 1
        except:
            useridz.append(userids)

print(f'Starting {threadc} threads.')
for i in range(threadc):
    Thread(target=thread).start()

while 1:
    finished = done
    ctypes.windll.kernel32.SetConsoleTitleW(f'Last Online Scraper | Done: {finished}/{total}')
    if finished == total: break

with open('out.txt','w',errors='ignore') as f:
    f.writelines(output)

input('Finished.')
