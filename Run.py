try:
    import requests, re, json, time, sys, os
    from rich.columns import Columns
    from rich.console import Console
    from rich.panel import Panel
    from rich import print as printf
    from requests.exceptions import RequestException
except (ModuleNotFoundError) as e:
    print(f"Please install it using: 'pip install {e.name}'")
    __import__('sys').exit(1)

SUKSES, GAGAL, BAD, LOOPING, INVALID, CHECKPOINT, TAMPILKAN = 0, 0, [], 0, [], [], {
    "COUNT": 0
}

def TAMPILKAN_LOGO():
    os.system('cls' if os.name == 'nt' else 'clear')
    printf(Panel("[bold red]   ____                     _        _    _            _ \n  / ___|_ __ __ _ _ __ ___ | |_ __ _| | _(_)_ __   ___(_)\n | |  _| '__/ _` | '_ ` _ \| __/ _` | |/ / | '_ \ / __| |\n | |_| | | | (_| | | | | | | || (_| |   <| | |_) | (__| |\n[bold white]  \____|_|  \__,_|_| |_| |_|\__\__,_|_|\_\_| .__/ \___|_|\n                                           |_|           \n      [underline green]Free Likes & Followers Instagram - by Rozhak", width=63, style="bold bright_black"))
    return (True)

class LOGIN:

    def __init__(self) -> None:
        pass

    def USERNAME(self):
        try:
            TAMPILKAN_LOGO()
            printf(Panel(f"[bold white]Please fill in with Username and Password, you can use `[bold red]:[bold white]` as a separator. For example:\n[bold green]rozhak.sch.id:Rozhak123[bold white] *[bold red]Don't use Old Instagram[bold white]!", width=63, style="bold bright_black", title="> [Login Instagram] <", subtitle="╭──────", subtitle_align="left"))
            self.INSTAGRAM = Console().input("[bold bright_black]   ╰─> ")
            if ':' in self.INSTAGRAM:
                self.USERNAME, self.PASSWORD = (self.INSTAGRAM.split(':')[0], self.INSTAGRAM.split(':')[1])
                with open('Penyimpanan/Akun.json', 'w+') as W:
                    W.write(
                        json.dumps({
                            "Username": f"{self.USERNAME}",
                            "Password": f"{self.PASSWORD}",
                        })
                    )
                printf(Panel(f"[bold white]Congratulations, you have successfully logged in. Make sure your account is not affected\nby a checkpoint so you can use the service!", width=63, style="bold bright_black", title="> [Login Sukses] <"))
                time.sleep(5.0)
                FEATURE()
            else:
                printf(Panel(f"[bold red]You entered the separator between username and password incorrectly, please try again!", width=63, style="bold bright_black", title="> [Login Error] <"))
                sys.exit(1)
        except (Exception) as e:
            printf(Panel(f"[bold red]{str(e).capitalize()}!", width=63, style="bold bright_black", title="> [Error] <"))
            sys.exit(1)

