import time
import requests
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

banner = pyfiglet.figlet_format("Reloaded")

print(Fore.GREEN + Style.BRIGHT + banner)

print("url ex.: https://www.example.com")

url = input("Enter url: ")

refresh_rate = int(input("Enter refresh rate: "))

session = requests.Session()

try:
    while True:
                response = session.get(url)

                print(f"Requested Page | Status: {response.status_code}")

                time.sleep(refresh_rate)
except KeyboardInterrupt:
    print("Action Stopped")
