import sys, json, os, time, random, re

try:
	import stdiomask, requests, requests_toolbelt
except:
	os.system('pip install requests stdiomask requests_toolbelt')

from Data import Nyhead
from Data.InstagramAPI import InstagramAPI

D = '\033[90m'
W = '\033[1;97m'
R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
C = '\033[1;96m'
r = '\033[0;31m'
g = '\033[0;32m'
y = '\033[0;33m'
b = '\033[0;34m'
p = '\033[0;35m'
c = '\033[0;36m'
w = '\033[0;37m'
O = '\033[38;2;255;127;0;1m'

followers = []
followings = []

nyMnD = 5
nyMxD = 10
nyMxX = 100

def main():
	Nyhead.nyLl()
	try:
		with open('Data/biskuit.log', 'r') as nyb:
			nyf = nyb.read()
			nyd = nyf.split("|")
			nyUSR = nyd[0]
			nyPWD = nyd[1]
			nyL(nyUSR,nyPWD)
	except FileNotFoundError:
		login()

def login():
	try:
		print(f'{w}Masukan username dan password instagram Lu\nReport bug ke FB atau WA Gua\n')
		nyUSR = input(f' {P}{{{w}#{P}}}{w} Username: ')
		nyPWD = stdiomask.getpass(prompt=f' {P}{{{w}#{P}}}{w} Password: ')
	except KeyboardInterrupt:
		exit('\n Sampai jumpa lagi bro \n')
		
	Nyhead.nyLl()
	with open('Data/biskuit.log', 'w') as nyb:
		nyb.write(f'{nyUSR}|{nyPWD}')
		nyb.close
	nyL(nyUSR,nyPWD)

def nyCl():
	Nyhead.nyLl()
	print(f'''{P}v0.1 Releasee:{w}
 Add follow yg gak lu follback
 Add unfollow yg gak follback Lu
 
{P}v0.2 Release:{w}
 Add unfollow semua user
 Add follow user dari hashtag

{P}v0.3 Release:{w}
 Memperbaiki beberapa bug
 Update beberapa tampilan
 Update Instagram Api
''')
	input(f' {P}{{{w} Back{P} }} ');main()

def nyGid(nyUs):
	nyUr = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+nyUs+"&rank_token=0.3953592318270893&count=1"
	nyRp = requests.get(nyUr)
	nyRj = nyRp.json()
	nyUid = str( nyRj['users'][0].get("user").get("pk") )
	return nyUid

def nyL(nyUSR,nyPWD):
	try:
		api = InstagramAPI(nyUSR, nyPWD)
		api.login()
		for i in api.getTotalSelfFollowers():
			followers.append(i.get("username") )
		for i in api.getTotalSelfFollowings():
			followings.append(i.get("username") )
		nyU = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+nyUSR+"&rank_token=0.3953592318270893&count=1"
		nyrr = requests.get(nyU)
		nyrrr = nyrr.json()
		nyNN = str( nyrrr['users'][0].get("user").get("full_name") )
		print(f'{w}Masuk sebagai {G}{nyNN}\n{w}Report bug ke FB atau WA Gua\n')
		tt = 0
		for i in followings:
			tt=tt+1
		print(f" {R}>{w} Total diikuti: {str(tt)}")
		tt = 0
		for i in followers:
			tt=tt+1
		print(f" {R}>{w} Total pengikut: {str(tt)}")
		tt = 0
		for i in followings:
			if i not in followers:
				tt=tt+1
		print(f" {R}>{w} Kagak follback Lu: {str(tt)}")
		tt = 0
		for i in followers:
			if i not in followings:
				tt=tt+1
		print(f''' {R}>{w} Kagak Lu follback: {str(tt)}\n
1{P}}}{w} Unfollow semua orang
2{P}}}{w} Unfollow yang kagak follback lu
3{P}}}{w} Follback semua follower lu
4{P}}}{w} Follow user dari hashtag

 C{O}}}{w} Changelog
 L{O}}}{w} Logout
 U{O}}}{w} Update
 E{O}}}{w} Exit
		''')
		nyIi = input(' >> ')
	except KeyboardInterrupt:
		print(f'\n {w}Fitur exit ada di menu bro \n');time.sleep(2);main()
		
	if (nyIi == '2') or (nyIi == '02'):
		nyCn = 0
		nyWL = open("kecualikan.txt").read().splitlines()
		Nyhead.nyLl();print(f"{w} Unfollow dijalankan bro\n")
		for i in followings:
			if (i not in followers) and (i not in nyWL):
				nyCn+=1
				time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				nyUid = nyGid(i)
				print(f' {R}{{{w}{str(nyCn)}{R}}}{w} {i} diunfollow')
				api.unfollow(nyUid)
		input(f' {P}{{{w} Back{P} }} ');main()
				
	elif (nyIi == '3') or (nyIi == '03'):
		nyCn = 0
		Nyhead.nyLl();print(f"{w} Followback dijalankan bro\n")
		for i in followers:
			if i not in followings:
				nyCn+=1
				time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				nyUid = nyGid(i)
				print(f' {R}{{{w}{str(nyCn)}{R}}}{w} {i} terfollow')
				api.follow(nyUid)
		input(f' {P}{{{w} Back{P} }} ');main()
				
	elif (nyIi == '1') or (nyIi == '01'):
		nyCn = 0
		Nyhead.nyLl();print(f"{w} Otw unfollow semua orang bro\n")
		for i in followings:
			nyCn +=1
			time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
			nyUid = nyGid(i)
			print(f' {R}{{{w}{str(nyCn)}{R}}}{w} {i} diunfollow')
			api.unfollow(nyUid)
		input(f' {P}{{{w} Back{P} }} ');main()
			
	elif (nyIi == '4') or (nyIi == '04'):
		Nyhead.nyLl()
		tag = input(f'{w} Hashtag: ')
		api.tagFeed(tag)
		media_id = api.LastJson 
		nyCn = 0
		print(f' {w}Follow user dari Hashtag dijalankan\n')
		for i in media_id["items"]:
			time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
			nyUMe = i.get("user")["username"]
			nyuiD = i.get("user")["pk"]
			nyCn += 1
			api.follow(nyuiD)
			print(f' {R}{{{w}{str(nyCn)}{R}}}{w} {str(nyUMe)} terfollow')
			if(nyCn>=nyMxX):
				break
		print(f' {w}Total {str(nyCn)} user terfollow \n')
		input(f' {P}{{{w} Back{P} }} ');main()
		
	elif (nyIi == 'c') or (nyIi == 'C'):
		nyCl()
		
	elif (nyIi == 'l') or (nyIi == 'L'):
		os.remove('Data/biskuit.log')
		print('\n Logout sukses bro \n');time.sleep(1);os.system('python taig.py')
		
	elif (nyIi == 'u') or (nyIi == 'U'):
		os.system('git pull; python taig.py')
		
	elif (nyIi == 'e') or (nyIi == 'E'):
		exit('\n Sampai dilain waktu bro \n')
		
	else:
		print('\n Error bro, input kagak bener! \n');time.sleep(1);main()

if __name__ == "__main__":
	main()
