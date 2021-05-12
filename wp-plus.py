import urllib.request
import json, datetime, random, time, os, sys
import string
from rich import pretty, print
from rich.console import Console
import colors as styles

pretty.install()
console = Console()

try:
    os.system("cls" if os.name == "nt" else "clear")
    console.print(
        "This Script is written by Aliilpro and modified by minlaxz ...",
        style=styles.dodgetblue,
    )
    referrer = console.input("Enter your [i]Warp[/i] [bold red]ID[/] :smiley: :")
except KeyboardInterrupt:
    print("[yellow]\nUser aborted.[/yellow]")
    exit()


def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return "".join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(f"[red]{error}[/red]")


def digitString(stringLength):
    try:
        digit = string.digits
        return "".join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(f"[red]{error}[/red]")


url = f"https://api.cloudflareclient.com/v0a{digitString(3)}/reg"


def run():
    try:
        install_id = genString(22)
        body = {
            "key": "{}=".format(genString(43)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
            "type": "Android",
            "locale": "es_ES",
        }
        data = json.dumps(body).encode("utf8")
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "api.cloudflareclient.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.1",
        }
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception as error:
        print(f"[red]{error}[/red]")


def reversCount():
    try:
        for i in range(18, 0, -1):
            print(f"\r{i}", end=" ")
            sys.stdout.flush()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nUser stopped.")
        exit()


g = 0
b = 0
while True:
    result = run()
    if result == 200:
        g = g + 1
        os.system("cls" if os.name == "nt" else "clear")
        print("")
        print(f"[green] [-] WORK ON ID: {referrer}[/green]")
        print(f"[:)] {g} GB has been successfully added to your account.")
        print(f"[#] Total: {g} GB added. {b} Bad request(s)")
        print("[*] After 18 seconds, a new request will be sent.")
        reversCount()

    elif g == 10 or b == 5:
        print("Script is stopped.")
        print(f"[#] Total: {g} GB added. {b} Bad request(s)")
        raise KeyboardInterrupt

    else:
        b = b + 1
        os.system("cls" if os.name == "nt" else "clear")
        print("")
        print(result)
        print("[red][:(] Failed to connect to the server.[/red]")
        print(f"[#] Total: {g} GB added. {b} Bad request(s)")
        print("[*] After 20 seconds, a new request will be sent.")
        reversCount()
