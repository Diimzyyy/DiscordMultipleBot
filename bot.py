import requests, time, json, random
from colorama import Fore

# Isi channel ID 
channel_ids = ['Channel1','Channel2']

# Tulis Kata Kata Mutiaramu
text = ['text1','text2','text3']

# Isi Token
token = ['TOKEN_DISCORD1','TOKEN_DISCORD2']

while True:

    # Pilih channel ID secara random
    channel_id = random.choice(channel_ids)

    payload = {
        'content': random.choice(text)
    }


    headers = {
        'Authorization': random.choice(token)
    }
    

    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
    print(Fore.WHITE + "Sent message: ")
    print(Fore.YELLOW + payload['content'])
    
    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

    if response.status_code == 200:
        messages = response.json()
        if len(messages) == 0:
                        
            break
        else:
            # Jeda 2 Detik Sebelum Menghapus Pesan
            time.sleep(2) 

            # Hapus pesan terbaru di channel
            message_id = messages[0]['id']
            response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
            if response.status_code == 204:
                print(Fore.GREEN + f'Pesan dengan ID {message_id} berhasil dihapus')
            else:
                print(Fore.RED + f'Gagal menghapus pesan dengan ID {message_id}: {response.status_code}')
    else:
        print(f'Gagal mendapatkan pesan di channel: {response.status_code}')

            # Angka 3 adalah countdown untuk next text sesuaikan dengan keinginan kalian
    for i in range(3): 
        print(Fore.WHITE + f"Menunggu {3-i} Detik", end='\r')
        time.sleep(1) 
