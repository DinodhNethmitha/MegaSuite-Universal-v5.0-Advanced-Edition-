import os
import sys
import platform
import requests
import tkinter as tk
from tkinter import ttk, messagebox

# --- GUI පරීක්ෂාව ---
HAS_GUI = True

# --- 1. CORE FUNCTIONS (වැඩ කරන කොටස්) ---
def start_scan(ip_range):
    print(f"Scanning {ip_range}...")
    messagebox.showinfo("Scanner", f"Scanning started for: {ip_range}")

def start_recon(domain):
    try:
        res = requests.get(f"https://ipinfo.io/{domain}/json").json()
        info = "\n".join([f"{k}: {v}" for k, v in res.items()])
        messagebox.showinfo("Web Recon", info)
    except:
        messagebox.showerror("Error", "Could not fetch data.")

# --- 2. MAIN GUI CLASS ---
class MegaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MegaSuite Universal PRO")
        self.root.geometry("800x550")
        self.root.configure(bg="#0f172a")

        # Tabs සෑදීම
        self.nb = ttk.Notebook(root)
        self.nb.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_scan = ttk.Frame(self.nb)
        self.tab_log = ttk.Frame(self.nb)
        self.tab_attack = ttk.Frame(self.nb)
        self.tab_web = ttk.Frame(self.nb)

        self.nb.add(self.tab_scan, text="📡 NETWORK SCAN")
        self.nb.add(self.tab_log, text="📊 TRAFFIC LOG")
        self.nb.add(self.tab_attack, text="⚔️ ATTACK MODES")
        self.nb.add(self.tab_web, text="🌐 WEB INTELLIGENCE")

        # සෑම Tab එකක්ම පිරවීම
        self.init_scan()
        self.init_log()
        self.init_attack()
        self.init_web()

    def init_scan(self):
        tk.Label(self.tab_scan, text="IP Range:", font=("Arial", 11)).pack(pady=10)
        self.ip_ent = tk.Entry(self.tab_scan, width=30)
        self.ip_ent.insert(0, "192.168.1.1/24")
        self.ip_ent.pack()
        tk.Button(self.tab_scan, text="RUN SCAN", bg="#3b82f6", fg="white", 
                  command=lambda: start_scan(self.ip_ent.get())).pack(pady=10)

    def init_log(self):
        self.log_txt = tk.Text(self.tab_log, height=15, width=80, bg="black", fg="lime")
        self.log_txt.pack(padx=10, pady=10)
        tk.Button(self.tab_log, text="START SNIFFING", bg="green", fg="white").pack()

    def init_attack(self):
        tk.Label(self.tab_attack, text="Target MAC:", font=("Arial", 11)).pack(pady=5)
        self.mac_ent = tk.Entry(self.tab_attack, width=30)
        self.mac_ent.pack()
        tk.Button(self.tab_attack, text="DEAUTH ATTACK", bg="red", fg="white").pack(pady=10)

    def init_web(self):
        tk.Label(self.tab_web, text="Domain Name:", font=("Arial", 11)).pack(pady=5)
        self.dom_ent = tk.Entry(self.tab_web, width=30)
        self.dom_ent.pack()
        tk.Button(self.tab_web, text="GET INFO", bg="#8b5cf6", fg="white",
                  command=lambda: start_recon(self.dom_ent.get())).pack(pady=10)

# --- 3. EXECUTION ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MegaGUI(root)
    root.mainloop()
