import tkinter as tk
from tkinter import messagebox
import os
import subprocess

def update_environment():
    # Get all inputs
    ip1 = entry_ip1.get().strip()
    ip2 = entry_ip2.get().strip()
    ip3 = entry_ip3.get().strip()
    ms01 = entry_ms01.get().strip()
    ms02 = entry_ms02.get().strip()
    dc1 = entry_dc1.get().strip()
    standalone_domain1 = entry_standalone_domain1.get().strip()
    standalone_domain2 = entry_standalone_domain2.get().strip()
    standalone_domain3 = entry_standalone_domain3.get().strip()
    ad_domain = entry_ad_domain.get().strip()

    # Function to check if a line already exists in a file
    def line_exists(file_path, line):
        if not os.path.exists(file_path):
            return False
        with open(file_path, 'r') as file:
            return line in file.read()

    # Function to check if a variable is already defined in ~/.zshrc
    def variable_exists(file_path, variable):
        if not os.path.exists(file_path):
            return False
        with open(file_path, 'r') as file:
            return f"export {variable}=" in file.read()

    # Check for duplicate variables in ~/.zshrc
    duplicate_vars = []
    if ip1 and variable_exists(os.path.expanduser('~/.zshrc'), 'ip1'):
        duplicate_vars.append('ip1')
    if ip2 and variable_exists(os.path.expanduser('~/.zshrc'), 'ip2'):
        duplicate_vars.append('ip2')
    if ip3 and variable_exists(os.path.expanduser('~/.zshrc'), 'ip3'):
        duplicate_vars.append('ip3')
    if ms01 and variable_exists(os.path.expanduser('~/.zshrc'), 'ms01'):
        duplicate_vars.append('ms01')
    if ms02 and variable_exists(os.path.expanduser('~/.zshrc'), 'ms02'):
        duplicate_vars.append('ms02')
    if dc1 and variable_exists(os.path.expanduser('~/.zshrc'), 'dc1'):
        duplicate_vars.append('dc1')

    # If duplicates exist, show a warning and exit
    if duplicate_vars:
        messagebox.showwarning(
            "Duplicate Variables",
            f"The following variables already exist in ~/.zshrc: {', '.join(duplicate_vars)}\n"
            "Please delete the old entries before adding new ones."
        )
        return

    # Update ~/.zshrc with non-empty IPs
    zshrc_path = os.path.expanduser('~/.zshrc')
    with open(zshrc_path, 'a') as zshrc:
        if ip1:
            zshrc.write(f"export ip1={ip1}\n")
        if ip2:
            zshrc.write(f"export ip2={ip2}\n")
        if ip3:
            zshrc.write(f"export ip3={ip3}\n")
        if ms01:
            zshrc.write(f"export ms01={ms01}\n")
        if ms02:
            zshrc.write(f"export ms02={ms02}\n")
        if dc1:
            zshrc.write(f"export dc1={dc1}\n")

    # Update /etc/hosts with non-empty IPs and domain names (avoid duplicates)
    hosts_path = '/etc/hosts'
    with open(hosts_path, 'a') as hosts:
        if ip1 and standalone_domain1 and not line_exists(hosts_path, f"{ip1} {standalone_domain1}\n"):
            hosts.write(f"{ip1} {standalone_domain1}\n")
        if ip2 and standalone_domain2 and not line_exists(hosts_path, f"{ip2} {standalone_domain2}\n"):
            hosts.write(f"{ip2} {standalone_domain2}\n")
        if ip3 and standalone_domain3 and not line_exists(hosts_path, f"{ip3} {standalone_domain3}\n"):
            hosts.write(f"{ip3} {standalone_domain3}\n")
        if dc1 and ad_domain and not line_exists(hosts_path, f"{dc1} {ad_domain}\n"):
            hosts.write(f"{dc1} {ad_domain}\n")

    # Show success message and prompt to source ~/.zshrc
    messagebox.showinfo(
        "Success",
        "Environment variables and /etc/hosts updated successfully!\n\n"
        "Please run the following command in your terminal to apply the changes:\n"
        "source ~/.zshrc"
    )

    # Close the app after clicking OK
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Env Helper")

# IP Inputs
tk.Label(root, text="IP1:").grid(row=0, column=0)
entry_ip1 = tk.Entry(root)
entry_ip1.grid(row=0, column=1)

tk.Label(root, text="IP2:").grid(row=1, column=0)
entry_ip2 = tk.Entry(root)
entry_ip2.grid(row=1, column=1)

tk.Label(root, text="IP3:").grid(row=2, column=0)
entry_ip3 = tk.Entry(root)
entry_ip3.grid(row=2, column=1)

tk.Label(root, text="MS01:").grid(row=3, column=0)
entry_ms01 = tk.Entry(root)
entry_ms01.grid(row=3, column=1)

tk.Label(root, text="MS02:").grid(row=4, column=0)
entry_ms02 = tk.Entry(root)
entry_ms02.grid(row=4, column=1)

tk.Label(root, text="DC1:").grid(row=5, column=0)
entry_dc1 = tk.Entry(root)
entry_dc1.grid(row=5, column=1)

# Domain Inputs
tk.Label(root, text="Standalone Domain 1:").grid(row=6, column=0)
entry_standalone_domain1 = tk.Entry(root)
entry_standalone_domain1.grid(row=6, column=1)

tk.Label(root, text="Standalone Domain 2:").grid(row=7, column=0)
entry_standalone_domain2 = tk.Entry(root)
entry_standalone_domain2.grid(row=7, column=1)

tk.Label(root, text="Standalone Domain 3:").grid(row=8, column=0)
entry_standalone_domain3 = tk.Entry(root)
entry_standalone_domain3.grid(row=8, column=1)

tk.Label(root, text="AD Domain:").grid(row=9, column=0)
entry_ad_domain = tk.Entry(root)
entry_ad_domain.grid(row=9, column=1)

# OK Button
tk.Button(root, text="OK", command=update_environment).grid(row=10, column=0, columnspan=2)

root.mainloop()
