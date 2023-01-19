import requests, time, json, random
from colorama import Fore

# Isi channel ID 
channel = ['1065535137145688104','1065535155458027540']

# Tulis Kata Kata Mutiaramu
text = ['test1','test2','test3']

# Isi Token
token = ['NDI1MjY4MzE3NTI0MDY2MzA1.GNBDwf.P-jcjyQ0gNrfA0bp5-HOONYb3Hsl5qfOkIzC58','OTA5MDE2MjQ5NjQyNjgwMzUw.GUKYcc.W3znAcPnfo8P6CT7P43bnlJAke0_VPIWeYehS0']

while True:

    # Pilih channel ID secara random
    channel_id = random.choice(channel_ids)

    payload = {
        'content': random.choice(words)
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
            # Tidak ada pesan lagi di channel, berhenti menghapus pesan
            break
        else:
            # Tambahkan jeda selama 20 detik sebelum menghapus pesan
            time.sleep(0) 

            # Hapus pesan terbaru di channel
            message_id = messages[0]['id']
            response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
            if response.status_code == 204:
                print(Fore.GREEN + f'Pesan dengan ID {message_id} berhasil dihapus')
            else:
                print(Fore.RED + f'Gagal menghapus pesan dengan ID {message_id}: {response.status_code}')
    else:
        print(f'Gagal mendapatkan pesan di channel: {response.status_code}')

            # Angka 30 adalah countdown untuk next text sesuaikan dengan keinginan kalian
    for i in range(30): 
        print(Fore.WHITE + f"Sabar ya ganteng {30-i}", end='\r')
        time.sleep(1) 
