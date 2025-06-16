from click_fight import main as call_function
import threading
import time

n = 100
delta_time = 0.00001
threads = [threading.Thread(target=call_function, args=[i, delta_time]) for i in range(n)]

for thread in threads:
  # thread.daemon = True
  thread.start()

# try:
#   while True:
#     time.sleep(delta_time)
# except KeyboardInterrupt:
#   for thread in threads:
#     thread.join()
  
#   print("BYE!!!!!")
# except Exception as e:
#   print(e)
