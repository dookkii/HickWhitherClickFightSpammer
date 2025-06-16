import requests
import time

URL = "https://hw.io.vn/"

cookies = {
  "session": ""
}

def call(path):
  return requests.get(URL + path, cookies=cookies)

def call_clicks():
  return call("/api/click")

def call_level_up():
  return call("/api/level_up")

def main(no = None, delta_time = 0.001):
  while True:
    try:
      print(call_clicks().text)
      request_result = call_clicks().json()
      
      if no:
        print(f"Thread No.{no}: {request_result}")
      else:
        print(request_result)

      clicks = request_result.get("click")
      next_level = request_result.get("next_level")
      next_level = next_level if isinstance(next_level, int) else 0
      
      if next_level <= clicks:
        call_level_up()

      time.sleep(delta_time)
    except KeyboardInterrupt as error:
      print("BYE!")
      break
    except Exception as e:
      print(e)
      break

if __name__ == "__main__":
  main()