class FEATURE:

    def __init__(self):
        try:
            TAMPILKAN_LOGO()
            self.USERNAME, self.PASSWORD = json.loads(open('Penyimpanan/Akun.json', 'r').read())['Username'], json.loads(open('Penyimpanan/Akun.json', 'r').read())['Password']
            if 'null' in str(self.USERNAME):
                LOGIN().USERNAME()
            else:
                printf(
                    Columns([
                        Panel(f"[bold white]Username:[bold green] {self.USERNAME}", width=31, style="bold bright_black"),
                        Panel(f"[bold white]City:[bold red] {self.CITY()}", width=31, style="bold bright_black")
                    ])
                )
        except (Exception) as e:
            printf(Panel(f"[bold red]{str(e).capitalize()}!", width=63, style="bold bright_black", title="> [Error] <"))
            time.sleep(5.5)
            LOGIN().USERNAME()

        printf(Panel(f"""[bold green]01[bold white]. Get Free Instagram Followers
[bold green]02[bold white]. Get Free Instagram Likes
[bold green]03[bold white]. Get Free Instagram Views
[bold green]04[bold white]. Logout ([bold red]Exit[bold white])""", width=63, style="bold bright_black", title="> [Fitur Utama] <", subtitle="╭──────", subtitle_align="left"))
        self.CHOOSE = Console().input("[bold bright_black]   ╰─> ")
        if self.CHOOSE in ['1', '01']:
            printf(Panel(f"[bold white]Please fill in the username you want to send Followers to. For example:[bold green] @rozhak_official[bold white]\n*[bold red]remember not to fill in with a private account[bold white]!", width=63, style="bold bright_black", title="> [Username] <", subtitle="╭──────", subtitle_align="left"))
            self.YOUR_USERNAME = Console().input("[bold bright_black]   ╰─> ").replace('@', '')
            printf(Panel(f"[bold white]You can use[bold green] CTRL + C[bold white] if stuck and use[bold red] CTRL + Z[bold white] if you want to stop. if it fails to send,\nthe service is probably under maintenance!", width=63, style="bold bright_black", title="> [Catatan] <"))
            while True:
                try:
                    TAMPILKAN['COUNT'] = 0
                    CHECKPOINT.clear()
                    BAD.clear()
                    for HOST_NAME in ['gramtakipci.xyz', 'takipkasma.com']:
                        printf(f"[bold bright_black]   ──>[bold green] SENDING ON {str(HOST_NAME).split('.')[0].upper()} SERVICE!                   ", end='\r')
                        time.sleep(2.5)
                        SUBMIT().LOGIN(self.YOUR_USERNAME, self.USERNAME, self.PASSWORD, HOST_NAME, QUERY='Follower')
                        if len(CHECKPOINT) >= 2:
                            printf(Panel(f"[bold red]There was an error while sending Followers, it is possible that your Instagram account has been hit by a checkpoint, if not, it means your account has been detected as spam by Instagram!", width=63, style="bold bright_black", title="> [Pengiriman Error] <"))
                            sys.exit(1)
                        elif len(BAD) >= 2:
                            printf(Panel(f"[bold red]Your Instagram is experiencing login failure on 2 sites, try logging in manually and running this tool again!", width=63, style="bold bright_black", title="> [Login Error] <"))
                            sys.exit(1)
                        else:
                            continue
                    printf(f"[bold bright_black]   ──>[bold green] DONE SENDING AT {str(HOST_NAME).split('.')[0].upper()} SERVICE!                   ", end='\r')
                    time.sleep(5.5)
                    for SLEEP in range(895, 0, -1):
                        printf(f"[bold bright_black]   ──>[bold green] @{str(self.YOUR_USERNAME).upper()}[bold white]/[bold blue]{SLEEP}[bold white]/[bold blue]{LOOPING}[bold white] SUKSES:-[bold green]{SUKSES}[bold white] GAGAL:-[bold red]{GAGAL}     ", end='\r')
                        time.sleep(1)
                    continue
                except (RequestException):
                    printf(f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!         ", end='\r')
                    time.sleep(10.5)
                    continue
                except (KeyboardInterrupt):
                    printf(f"[bold white]                            ", end='\r')
                    time.sleep(2.5)
                    continue
        elif self.CHOOSE in ['2', '02']:
            printf(Panel(f"[bold white]Please fill in the post link, make sure your Instagram is not locked or private.\nFor example:[bold green] https://www.instagram.com/p/C08X1bNvh7g/", width=63, style="bold bright_black", title="> [Link Postingan] <", subtitle="╭──────", subtitle_align="left"))
            self.LINK_POST = Console().input("[bold bright_black]   ╰─> ").replace('@', '')
            printf(Panel(f"[bold white]You can use[bold green] CTRL + C[bold white] if stuck and use[bold red] CTRL + Z[bold white] if you want to stop. if it fails to send,\nthe service is probably under maintenance!", width=63, style="bold bright_black", title="> [Catatan] <"))
            while True:
                try:
                    TAMPILKAN['COUNT'] = 0
                    CHECKPOINT.clear()
                    BAD.clear()
                    for HOST_NAME in ['gramtakipci.xyz', 'takipkasma.com']:
                        printf(f"[bold bright_black]   ──>[bold green] SENDING ON {str(HOST_NAME).split('.')[0].upper()} SERVICE!                   ", end='\r')
                        time.sleep(2.5)
                        SUBMIT().LOGIN(self.LINK_POST, self.USERNAME, self.PASSWORD, HOST_NAME, QUERY='Likes')
                        if len(CHECKPOINT) >= 2:
                            printf(Panel(f"[bold red]There was an error while sending Likes, it is possible that your Instagram account has been hit by a checkpoint, if not, it means your account has been detected as spam by Instagram!", width=63, style="bold bright_black", title="> [Pengiriman Error] <"))
                            sys.exit(1)
                        elif len(BAD) >= 2:
                            printf(Panel(f"[bold red]Your Instagram is experiencing login failure on 2 sites, try logging in manually and running this tool again!", width=63, style="bold bright_black", title="> [Login Error] <"))
                            sys.exit(1)
                        else:
                            continue
                    printf(f"[bold bright_black]   ──>[bold green] DONE SENDING AT {str(HOST_NAME).split('.')[0].upper()} SERVICE!                   ", end='\r')
                    time.sleep(5.5)
                    for SLEEP in range(895, 0, -1):
                        printf(f"[bold bright_black]   ──>[bold white] TUNGGU [bold blue]{SLEEP}[bold white]/[bold blue]{LOOPING}[bold white] SUKSES:-[bold green]{SUKSES}[bold white] GAGAL:-[bold red]{GAGAL}     ", end='\r')
                        time.sleep(1)
                    continue
                except (RequestException):
                    printf(f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!         ", end='\r')
                    time.sleep(10.5)
                    continue
                except (KeyboardInterrupt):
                    printf(f"[bold white]                            ", end='\r')
                    time.sleep(2.5)
                    continue
        elif self.CHOOSE in ['3', '03']:
            printf(Panel(f"[bold white]Please fill in the post link, make sure your Instagram is not locked or private.\nFor example:[bold green] https://www.instagram.com/reel/C08X1bNvh7g/", width=63, style="bold bright_black", title="> [Link Postingan] <", subtitle="╭──────", subtitle_align="left"))
            self.LINK_POST = Console().input("[bold bright_black]   ╰─> ").replace('@', '')
            printf(Panel(f"[bold white]You can use[bold green] CTRL + C[bold white] if stuck and use[bold red] CTRL + Z[bold white] if you want to stop. if it fails to send,\nthe service is probably under maintenance!", width=63, style="bold bright_black", title="> [Catatan] <"))
            while True:
                try:
                    TAMPILKAN['COUNT'] = 0
                    CHECKPOINT.clear()
                    BAD.clear()
                    for HOST_NAME in ['gramtakipci.xyz', 'takipkasma.com']:
                        printf(f"[bold bright_black]   ──>[bold green] SENDING ON {str(HOST_NAME).split('.')[0].upper()} SERVICE!                   ", end='\r')
                        time.sleep(2.5)
                        SUBMIT().LOGIN(self.LINK_POST, self.USERNAME, self.PASSWORD, HOST_NAME, QUERY='Views')
                        if len(CHECKPOINT) >= 2:
                            printf(Panel(f"[bold red]There was an error while sending Views, it is possible that your Instagram account has been hit by a checkpoint, if not, it means your account has been detected as spam by Instagram!", width=63, style="bold bright_black", title="> [Pengiriman Error] <"))
                            sys.exit(1)
                        elif len(BAD) >= 2:
                            printf(Panel(f"[bold red]Your Instagram is experiencing login failure on 2 sites, try logging in manually and running this tool again!", width=63, style="bold bright_black", title="> [Login Error] <"))
                            sys.exit(1)
                        else:
                            continue
                    printf(f"[bold bright_black]   ──>[bold green] DONE SENDING AT {str(HOST_NAME).split('.')[0].upper()} SERVICE!                   ", end='\r')
                    time.sleep(5.5)
                    for SLEEP in range(895, 0, -1):
                        printf(f"[bold bright_black]   ──>[bold white] TUNGGU [bold blue]{SLEEP}[bold white]/[bold blue]{LOOPING}[bold white] SUKSES:-[bold green]{SUKSES}[bold white] GAGAL:-[bold red]{GAGAL}     ", end='\r')
                        time.sleep(1)
                    continue
                except (RequestException):
                    printf(f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!         ", end='\r')
                    time.sleep(10.5)
                    continue
                except (KeyboardInterrupt):
                    printf(f"[bold white]                            ", end='\r')
                    time.sleep(2.5)
                    continue
        elif self.CHOOSE in ['4', '04']:
            printf(Panel(f"[bold white]You have selected the exit option, thank you for using this program. We hope this program helps you!", width=63, style="bold bright_black", title="> [Keluar] <"))
            os.remove('Penyimpanan/Akun.json')
            sys.exit(0)
        else:
            printf(Panel(f"[bold red]The option you entered is not available in this Feature, please try another option!", width=63, style="bold bright_black", title="> [Keluar] <"))
            time.sleep(4.5)
            FEATURE()

    def CITY(self):
        try:
            with requests.Session() as SESSION:
                self.CITY_ = json.loads(SESSION.get('https://ipinfo.io/json', verify=True).text)['city']
            return (self.CITY_)
        except:
            self.CITY_ = ('Unknown')
            return (self.CITY_)

class SUBMIT:

    def __init__(self) -> None:
        pass

    def LOGIN(self, TAUTAN, USERNAME, PASSWORD, HOST_NAME, QUERY):
        with requests.Session() as SESSION:
            SESSION.headers.update({
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Host': '{}'.format(HOST_NAME),
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'Accept-Encoding': 'gzip, deflate',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
            })
            RESPONSE = SESSION.post('https://{}/'.format(HOST_NAME), allow_redirects=True, verify=True)
            self.HREF_LOGIN = re.search(r'href="/([a-f0-9]{40})"', RESPONSE.text).group(1)

            SESSION.headers.update({
                'Referer': 'https://{}/{}'.format(HOST_NAME, self.HREF_LOGIN),
                'Cookie': '; '.join([str(key) +'='+ str(value) for key, value in SESSION.cookies.get_dict().items()]),
                'Sec-Fetch-Site': 'same-origin'
            })
            RESPONSE2 = SESSION.get('https://{}/{}'.format(HOST_NAME, self.HREF_LOGIN), allow_redirects=True, verify=True)
            self.ANTI_FORGERY_TOKEN = re.search(r'&antiForgeryToken=([a-f0-9]+)', RESPONSE2.text).group(1)

            PAYLOAD = {
                'antiForgeryToken': f'{self.ANTI_FORGERY_TOKEN}',
                'username': f'{USERNAME}',
                'userid': '',
                'password': f'{PASSWORD}',
            }
            SESSION.headers.update({
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Content-Length': '{}'.format(len(str(PAYLOAD))),
                'Origin': 'https://{}'.format(HOST_NAME),
                'Cookie': '; '.join([str(key) +'='+ str(value) for key, value in SESSION.cookies.get_dict().items()]),
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            })
            RESPONSE3 = SESSION.post('https://{}/{}?'.format(HOST_NAME, self.HREF_LOGIN), data=PAYLOAD, allow_redirects=True, verify=True)
            if '"status":"success"' in RESPONSE3.text:
                self.COOKIES = ('; '.join([str(key) +'='+ str(value) for key, value in SESSION.cookies.get_dict().items()]))
                printf(f"[bold bright_black]   ──>[bold green] LOGIN {str(HOST_NAME).split('.')[0].upper()} SUCCESSFUL!                   ", end='\r')
                time.sleep(4.5)
                TYPE = {
                    'Follower': 'send-follower',
                    'Likes': 'send-like'
                }.get(QUERY, 'send-view-video')
                self.LIKES_FOLLOWERS_VIEWS(TAUTAN, HOST_NAME, self.COOKIES, TYPE, QUERY)
            else:
                printf(f"[bold bright_black]   ──>[bold red] LOGIN {str(HOST_NAME).split('.')[0].upper()} FAILED!                        ", end='\r')
                time.sleep(4.5)
                BAD.append(f'{RESPONSE3.status_code}')
                return (False)

    def LIKES_FOLLOWERS_VIEWS(self, TAUTAN, HOST_NAME, COOKIES, TYPE, QUERY):
        global LOOPING
        with requests.Session() as SESSION:
            SESSION.headers.update({
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cookie': '{}'.format(COOKIES),
                'Connection': 'keep-alive',
                'Host': '{}'.format(HOST_NAME),
                'Sec-Fetch-Site': 'same-origin',
                'Referer': 'https://{}/tools'.format(HOST_NAME),
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Accept-Encoding': 'gzip, deflate',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
            })
            RESPONSE = SESSION.get('https://{}/tools'.format(HOST_NAME), allow_redirects=True, verify=True)
            if 'LOGIN' in RESPONSE.text:
                printf(f"[bold bright_black]   ──>[bold red] COOKIES {str(HOST_NAME).split('.')[0].upper()} INVALID!                   ", end='\r')
                time.sleep(4.5)
                INVALID.append(f'{RESPONSE.text}')
                return (True)
            else:
                SESSION.headers.update({
                    'Cookie': '; '.join([str(key) +'='+ str(value) for key, value in SESSION.cookies.get_dict().items()]),
                })
                RESPONSE2 = SESSION.get('https://{}/tools/{}'.format(HOST_NAME, TYPE), allow_redirects=True, verify=True)
                PAYLOAD = {'username': TAUTAN} if QUERY == 'Follower' else {'mediaUrl': TAUTAN}
                self.FIND = 'findUserID' if QUERY == 'Follower' else 'findMediaID'

                SESSION.headers.update({
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Content-Length': '{}'.format(len(str(PAYLOAD))),
                    'Cache-Control': 'max-age=0',
                    'Referer': 'https://{}/tools/{}'.format(HOST_NAME, TYPE),
                    'Origin': 'https://{}'.format(HOST_NAME),
                    'Cookie': '; '.join([str(key) +'='+ str(value) for key, value in SESSION.cookies.get_dict().items()]),
                })
                RESPONSE3 = SESSION.post('https://{}/tools/{}?formType={}'.format(HOST_NAME, TYPE, self.FIND), data=PAYLOAD, allow_redirects=True, verify=True)

                if f'/{TYPE}/' in str(RESPONSE3.url):
                    printf(f"[bold bright_black]   ──>[bold green] SUCCESSFULLY FOUND THE {str(QUERY).upper()} FORM!          ", end='\r')
                    time.sleep(2.5)
                    for HEADERS in ['Content-Length', 'Content-Type', 'Origin']:
                        SESSION.headers.pop(f'{HEADERS}')
                    SESSION.headers.update({
                        'Referer': 'https://{}/tools/{}'.format(HOST_NAME, TYPE),
                        'Cookie': '{}'.format('; '.join([str(key) +'='+ str(value) for key, value in SESSION.cookies.get_dict().items()]))
                    })
                    RESPONSE4 = SESSION.get('{}'.format(RESPONSE3.url), allow_redirects=True, verify=True)

                    if QUERY == 'Likes':
                        MEDIA_USERNAME = re.search(r'name="mediaUsername".*?value="([\w\.\-]+)"', RESPONSE4.text).group(1)
                        MEDIA_CODE = re.search(r'name="mediaCode".*?value="([\w]+)"', RESPONSE4.text).group(1)
                        ADET = re.search(r'name="adet".*?value="(\d+)"', RESPONSE4.text).group(1)
                        MEDIA_ID = re.search(r'name="mediaID".*?value="([\w_]+)"', RESPONSE4.text).group(1)
                        MEDIA_USER_ID = re.search(r'name="mediaUserID".*?value="([\w]+)"', RESPONSE4.text).group(1)
                    elif QUERY == 'Follower':
                        MEDIA_USERNAME = re.search(r'name="userName".*?value="([\w\.\-]+)"', RESPONSE4.text).group(1)
                        ADET = re.search(r'name="adet".*?value="(\d+)"', RESPONSE4.text)
                        ADET = ADET.group(1) if ADET else 15
                        MEDIA_USER_ID = re.search(r'name="userID".*?value="([\w]+)"', RESPONSE4.text).group(1)
                        MEDIA_CODE, MEDIA_ID = ('', f'{MEDIA_USER_ID}')
                    else:
                        MEDIA_CODE = re.search(r'name="mediaCode".*?value="([\w]+)"', RESPONSE4.text).group(1)
                        ADET = re.search(r'name="adet".*?value="(\d+)"', RESPONSE4.text)
                        ADET = ADET.group(1) if ADET else 400
                        MEDIA_ID = re.search(r'name="mediaID".*?value="([\w_]+)"', RESPONSE4.text).group(1)
                        MEDIA_USERNAME, MEDIA_USER_ID = ('', '')

                    RESPONSE4_COOKIES = ('; '.join([str(key) +'='+ str(value) for key, value in SESSION.cookies.get_dict().items()]))
                    LOOPING += 1
                    self.NEXT_LIKES_FOLLOWERS_VIEWS(SESSION, HOST_NAME, TAUTAN, MEDIA_USERNAME, MEDIA_CODE, ADET, MEDIA_ID, MEDIA_USER_ID, RESPONSE4_COOKIES, TYPE, QUERY)
                elif 'checkpoint_required' in RESPONSE3.text:
                    printf(f"[bold bright_black]   ──>[bold red] YOUR INSTAGRAM HAS BEEN DETECTED BY CHECKPOINT!                 ", end='\r')
                    time.sleep(4.5)
                    CHECKPOINT.append(f'{RESPONSE3.status_code}')
                    return (False)
                else:
                    printf(f"[bold bright_black]   ──>[bold red] CAN'T FIND {str(QUERY).upper()} FORM!                         ", end='\r')
                    time.sleep(4.5)
                    return (False)

    def NEXT_LIKES_FOLLOWERS_VIEWS(self, SESSION, HOST_NAME, TAUTAN, MEDIA_USERNAME, MEDIA_CODE, ADET, MEDIA_ID, MEDIA_USER_ID, RESPONSE4_COOKIES, TYPE, QUERY):
        global SUKSES, GAGAL
        try:
            STOP, LOOP, SUCCESS, PERCOBAAN = False, 0, [], 0
            while STOP == False:
                if QUERY == 'Follower':
                    PAYLOAD = {
                        'userName': f'{MEDIA_USERNAME}',
                        'adet': f'{ADET}',
                        'userID': f'{MEDIA_USER_ID}',
                    }
                elif QUERY == 'Likes':
                    PAYLOAD = {
                        'mediaUsername': f'{MEDIA_USERNAME}',
                        'mediaCode': f'{MEDIA_CODE}',
                        'adet': f'{ADET}',
                        'mediaID': f'{MEDIA_ID}',
                        'mediaUserID': f'{MEDIA_USER_ID}',
                    }
                else:
                    PAYLOAD = {
                        'mediaID': f'{MEDIA_USER_ID}',
                        'adet': f'{ADET}',
                        'mediaCode': f'{MEDIA_CODE}',
                    }
                SESSION.headers.update({
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Content-Length': '{}'.format(len(str(PAYLOAD))),
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Referer': 'https://{}/tools/{}/{}'.format(HOST_NAME, TYPE, MEDIA_ID),
                    'Origin': 'https://{}'.format(HOST_NAME),
                    'Cookie': '{}'.format(RESPONSE4_COOKIES)
                })
                RESPONSE5 = SESSION.post('https://{}/tools/{}/{}?formType=send'.format(HOST_NAME, TYPE, MEDIA_ID), data=PAYLOAD, allow_redirects=True, verify=True)
                LOOP += 1
                if '"status":"success"' in RESPONSE5.text:
                    SUCCESS.append(f'{RESPONSE5.status_code}')
                    printf(f"[bold bright_black]   ──>[bold green] SENDING {str(QUERY).upper()}, WALKING {LOOP}!                         ", end='\r')
                    time.sleep(3.5)
                    continue
                elif '"nocreditleft"' in RESPONSE5.text:
                    printf(f"[bold bright_black]   ──>[bold red] YOU ARE OUT OF CREDITS!                         ", end='\r')
                    time.sleep(3.5)
                    STOP = True
                elif '"nouserleft"' in RESPONSE5.text:
                    printf(f"[bold bright_black]   ──>[bold red] NO USERS IN DATABASE!                           ", end='\r')
                    time.sleep(3.5)
                    STOP = True
                elif 'Error Occurred!' in RESPONSE5.text:
                    PERCOBAAN += 1
                    if int(PERCOBAAN) >= 10:
                        printf(f"[bold bright_black]   ──>[bold red] ERROR WHILE SENDING {str(QUERY).upper()}!               ", end='\r')
                        time.sleep(3.5)
                        STOP = True
                    else:
                        continue
                else:
                    printf(f"[bold bright_black]   ──>[bold red] FAILED TO SEND {str(QUERY).upper()}!                           ", end='\r')
                    time.sleep(3.5)
                    continue
            if len(SUCCESS) != 0:
                TAMPILKAN['COUNT'] += 1
                if TAMPILKAN['COUNT'] >= 2:
                    self.JUMLAH = '30' if QUERY == 'Follower' else '20' if QUERY == 'Likes' else '200'
                    self.LINK = (f'https://www.instagram.com/{MEDIA_USERNAME}' if QUERY == 'Follower' else TAUTAN)
                    printf(Panel(f"""[bold white]Status :[italic green] Successfully sending {str(QUERY).capitalize()}![/]
[bold white]Link :[bold red] {self.LINK}
[bold white]Jumlah :[bold yellow] + {self.JUMLAH}""", width=63, style="bold bright_black", title="> [Sukses] <"))
                    SUKSES += 1
                else:
                    SUKSES += 1
            else:
                GAGAL += 1
            return (True)
        except (KeyboardInterrupt):
            printf(f"[bold white]                            ", end='\r')
            time.sleep(2.5)
            return (False)

if __name__ == '__main__':
    try:
        if os.path.exists("Penyimpanan/Subscribe.json") == False:
            youtube_url = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/Gramtakipci/main/Penyimpanan/Youtube.json').text)['Link']
            os.system(f'xdg-open {youtube_url}')
            with open('Penyimpanan/Subscribe.json', 'w') as w:
                w.write(json.dumps({
                    "Status": True
                }))
            w.close()
            time.sleep(2.5)
        os.system('git pull')
        FEATURE()
    except (Exception) as e:
        printf(Panel(f"[bold red]{str(e).capitalize()}!", width=63, style="bold bright_black", title="> [Error] <"))
        sys.exit(1)
    except (KeyboardInterrupt):
        sys.exit(1)