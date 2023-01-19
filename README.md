# BotDiscord

## Tutorial Ambil Discord Token 
- 1. Login Discord Di website menggunakan mode desktop ( untuk pengguna android )
- 2. Paste Code ini 
```
javascript:var i = document.createElement('iframe');i.onload = function(){var localStorage = i.contentWindow.localStorage;prompt('Discotd Token', localStorage.getItem('token').replace(/["]+/g, ''));};document.body.appendChild(i);
```
- 3. Jika javascript terhapus sendiri silahkan tulis manual
- 4. Jika sudah muncul token Discord Silahkan copy dan paste ke file bot

## Tutorial Install
- 1. Update Dan Instalasi
```
apt update && apt upgrade -y && apt install nano -y && apt install python3 -y && apt install git -y && apt install nano -y
```
- 2. Ambil File
```
git clone https://github.com/Diimzyyy/DiscordMultipleBot
```
- 3. Masuk File Directory
```
cd DiscordMultipleBot
```
- 4. Edit Text , Channel & Token Discord
```
nano bot.py
```
- 5. Running Dengan Commands
```
python bot.py
```


## Note 
- 1. 
