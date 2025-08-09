#!/usr/bin/env python3
import subprocess
import shlex
import os

# Helper
def run_cmd(cmd):
    try:
        p = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
        return p.stdout if p.stdout else p.stderr
    except Exception as e:
        return f"Error: {e}"

# Menu
menu = {
    1: "Ping Test",
    2: "Traceroute",
    3: "Port Scan (nmap)",
    4: "Check Local IP",
    5: "Check Public IP",
    6: "WiFi Scan (Nearby)",
    7: "Current WiFi Info",
    0: "Exit"
}

while True:
    print("\n=== Termux Network Toolkit ===")
    for k, v in menu.items():
        print(f"{k}. {v}")

    try:
        choice = int(input("\nSelect option: "))
    except:
        print("Invalid choice.")
        continue

    if choice == 0:
        break
    elif choice == 1:
        host = input("Enter domain/IP to ping: ")
        print(run_cmd(f"ping -c 4 {host}"))
    elif choice == 2:
        host = input("Enter domain/IP for traceroute: ")
        print(run_cmd(f"traceroute {host}"))
    elif choice == 3:
        target = input("Enter target IP/domain: ")
        print(run_cmd(f"nmap {target}"))
    elif choice == 4:
        print(run_cmd("ifconfig"))
    elif choice == 5:
        print(run_cmd("curl ifconfig.me"))
    elif choice == 6:
        print(run_cmd("termux-wifi-scaninfo"))
    elif choice == 7:
        print(run_cmd("termux-wifi-connectioninfo"))
    else:
        print("Invalid option.")
