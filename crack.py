from banner import *
banner()
import pyzipper
import os

def rocku(zfile):
	wordlist = open("rockyou.txt","r")
	with pyzipper.AESZipFile(zfile) as zf:
		for i in wordlist:
			pwd = bytes(i.strip(),"utf-8")
			print("[-] Checking password : ",i)
			try:
				zf.extractall(pwd = pwd)
				print(50*"*")
				print("[+] Password is found : ",i)
				print("Files in ",zfile)
				for f in zf.namelist():
					print("\t",f)
				print(50*"*")
				break
		
			except:
				continue
def custom_passwd(zfile,wfile):
	wordlist = open(wfile,"r")
	with pyzipper.AESZipFile(zfile) as zf:
		for i in wordlist:
			pwd = bytes(i.strip(),"utf-8")
			print("[-] Checking password : ",i)
			try:
				zf.extractall(pwd = pwd)
				print(50*"*")
				print("[+] Password is found : ",i)
				print("Files in ",zfile)
				for f in zf.namelist():
					print("\t",f)
				print(50*"*")
				break
		
			except:
				continue

def bruteforce(zfile,passlen):

	with pyzipper.AESZipFile(zfile) as zf:
		total_passwords = int(passlen* "9")
		for i in range(total_passwords+1):
			pwd = bytes(str(i),"utf-8")
			print("[-] Checking password : ",i)
			try:
				zf.extractall(pwd = pwd)
				print(50*"*")
				print("[+] Password is found : ",i)
				print("Files in ",zfile)
				for f in zf.namelist():
					print("\t",f)
				print(50*"*")
				break
		
			except:
				continue

def main():
	zfile = input("Enter absolute path of the zip file : ")

	if not os.path.isfile(zfile):
		print(zfile," is not found..")
		exit()
	dir = zfile[0:len(zfile)-4]
	if os.path.isdir(dir):
		print(dir, "is already present.. extracting may leads to overwrite of old files.")
		exit()
	print("""
Select method 
	1. Crack using built-in wordlist
	2. Crack with custom wordlist
	3. Crack using bruteforce method
	0. Exit
		""")

	choice = int(input("Enter your choice[1/2/3/0] : "))
	if choice == 1 :
		rocku(zfile)


	elif choice == 2 :
		wfile = input("Enter the absolute path of your password list: ")
		if not os.path.isfile(wfile):
			print(wfile," is not found..")
			exit()
		custom_passwd(zfile,wfile)


	elif choice == 3 :
		print("""
----------------------------------------------------------------------------
Bruteforcing method takes too much of time and system resources to perform..
Use this method to crack the passwords of length upto 4 only.
And the passwords are combination of digits only.
----------------------------------------------------------------------------
			""")
		passlen = int(input("Enter the length of password[Note: <5] : "))
		bruteforce(zfile,passlen)

	else :
		exit()

if __name__ == '__main__':
	main()
