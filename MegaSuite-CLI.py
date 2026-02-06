import os
import sys
import threading
import platform
import requests

# --- ලයිබ්‍රරි පරීක්ෂාව ---
try:
    from scapy.all import ARP, Ether, srp, sniff
except ImportError:
    print("[!] Scapy is not installed. Run: pip install scapy")

# --- 1. CLI VERSION (ටර්මිනල් එකේ පෙනෙන විදිහ) ---
class MegaCLI:
    def _init_(self):
        self.G = '\033[92m' # Green
        self.R = '\033[91m' # Red
        self.Y = '\033[93m' # Yellow
        self.W = '\033[0m'  # White

    def banner(self):
        os.system('clear' if os.name != 'nt' else 'cls')
        print(f"""{self.G}
    _  __                 __       _ _     
   /  |/  /_  __ __ / _/_  _() /__ 
  / /|/ / _ \/ _ `/ _ `/\_ \/ / / / / __/ _ \\
 / /  / /  _/ // / // /_/ / // / / //  _/
//  //\_/\_, /\,//_/\,//\/\__/ 
            /__/  {self.Y}PRO EDITION v5.0{self.W}
        """)

    def run(self):
        while True:
            self.banner()
            print(f"1. {self.G}Network Scanner{self.W}")
            print(f"2. {self.G}Traffic Logger (Sniffer){self.W}")
            print(f"3. {self.G}Web Intelligence (Recon){self.W}")
            print(f"4. {self.R}Exit{self.W}")
            
            choice = input(f"\n{self.Y}Select an option > {self.W}")
            
            if choice == '1': self.network_scan()
            elif choice == '2': self.packet_sniffer()
            elif choice == '3': self.web_recon()
            elif choice == '4': break

    def network_scan(self):
        target = input(f"\n{self.Y}[?]{self.W} Enter IP Range (e.g. 192.168.1.1/24): ")
        print(f"{self.G}[*]{self.W} Scanning... (Please use sudo for better results)")
        try:
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target), timeout=2, verbose=False)
            print(f"\n{self.G}IP Address\t\tMAC Address{self.W}")
            for s, r in ans:
                print(f"{r.psrc}\t\t{r.hwsrc}")
        except Exception as e: print(f"{self.R}[!] Error: {e}{self.W}")
        input(f"\n{self.Y}Press Enter to return...{self.W}")

    def packet_sniffer(self):
        print(f"\n{self.G}[*]{self.W} Starting Traffic Log (Press Ctrl+C to stop)...")
        try:
            sniff(prn=lambda x: print(f"{self.Y}[PKT]{self.W} {x.summary()}"), store=0)
        except Exception as e: print(f"{self.R}[!] Root/Admin required!{self.W}")

    def web_recon(self):
        domain = input(f"\n{self.Y}[?]{self.W} Enter Domain (e.g. google.com): ")
        try:
            data = requests.get(f"https://ipinfo.io/{domain}/json").json()
            for k, v in data.items(): print(f"{self.G}{k}:{self.W} {v}")
        except: print(f"{self.R}[!] Recon failed.{self.W}")
        input(f"\n{self.Y}Press Enter to return...{self.W}")

# --- 2. SMART LOADER ---
if _name_ == "_main_":
    # Android (Termux) හෝ Linux Terminal එකකදී නිතරම CLI එක රන් වෙයි
    if platform.system() == "Android" or len(sys.argv) > 1 or os.isatty(sys.stdin.fileno()):
        cli = MegaCLI()
        cli.run()
    else:
        # GUI එක පූරණය කිරීම (Windows/Desktop සඳහා)
        try:
            import tkinter as tk
            # මෙහි ඔබ සතු GUI කේතය ඇතුළත් කළ හැකිය
            print("[*] GUI Mode is starting...")
        except ImportError:
            cli = MegaCLI()
            cli.run()
