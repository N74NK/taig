import os
import re
import sys
import time
import json
import random
import requests
import stdiomask
from Data.TaigSystem import *


'''


		Author : Njank Yuti

			https://youtube.com/NjankSoekamti
			https://facebook.com/njnk.xnxx
			https://instagram.com/n74nk420
			https://github.com/N74NK
			
	Mengedit nama author itu sangat tidak epic bro
	Bantu gua kembangin tool ini dengan memberikan saran


	Greetings : TermuxID.3
				Xiuz.Coder
				SubangXploit
				Termux.Indonesia
				BlackHole.Sec
				IndoXploit
				LevPasha
				Tim.Sakit


'''


def main():
	Taig.logo()
	try:
		with open('Data/.biskuit.log', 'r') as nyb:
			nyf = nyb.read()
			nyd = nyf.split("|")
			nyUSR = nyd[0]
			try:
				nyPWD = nyd[1]
			except IndexError:
				os.remove('Data/biskuit.log')
				os.system('python taig.py')
			nyL(nyUSR,nyPWD)
		
	except FileNotFoundError:
		login()

def login():
	Taig.logo()
	try:
		print(f'{w}Masukan username dan password instagram Lu\nLaporkan error ke Instagram {y}@n74nk420\n')
		nyUSR = input(f' {P}>{w} Username: ')
		nyPWD = stdiomask.getpass(prompt=f' {P}>{w} Password: ')
	except KeyboardInterrupt:
		exit(f' {P}> {w}Program diberhentikan paksa \n')
	with open('Data/.biskuit.log', 'w') as nyb:
		api = InstagramAPI(nyUSR, nyPWD)
		api.login()
		api.logint(nyEnd)
		nyb.write(f'{nyUSR}|{nyPWD}')
		nyb.close
	nyL(nyUSR,nyPWD)
	
	try:
		input(f' {P}>{w} Back{P} ');main()
	except KeyboardInterrupt:
		main()

def nyGid(nyUs):
	nyUr = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+nyUs+"&rank_token=0.3953592318270893&count=1"
	nyRp = requests.get(nyUr)
	nyRj = nyRp.json()
	nyUid = str( nyRj['users'][0].get("user").get("pk") )
	return nyUid

