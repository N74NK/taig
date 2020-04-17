from fbparser import Account
from fbparser import function
from fbparser import sorting
from getpass import getpass
import os, time, random, fbparser, sys

ses = None
count = 0

D = '\033[90m'
W = '\033[1;97m'
R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
C = '\033[1;96m'
r = '\033[0;91m'
g = '\033[0;92m'
y = '\033[0;93m'
b = '\033[0;94m'
p = '\033[0;95m'
c = '\033[0;96m'
w = '\033[0;97m'

def banner():
	os.system("cls" if os.name == "nt" else "clear")
	print(f"""
{p}________________ {c} ___________{p}_____   
{p}\__    ___/  _  \ {c}\_   _____/{p}  _  \ {c}v1.0{D}dev
{p}  |    | /  /_\  \{c} |    __){p}/  /_\  \ 
{p}  |    |/    |    \{c}|     \{p}/    |    \\
{p}  |____|\____|__  /{c}\___  /{p}\____|__  /
{c}  Salis {w}   {c}     {p}\/ {c}    \/ {p}        \/ 
	""")

def hitung_proses(jumlah):
	global count
	count += 1
	hitung = str(count * 100 / jumlah)
	hitung = hitung.split(".")[0] + "." + hitung.split(".")[1][:2]
	sys.stdout.write(f"\r   ->> Process {hitung} %")
	sys.stdout.flush()

def enter(to = "home"):
	global count
	count = 0
	getpass(f"\n   {w}->> {c}Enter To Back ")
	exec(to + "()")

def confirm_execute():
	angka = random.randint(1,999)
	angka = str(angka).zfill(3)
	if input(f"   [?] type 'yes{angka}' to confirm: ") != "yes" + angka:
		print()
		print("   [!] Operation Cancelled")
		enter()
		exit()

def select(min, max, msg_error = None, teks = "->>"):
	for _ in range(7):
		try:
			pilih = int(input(f"   {w}{teks} {p}"))
			if pilih < min or pilih > max:
				raise Exception
			return pilih
		except:
			if msg_error:
				print(f"    {msg_error}")
	else:
		print(f"   {w}->> {p}Salah mulu tolol!")
		enter()
		exit()

def home():
	banner()
	print('')
	print(f"{y}   1). {w}Go To Menu")
	print(f"{y}   2). {w}Login")
	print(f"{y}   3). {w}Logout")
	print(f"{y}   0). {w}Exit\n")
	pilih = select(0,3)
	if pilih == 0:
		banner()
		print(f"{p}  ->>{w} Thanks for using our tool")
		print(f"{p}     {c} -------------------------")
		print(f"{p}     {w} Copyright: Salis Mazaya\n")
	elif pilih == 1:
		menu1()
	elif pilih == 2:
		login()
	elif pilih == 3:
		logout()

def menu1():
	global ses
	check_login()
	banner()
	if not ses.logged:
		print()
		print("   [!] You must login")
		enter()
	else:
		print(f"   {w}Login as {g}{ses.name[:22]}")
		print(f"   {w}Please use it naturally!\n")
		print(f"   {p}No. {w}Menu")
		print(f"   {c}--- ----")
		print(f"   {p}1). {w}Like")
		print(f"   {p}2). {w}React")
		print(f"   {p}3). {w}Comment")
		print(f"   {p}4). {w}Friend")
		print(f"   {p}5). {w}Other")
		print(f"   {p}0). {w}Back\n")
		pilih = select(0,5)
		if pilih == 0:
			home()
		elif pilih == 1:
			menu2()
		elif pilih == 2:
			menu3()
		elif pilih == 3:
			menu4()
		elif pilih == 4:
			menu5()
		elif pilih == 5:
			menu6()

