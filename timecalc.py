import time
#import speedtest
def timeit(method):

	def timed(*args, **kw):
		# Time
		ts = time.time()
		result = method(*args, **kw)
		te = time.time()
		# Upload Speed
		# try:
		# 	s = speedtest.Speedtest()
		# 	s.get_best_server()
		# 	uspeed=s.upload()/8
		# except:
		# 	try:
		# 		s = speedtest.Speedtest()
		# 		s.get_best_server()
		# 		uspeed=s.upload()/8
		# 	except:
		# 		uspeed=0.0
		uspeed='NA'

		print(method.__name__, args, kw, te-ts,uspeed) 
		f=open("multithreading.txt","a")
		f.write(str(args[0])+","+str(te-ts)+","+str(uspeed)+"\n")
		f.close()
		return result

	return timed
