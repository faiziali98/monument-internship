from subprocess import *
from resource import *
# import psutil
import time

def mean(arr):
	return sum(arr)/len(arr)

commands = [
    'time sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
]

times = []
procs = []

# Running all the commands in subprocesses
t = time.time()
for command in commands:
	print("Running {}".format(command))
	proc = Popen(command, shell=True, stdout=DEVNULL, stderr=DEVNULL) 
	procs.append(proc)

# Running all the commands in subprocesses
for proc in procs:
	# ps = psutil.Process(proc.pid)
	#
	# I could have used psutil to get the time for individual commands when the finish
	# but somehow, it was not getting installed on the computer
	
	proc.wait()
	times.append(time.time()-t)

te = time.time()-t

print("\nTime elasped: {}".format(te))
print("Average Time: {}".format(te/len(commands)))
print("Max time: {}".format(max(times)))


#For min time we can run this

# for command in commands:
# 	t_start = time.time()
# 	proc = Popen(command, shell=True, stdout=DEVNULL, stderr=DEVNULL) 
# 	try:
# 		proc.wait()
# 		# print(getrusage(RUSAGE_CHILDREN))
# 		t_stop = time.time()
# 		times.append(t_stop-t_start)
# 	except KeyboardInterrupt:
# 		proc.terminate()
# print("Min time: {}".format(min(times)))