def menu2():
	banner()
	print(f"   {p}1). {w}Spam Like in Home")
	print(f"   {p}2). {w}Spam Like in Friend Timeline")
	print(f"   {p}3). {w}Spam Like in Group")
	print(f"   {p}4). {w}Spam Like in Fanspage")
	print(f"   {p}0). {w}Back\n")
	pilih = select(0,4)
	if pilih == 0:
		menu1()
	elif pilih == 1:
		banner()
		print(f"   {p}1). {w}Spam Like in Home")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", teks = f"    {C}> {w}Limit:")
		data = dump(fbparser.like_post_home, ({"next":None}), limit = limit, show_target = False)
		for url in data:
			function.open_url(ses, url)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()
	elif pilih == 2:
		print()
		id_ = input("   [?] Id Friend: ")
		limit = select(1,500, msg_error = "min: 1, max: 500", teks = "[?] Limit:")
		data = dump(fbparser.like_post_friend, ({"id":id_}), limit = limit)
		for url in data:
			function.open_url(ses, url)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()
	elif pilih == 3:
		print()
		id_ = input("   [?] Id Group: ")
		limit = select(1,500, msg_error = "min: 1, max: 500", teks = "[?] Limit:")
		data = dump(fbparser.like_post_grup, ({"id":id_}), limit = limit)
		for url in data:
			function.open_url(ses, url)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()
	elif pilih == 4:
		print()
		id_ = input("   [?] Username Fanspage: ")
		limit = select(1,500, msg_error = "min: 1, max: 500", teks = "[?] Limit:")
		data = dump(fbparser.like_post_fanspage, ({"username":id_}), limit = limit)
		for url in data:
			function.open_url(ses, url)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()

def menu3():
	banner()
	print("   1). Spam React in Home")
	print("   2). Spam React in Friend Timeline")
	print("   3). Spam React in Group")
	print("   4). Spam React in Fanspage")
	print("   0). Back")
	pilih = select(0,4)
	print()
	if pilih == 0:
		menu1()
	
	print("   1). Love")
	print("   2). Haha")
	print("   3). Wow")
	print("   4). Sad")
	print("   5). Angry")
	type = ["love", "haha", "wow", "sad", "angry"]
	type = type[select(1,5) - 1]
	
	if pilih == 1:
		print()
		limit = select(1,500, msg_error = "min: 1, max: 500", teks = "[?] Limit:")
		data = dump(fbparser.react_post_home, ({"next":None}), limit = limit, show_target = False)
		for url in data:
			function.react(ses, url, type = type)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()
	elif pilih == 2:
		print()
		id_ = input("   [?] Id Friend: ")
		limit = select(1,500, msg_error = "min: 1, max: 500", teks = "[?] Limit:")
		data = dump(fbparser.react_post_friend, ({"id":id_}), limit = limit)
		for url in data:
			function.react(ses, url, type = type)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()
	elif pilih == 3:
		print()
		id_ = input("   [?] Id Group: ")
		limit = select(1,500, msg_error = "min: 1, max: 500", teks = "[?] Limit:")
		data = dump(fbparser.react_post_grup, ({"id":id_}), limit = limit)
		for url in data:
			function.react(ses, url, type = type)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()
	elif pilih == 4:
		print()
		id_ = input("   [?] Username Fanspage: ")
		limit = select(1,500, msg_error = "min: 1, max: 500", teks = "[?] Limit:")
		data = dump(fbparser.react_post_fanspage, ({"username":id_}), limit = limit)
		for url in data:
			function.react(ses, url, type = type)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()

def menu4():
	banner()
	print("   1). Spam Comment in Home")
	print("   2). Spam Comment in Friend Timeline")
	print("   3). Spam Comment in Group")
	print("   4). Spam Comment in Fanspage")
	print("   0). Back")
	pilih = select(0,4)
	if pilih == 0:
		menu1()
	elif pilih == 1:
		print()
		msg = input("   [?] Comment value: ")
		limit = select(1,100, msg_error = "min: 1, max: 100", teks = "[?] Limit:")
		data = dump(fbparser.comment_post_home, ({"next":None}), limit = limit, show_target = False)
		for url in data:
			function.comment(ses, url, msg)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()

	elif pilih in [2,3,4]:
		print()
		id_ = input("   [?] " + ("Id" if pilih != 4 else "Username") + " Target: ")
		msg = input("   [?] Comment value: ")
		limit = select(1,100, msg_error = "min: 1, max: 100", teks = "[?] Limit:")
		data = dump(fbparser.comment_post_friend if pilih == 2 else fbparser.comment_post_grup if pilih == 3 else fbparser.comment_post_fanspage, ({"id" if pilih != 4 else "username":id_}), limit = limit)
		for url in data:
			function.comment(ses, url, msg)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()

