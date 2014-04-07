from StringIO import StringIO
import sys

def suppress_printing(fn):
	def function(*args, **kwargs):
		output = StringIO()
		suppressed_stdout = sys.stdout
		sys.stdout = output
		return fn(*args, **kwargs)
	return function
def square(n):
	return n*n