
import random
from time import sleep
import sys
import msvcrt as m

fname = "names.txt"
pname = "prizes.txt"

def wait():
	m.getch()
def line_count(fn):
	with open(fn, 'r') as f:
		for i, l in enumerate(f):
			pass
	f.close()
	return i + 1
	
def load_things(f):
	things = []
	lines = line_count(f)
	x = 0
	with open(f, 'rb') as fn:
		while x < lines:
			things.append(fn.readline()[:-2])
			x += 1
	fn.close()
	return things

def randomizer(names,prizes):
	x = 0 
	while x < 10:
		xindex = random.randint(0,len(names) -1)
		yindex = random.randint(0,len(prizes) -1)
		print'\r>> ' + names[xindex] +' wins: ' + prizes[yindex] + '               ',
		sys.stdout.flush()
		sleep(0.1)
		x += 0.1
	print
	return [xindex,yindex]
def main():
	print(">> Loading Names...")
	sleep(0.1)
	names = load_things(fname)
	for name in names:
		print('>> ' + name + ' added')
	sleep(0.1)
	print(">> Loading Prizes...")
	prizes = load_things(pname)
	for prize in prizes:
		print('>> ' + prize + ' added')
	sleep(0.1)
  print
  print
	while len(prizes) > 0:
		print(">> Press any key to randomly select a name and a prize...")
		wait()
		poppers = randomizer(names,prizes)
		#remove names and prizes that have already won or been won.
    names.pop(poppers[0])
		prizes.pop(poppers[1])
    print

if __name__ == '__main__':
	main()
	
	
