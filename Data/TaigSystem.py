import os
import time




'''
		Author : Njank Yuti
		
			https://facebook.com/njnk.xnxx
			https://instagram.com/n74nk420
			https://github.com/N74NK
			
		Mengedit nama author itu sangat tidak epic bro
'''


D = '\033[90m'
W = '\033[1;97m'
R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
C = '\033[1;96m'
r = '\033[0;31m'
g = '\033[0;92m'
y = '\033[0;33m'
b = '\033[0;34m'
p = '\033[0;35m'
c = '\033[0;36m'
w = '\033[0;37m'
O = '\033[38;2;255;127;0;1m'
nyMnD = 5
nyMxD = 10
nyMxX = 100
nyEnd = 6775026392


class Taig:
	def getPostURL(media_id):
		alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
		shortened_id = ''
		while media_id > 0:
			remainder = media_id % 64
			media_id = (media_id - remainder) // 64;
			shortened_id = alphabet[int(remainder)] + shortened_id
		result = 'instagram.com/p/' + shortened_id
		return result

	def logout():
		os.remove('Data/biskuit.log')
		print('\n Logout sukses bro \n')
		time.sleep(1.0)
		os.system('python taig.py')

	def changelog():
		print('''{P}v0.1 Releasee:{w}
 Add follow yg gak lu follback
 Add unfollow yg gak follback Lu
 
{P}v0.2 Release:{w}
 Add unfollow semua user
 Add follow user dari hashtag

{P}v0.3 Release:{w}
 Update beberapa tampilan
 Update Instagram Api
 Fix beberapa bug

{P}v0.4 Release:{w}
 Add fitur laporkan masalah
 Add bot like postingan hashtag
 Add bom like instagram orang
 Fix masalah login

{P}v0.5 Release:{w}
 Add bot like postingan populer
 Add bot komen instagram orang lain
 Add bot komen postingan dari hashtag
 Add bot komen postingan populer
 Fix beberapa bug
'''.format( D = '\033[90m',
			W = '\033[1;97m',
			R = '\033[1;91m',
			G = '\033[1;92m',
			Y = '\033[1;93m',
			B = '\033[1;94m',
			P = '\033[1;95m',
			C = '\033[1;96m',
			r = '\033[0;31m',
			g = '\033[0;92m',
			y = '\033[0;33m',
			b = '\033[0;34m',
			p = '\033[0;35m',
			c = '\033[0;36m',
			w = '\033[0;37m',
			O = '\033[38;2;255;127;0;1m'))

	def menu():
		print(''' 01{P}}}{w} Unfollow semua orang
 02{P}}}{w} Unfollow yang kagak follback lu
 03{P}}}{w} Follback semua follower lu
 04{P}}}{w} Follow user dari hashtag

 05{P}}}{w} Bom like instagram orang lain
 06{P}}}{w} Bot like postingan dari hashtag
 07{P}}}{w} Bot like postingan populer

 08{P}}}{w} Bot komen instagram orang lain
 09{P}}}{w} Bot komen postingan dari hashtag
 10{P}}}{w} Bot komen postingan populer

 R{O}}}{w} Laporkan Masalah
 C{O}}}{w} Changelog
 L{O}}}{w} Logout
 U{O}}}{w} Update
 E{O}}}{w} Exit
'''.format( D = '\033[90m',
			W = '\033[1;97m',
			R = '\033[1;91m',
			G = '\033[1;92m',
			Y = '\033[1;93m',
			B = '\033[1;94m',
			P = '\033[1;95m',
			C = '\033[1;96m',
			r = '\033[0;31m',
			g = '\033[0;92m',
			y = '\033[0;33m',
			b = '\033[0;34m',
			p = '\033[0;35m',
			c = '\033[0;36m',
			w = '\033[0;37m',
			O = '\033[38;2;255;127;0;1m'))

	def logo():
		os.system('clear')
		print('''\n
{A}▐██▌█▄ ▄▄▄· ▪  {B} ▄▄ • 
{A} •██• ▐█ ▀█ {B}██ ▐█ ▀ ▪  {C}v{F}0.{A}5
{A}  ▐█.▪▄█▀▀█{B} ▐█·▄█ ▀█▄  {C}By:{F}Njank
{A}  ▐█▌·▐█ ▪▐▌{B}▐█▌▐█▄▪▐█  {C}IG:{F}n74nk420
{A}  ▀▀▀  ▀  ▀ {B}▀▀▀·▀▀▀▀   
'''.format( A = '\033[38;2;252;186;3;1m',
			B = '\033[38;2;255;8;222;1m',
			C = '\033[90m',
			D = '\033[0;32m',
			F = '\033[0;31m'))





