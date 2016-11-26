from crypt import crypt
def testPass(cryptPass):
	salt = cryptPass.split('$')[2]
	myPass = cryptPass.split('$')[3]
	dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt(word,"$6$"+salt+'$')
		cryptWord = cryptWord.split("$")[3]
		if (cryptWord == myPass):
			print("[+] Found Password: "+word+"\n")
			return
	print("[-] Password Not Found.\n")
	return
def main():
	passFile = open('passwords512.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			if len(cryptPass)>3:
				print("[*] Cracking Password For: "+user)
				testPass(cryptPass)
if __name__ == "__main__":
   main()	
