import os
import re

def to_rename(f):
	m = re.match(r'^[0-9].*\.py$', f)
	if m is None:
		return False
	return True

l = os.listdir(".")
l2 = [f for f in l if to_rename(f)]
for f in l2:
	s = 'git mv %s %s' % (f, 'p' + f)
	os.system(s)

