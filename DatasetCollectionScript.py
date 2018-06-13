import socket, traceback
import time
host = '10.42.0.1'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
activities = {1:'Push_ups',2:'Jumping_Jack',3:'Walking',4:'Crunches',5:'Squats',6:'Standing',7:'Lying'}
print('Available activities are as follows.')
for key in activities:
    print(key, activities[key])
activity = int(input('Please input index of the activity to be recorded:'))
for i in range(5,0,-1):
    print(f'Starting recording in {i}')
    time.sleep(1)
dataset = open(activities[activity]+'_'+str(time.time())+'.csv','w')
print('Collecting dataset')
while 1:
    try:
        message, address = s.recvfrom(8192)
        row = bytes.decode(message)
        row = row[:-2]  + ',' + activities[activity] + '\n'
        print(row)
        dataset.write(row)
    except (KeyboardInterrupt, SystemExit):
        #dataset.close()
        print('\nClosing dataset file.')
        raise
    except:
        traceback.print_exc()
