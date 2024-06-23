from instabot import Bot
import time

username = 'username'
password = 'password'

# Inisialisasi bot
bot = Bot()
bot.login(username=username, password=password)

# Ambil daftar pengikut
followers = bot.get_user_followers(username)

# Kurangi jumlah operasi yang dilakukan
batch_size = 10  # Ubah sesuai kebutuhan
num_batches = 3  # Ubah sesuai kebutuhan

# Loop untuk setiap batch
for batch_index in range(num_batches):
    start_index = batch_index * batch_size
    end_index = (batch_index + 1) * batch_size
    batch = followers[start_index:end_index]

    # Loop untuk setiap pengikut dalam batch
    for follower in batch:
        # Periksa apakah pengikut ini adalah bot
        if follower != 'your_real_followers':
            # Hapus pengikut
            bot.unfollow(follower)
            print(f"Unfollowed: {follower}")
            time.sleep(10)  # Jeda 10 detik antara setiap penghapusan untuk menghindari pemblokiran

# Logout dari akun
bot.logout()
