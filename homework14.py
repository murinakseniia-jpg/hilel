import time
import random
import threading

files = ["photo.jpg", "document.pdf", "video.mp4", "archive.zip", "music.mp3"]

def downolad_file(file_name):
    print(f"Початок завантаження {file_name}...")
    time.sleep(random.randint(1, 3))
    print(f"Завершено: {file_name}")

start = time.perf_counter()

for file_name in files:
    downolad_file(file_name)

t_time = time.perf_counter() - start
print(f"Послідовне завантаження: {t_time:.2f} секунд.")

threads = []

for file_name in files:
    thread = threading.Thread(target=downolad_file, args=(file_name))
    threads.append(thread)

p_start = time.perf_counter()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

p_time = time.perf_counter() - p_start
print(f"Паралельне завантаження: {p_time:.2f} секунд.")

dif = t_time - p_time
print(f"Різниця в часі: {dif:.2f} секунд.")