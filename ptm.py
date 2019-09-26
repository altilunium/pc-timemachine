import os,sys,time
from sortedcontainers import SortedDict



class filetime:
	def __init__(self,path,epoch):
		self.path = path
		self.epoch = epoch
		timestruct = time.gmtime(epoch)
		self.year = timestruct.tm_year
		self.month = timestruct.tm_mon
		self.day = timestruct.tm_mday
		self.hour = timestruct.tm_hour
		self.min = timestruct.tm_sec
		

def decodeName(name):
	if type(name) == str:
		try:
			name = name.decode('utf8')
			print name
		except:
			print name
			name = name.decode('utf-16')
	return name

def convertToTime(epoch):
	timestruct = time.gmtime(epoch)
	year = str(timestruct.tm_year)
	month = str(timestruct.tm_mon)
	day = str(timestruct.tm_mday)
	hour = str(timestruct.tm_hour)
	minutes = str(timestruct.tm_sec)
	return day+"-"+month+"-"+year+" ("+hour+":"+minutes+")"


print sys.getdefaultencoding()
print sys.getfilesystemencoding()
walk_dir = "D://"
listofFile = []
filetime_o = SortedDict()
nfile = 0
for root,subdirs,files in os.walk(str(walk_dir)):
	for filename in files:
		file_path = os.path.join(root,filename)
		#print file_path
		try:
			time_struct =  time.localtime(os.path.getctime(file_path))
			filetime_o[os.path.getctime(file_path)] = file_path
			nfile = nfile + 1
		except:
			print file_path


for i in filetime_o:
	print convertToTime(i) +" : " + filetime_o[i]
