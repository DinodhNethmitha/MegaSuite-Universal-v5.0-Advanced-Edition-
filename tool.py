import os
import sys
import platform
import threading
import itertools
import requests

# --- PLATFORM CHECK & GUI IMPORT ---
# පද්ධතිය හඳුනාගෙන GUI අවශ්‍යද නැද්ද යන්න තීරණය කරයි
HAS_GUI = False
try:
    if platform.system() != "Android" and "termux" not in sys.executable.lower():
        import tkinter as tk
        from tkinter import ttk, messagebox, filedialog
        HAS_GUI = True
except ImportError:
    HAS_GUI = False

# --- NETWORK CORE ---
try:
    from scapy.all import ARP, Ether, srp, sniff, RadioTap, Dot11, Dot11Deauth, sendp
except ImportError:
    print("[!] Scapy not found. Network tools will be limited.")

# ------------------------------------------------------------------
# 1. ADVANCED CLI VERSION (For Android/Termux)
# ------------------------------------------------------------------
class MegaCLI:
    def _init_(self):
        self.G, self.R, self.Y, self.W = '\033[92m', '\033[91m', '\033[93m', '\033[0m'
        
    def banner(self):
        os.system('clear' if os.name != 'nt' else 'cls')
        print(f"{self.G}███╗   ███╗███████╗ ██████╗  █████╗ ███████╗██╗   ██╗██╗████████╗███████╗")
        print(f"████╗ ████║██╔════╝██╔════╝ ██╔══██╗██╔════╝██║   ██║██║╚══██╔══╝██╔════╝")
        print(f"██╔████╔██║█████╗  ██║  ███╗███████║███████╗██║   ██║██║   ██║   █████╗  ")
        print(f"██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║╚════██║██║   ██║██║   ██║   ██╔══╝  ")
        print(f"██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║███████║╚██████╔╝██║   ██║   ███████╗")
        print(f"╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝{self.W}")
        print(f"                 {self.Y}Universal Security Suite v5.0 | By YourName{self.W}\n")

    def run(self):
        while True:
            self.banner()
            print(f"1. {self.G}Network Scanner{self.W}")
            print(f"2. {self.G}Packet Logger{self.W}")
            print(f"3. {self.R}WiFi Deauth (Root Required){self.W}")
            print(f"4. {self.G}Web Intelligence (Recon){self.W}")
            print(f"5. {self.Y}Exit{self.W}")
            
            choice = input(f"\n{self.Y}Select Option > {self.W}")
            if choice == '1': self.scan()
            elif choice == '2': self.sniff()
            elif choice == '4': self.recon()
            elif choice == '5': break
            input(f"\n{self.Y}Press Enter to return...{W}")

    def scan(self):
        ip = input(f"{self.Y}[?]{self.W} Enter IP Range: ")
        print(f"{self.G}[*]{self.W} Scanning...")
        # Scapy logic here... (Simplified for display)

    def recon(self):
        domain = input(f"{self.Y}[?]{self.W} Enter Domain: ")
        res = requests.get(f"https://ipinfo.io/{domain}/json").json()
        for k, v in res.items(): print(f"{self.G}{k}:{self.W} {v}")

# ------------------------------------------------------------------
# 2. ADVANCED GUI VERSION (For Windows/Linux)
# ------------------------------------------------------------------
if HAS_GUI:
    class MegaGUI:
        def _init_(self, root):
            self.root = root
            self.root.title("MegaSuite Universal v5.0")
            self.root.geometry("900x700")
            self.root.configure(bg="#0f172a")
            
            # Use Style for Dark Theme
            style = ttk.Style()
            style.theme_use('clam')
            style.configure("TNotebook", background="#0f172a", borderwidth=0)
            style.configure("TNotebook.Tab", background="#1e293b", foreground="white", padding=[15, 5])
            style.map("TNotebook.Tab", background=[("selected", "#3b82f6")])

            # Header
            header = tk.Label(root, text="MEGASUITE PRO SECURITY", font=("Orbitron", 24, "bold"), bg="#0f172a", fg="#3b82f6")
            header.pack(pady=20)

            # Tab Control
            self.nb = ttk.Notebook(root)
            self.nb.pack(fill="both", expand=True, padx=20, pady=10)

            self.tab_scan = ttk.Frame(self.nb)
            self.tab_sniff = ttk.Frame(self.nb)
            self.tab_deauth = ttk.Frame(self.nb)
            self.tab_recon = ttk.Frame(self.nb)

            self.nb.add(self.tab_scan, text="📡 NETWORK SCAN")
            self.nb.add(self.tab_sniff, text="📊 TRAFFIC LOG")
            self.nb.add(self.tab_deauth, text="⚔️ ATTACK MODES")
            self.nb.add(self.tab_recon, text="🌐 WEB INTELLIGENCE")

            self.init_scan_ui()
            # ... (අනෙක් UI කොටස් කලින් වගේම මෙතැනට ඇතුළත් වේ)

        def init_scan_ui(self):
            lbl = tk.Label(self.tab_scan, text="Target IP Range:", font=("Arial", 12))
            lbl.pack(pady=10)
            self.ip_ent = tk.Entry(self.tab_scan, width=40, font=("Consolas", 12))
            self.ip_ent.insert(0, "192.168.1.1/24")
            self.ip_ent.pack()
            
            btn = tk.Button(self.tab_scan, text="START SCAN", bg="#3b82f6", fg="white", font=("Arial", 12, "bold"))
            btn.pack(pady=20)

# ------------------------------------------------------------------
# 3. SMART BOOT LOADER
# ------------------------------------------------------------------
if _name_ == "_main_":
    if HAS_GUI:
        root = tk.Tk()
        app = MegaGUI(root)
        root.mainloop()
    else:
        # If no GUI (Termux/Server), launch CLI
        cli = MegaCLI()
        cli.run()