def menu5():
	banner()
	print("   1). Mass Accept Request")
	print("   2). Mass Reject Friend")
	print("   3). Mass Unadd (not Unfriend)")
	print("   0). Back")
	pilih = select(0,3)
	if pilih == 0:
		menu1()
	elif pilih == 1 or pilih == 2:
		print()
		limit = select(1,9999999, teks = "[?] Limit:")
		confirm_execute()
		data = dump(fbparser.friend_request, ({"next":None}), limit = limit, show_target = False)
		for url in data:
			url = url["confirm"] if pilih == 1 else url["reject"]
			function.open_url(ses, url)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()
		
	elif pilih == 3:
		print()
		limit = select(1,9999999, teks = "[?] Limit:")
		confirm_execute()
		data = dump(fbparser.friend_requested, ({"next":None}), limit = limit, show_target = False)
		for url in data:
			function.open_url(ses, url)
			hitung_proses(len(data))
		print("\n   [+] Done !!!")
		enter()
	
def menu6():
	banner()
	print("   1). Find Id Friend")
	print("   2). Find Id Group")
	print("   0). Back")
	pilih = select(0,2)
	if pilih == 0:
		menu1()
	elif pilih == 1:
		print()
		name = input("   [?] Full Name: ")
		data = fbparser.find_id_friend(ses, name)
		if None in data:
			print("   [+] Not Found !!!")
		else:
			print("   [+] Name : " + data[0][:22])
			print("   [+] ID : " + data[1])
		enter()
	elif pilih == 2:
		print()
		name = input("   [?] Group Name: ")
		data = fbparser.find_id_group(ses, name)
		if None in data:
			print("   [+] Not Found !!!")
		else:
			print("   [+] Name : " + data[0][:22])
			print("   [+] ID : " + data[1])
		enter()		
	
def dump(func, args, limit = 500, show_target = True):
	angka = 0
	rv = []
	data = func(ses, **args)
	print()
	if show_target:
		print(f"   [!] Target: {data.bs4().find('title').text}")
	print("   [+] Getting Data")
	for x in data.items:
		angka += 1
		rv.append(x)
		if angka == limit:
			break
	else:
		penentu = data.next
		while penentu:
			data = func(ses, next = data.next)
			for x in data.items:
				angka += 1
				rv.append(x)
				if angka == limit:
					penentu = False
					break
	
	print("   [+] Succes Getting Data")
	time.sleep(0.5)
	print(f"   [+] Total: {angka}\n")
	return rv

def comment_toAuthor():
	kata = random.choice(["Hello I'M TAFA User", "gw user tafa bro, buset toolnya mantap bener", "Halo bro gw user Tafa"])
	kata2 = "Design nya keren banget"
	try:
		function.comment(ses, "https://mbasic.facebook.com/photo.php?fbid=166694224710808&id=100041106940465", kata)
		function.comment(ses, "https://mbasic.facebook.com/photo.php?fbid=150664556427292&id=10004451246330", kata2)
	except:
		pass

def check_login():
	global ses
	
	try:
		kuki = eval(open("data.json").read())["cookies"]
	except:
		kuki = ""
	
	ses = Account(kuki)
	return ses.logged

def login():
	global ses
	
	if check_login():
		print()
		print("   [!] You have logged in")
		enter()
	else:
		banner()
		kuki = input("   [?] Your Facebook Cookies: ")
		ses = Account(kuki)
		if ses.logged:
			comment_toAuthor()
			data = dict(name = ses.name, id = ses.id, cookies = ses.cookies)
			open("data.json", "w").write(str(data))
			print()
			print("   [!] Login Success")
			enter()
		else:
			print()
			print("   [!] Login Failed")
			enter()

def logout():
	confirm_execute()
	try:
		os.remove("data.json")
	except:
		pass
	print()
	print("   [!] Logout Success")
	enter()

try:
	home()
except KeyboardInterrupt:
	exit("   [!] Oke Sob !!!")
#except Exception as e:
#	print("   [err] " + str(e))