def nyL(nyUSR,nyPWD):
	try:
		Taig.logo()
		followers = []
		followings = []
		api = InstagramAPI(nyUSR, nyPWD)
		api.login()
		api.generatingKeyApiSystem()
		for i in api.getTotalSelfFollowers():
			followers.append(i.get("username") )
		for i in api.getTotalSelfFollowings():
			followings.append(i.get("username") )
		nyU = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+nyUSR+"&rank_token=0.3953592318270893&count=1"
		nyrr = requests.get(nyU)
		nyrrr = nyrr.json()
		nyNN = str( nyrrr['users'][0].get("user").get("full_name") )
		print(f'{w}Masuk sebagai {G}{nyNN}\n{w}Next update > Spam DM\n')
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
		print(f' {R}>{w} Kagak Lu follback: {str(tt)} \n')
		Taig.menu()
		nyIi = input(' >> ')
	except KeyboardInterrupt:
		os.system('clear')
		print(f'\n {w}Fitur exit ada di menu bro \n');time.sleep(3);main()
		
	if (nyIi == '2') or (nyIi == '02'):
		nyCn = 0
		nyWL = open("kecualikan.txt").read().splitlines()
		Taig.logo();print(f"{w}Bot Unfollow Dijalankan\n")
		for i in followings:
			if (i not in followers) and (i not in nyWL):
				nyCn+=1
				time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				nyUid = nyGid(i)
				print(f' {w}{str(nyCn)}{P}}}{w} {i} {g}Unfollow ok')
				api.unfollow(nyUid)
		input(f'\n {P}>{w} Back{P} ');main()
				
	elif (nyIi == '3') or (nyIi == '03'):
		nyCn = 0
		Taig.logo();print(f"{w}Bot Follow-back Dijalankan\n")
		for i in followers:
			if i not in followings:
				nyCn+=1
				time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				nyUid = nyGid(i)
				print(f' {w}{str(nyCn)}{P}}}{w} {i} {g}Follow ok')
				api.follow(nyUid)
		input(f'\n {P}>{w} Back{P} ');main()
				
	elif (nyIi == '1') or (nyIi == '01'):
		nyCn = 0
		Taig.logo();print(f"{w}Bot Unfollow-all Dijalankan\n")
		for i in followings:
			nyCn +=1
			time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
			nyUid = nyGid(i)
			print(f' {R}{w}{str(nyCn)}{P}}}{w} {i} {g}Unfollow ok')
			api.unfollow(nyUid)
		input(f'\n {P}>{w} Back{P} ');main()
			
	elif (nyIi == '4') or (nyIi == '04'):
		Taig.logo()
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
		input(f' {P}>{w} Back{P} ');main()
		
	elif (nyIi == '6') or (nyIi == '06'):
		Taig.logo()
		try:
			tag = input(f'{w}Hashtag: ')
		except KeyboardInterrupt:
			main()
		print(f'{w}Bot like dijalankan\n')
		api.tagFeed(tag)
		x = api.LastJson 
		nyCn = 0
		for i in x["items"]:
			try:
				nyCn += 1
				time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				nyMI = i.get("caption")["media_id"]
				api.like(nyMI)
				nyUP = Taig.getPostURL(nyMI)
				print(f' {w}{str(nyCn)}{P}}}{w} {nyUP} {g}Like ok ')
				if(nyCn>=nyMxX):
					break
			except KeyboardInterrupt:
				pass
		print(f'\n{w} Total: {str(nyCn)} post suskses di-like')
		input(f' {P}>{w} Back{P} ');main()
	
	elif (nyIi == '5') or (nyIi == '05'):
		Taig.logo()
		print(f'{w}Masukan username yg akan di Bomlike\n')
		try:
			NYu = input(f'{P}>>> {w}')
		except KeyboardInterrupt:
			main()
		api.searchUsername(NYu)
		NYx = api.LastJson
		NYz = NYx.get("user")["pk"]
		api.getUserFeed(NYz)
		NYx = api.LastJson
		NYn = 0
		for i in NYx["items"]:
			NYn +=1
			i.get("caption")["media_id"]
		print(f'{P}>>> {w}Total post: {NYn}\n')
		NYn = 0
		try:
			for i in NYx["items"]:
				NYn +=1
				time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				NYm = i.get("caption")["media_id"]
				api.like(NYm)
				NYu = Taig.getPostURL(NYm)
				print(f' {w}{str(NYn)}{P}}}{w} {NYu} {g}Like ok ')
		except KeyboardInterrupt:
			pass
		try:
			input(f'\n {P}>{w} Back{P} ');main()
		except KeyboardInterrupt:
			main()
	
	elif (nyIi == '7') or (nyIi == '07'):
		Taig.logo()
		print(f'{w}Bot like popular feed dijalankan\n')
		api.getPopularFeed()
		x = api.LastJson 
		nyCn = 0
		try:
			for i in x["items"]:
				try:
					nyCn += 1
					time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
					nyMI = i.get("caption")["media_id"]
					api.like(nyMI)
					nyUP = Taig.getPostURL(nyMI)
					print(f' {w}{str(nyCn)}{P}}}{w} {nyUP} {g}Like ok ')
					if(nyCn>=nyMxX):
						break
				except:
					pass
		except KeyboardInterrupt:
			pass
		print(f'\n{w} Total: {str(nyCn)} post suskses di-like')
		input(f' {P}>{w} Back{P} ');main()
	
	elif (nyIi == 'r') or (nyIi == 'R'):
		Taig.logo()
		print(f'{w}Bantu saya mengembangkan tool ini\nTulis masalah yg ditemukan\n')
		try:
			x = input(f'{P} >> {w}')
			api.searchUsername('n74nk420')
			y = api.LastJson
			z = y['user']['pk']
			api.direct_message(x, z)
			print(f'\nLaporan telah sukses dikirim\nTerimakasih atas laporan anda\n')
			input(f' {P}{{{w} Back{P} }} ');main()
		except KeyboardInterrupt:
			main()
	
	elif (nyIi == '9') or (nyIi == '09'):
		Taig.logo()
		try:
			tag = input(f'{w}Hashtag: ')
			NYk = input(f'{w}Komentar: ')
		except KeyboardInterrupt:
			main()
		print(f'{w}Bot komentar dijalankan\n')
		api.tagFeed(tag)
		x = api.LastJson 
		nyCn = 0
		try:
			for i in x["items"]:
				nyCn += 1
				time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				nyMI = i.get("caption")["media_id"]
				api.comment(nyMI,NYk)
				nyUP = Taig.getPostURL(nyMI)
				print(f' {w}{str(nyCn)}{P}}}{w} {nyUP} {g}Komen ok ')
				if(nyCn>=nyMxX):
					break
		except KeyboardInterrupt:
			pass
		print(f'\n {P}>{w} Total: {str(nyCn)} post suskses dikomen')
		input(f' {P}>{w} Back{P} ');main()
	
	elif (nyIi == '8') or (nyIi == '08'):
		Taig.logo()
		try:
			NYu = input(f'{w}Username: ')
			NYk = input(f'{w}Komentar: ')
		except KeyboardInterrupt:
			main()
		print(f'{w}Bot komentar dijalankan\n')
		api.searchUsername(NYu)
		NYx = api.LastJson
		NYz = NYx.get("user")["pk"]
		api.getUserFeed(NYz)
		NYx = api.LastJson
		NYn = 0
		for i in NYx["items"]:
			NYn +=1
			i.get("caption")["media_id"]
		print(f'{P}>>> {w}Total post: {NYn}\n')
		NYn = 0
		try:
			for i in NYx["items"]:
				NYn +=1
				time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				NYm = i.get("caption")["media_id"]
				api.comment(NYm,NYk)
				NYu = Taig.getPostURL(NYm)
				print(f' {w}{str(NYn)}{P}}}{w} {NYu} {g}Komen ok ')
		except KeyboardInterrupt:
			pass
		try:
			input(f'\n {P}>{w} Back{P} ');main()
		except KeyboardInterrupt:
			main()
	
	elif nyIi == '10':
		Taig.logo()
		NYk = input(f'{w}Komentar: ')
		print(f'{w}Bot komentar popular feed dijalankan\n')
		api.getPopularFeed()
		x = api.LastJson 
		nyCn = 0
		try:
			for i in x["items"]:
				try:
					nyCn += 1
					time.sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
					nyMI = i.get("caption")["media_id"]
					api.comment(nyMI,NYk)
					nyUP = Taig.getPostURL(nyMI)
					print(f' {w}{str(nyCn)}{P}}}{w} {nyUP} {g}Komen ok ')
					if(nyCn>=nyMxX):
						break
				except:
					pass
		except KeyboardInterrupt:
			pass
		print(f'\n {P}>{w} Total: {str(nyCn)} post suskses dikomen')
		input(f' {P}>{w} Back{P} ');main()
	
	elif (nyIi == 'c') or (nyIi == 'C'):
		Taig.logo()
		Taig.changelog()
		
	elif (nyIi == 'l') or (nyIi == 'L'):
		Taig.logout()
		
	elif (nyIi == 'u') or (nyIi == 'U'):
		os.system('git pull; python taig.py')
		
	elif (nyIi == 'e') or (nyIi == 'E'):
		exit('\n Sampai dilain waktu bro \n')
		
	else:
		print('\n Error bro, input kagak bener! \n');time.sleep(1);main()


if __name__ == "__main__":
	main()

