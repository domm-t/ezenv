# Env Helper - OSCP Global Environment Manager

A GUI tool to simplify managing environment variables and `/etc/hosts` entries during penetration testing exercises like OSCP.

![Demo Screenshot](ezenv.gif)

## Features ✨
- **GUI Interface**: Easy input for IPs and domain names
- **Environment Variables**: Auto-updates `~/.zshrc` with:
  - Standalone IPs (`ip1`, `ip2`, `ip3`)
  - AD Network IPs (`ms01`, `ms02`, `dc1`)
- **Hosts File Management**: Updates `/etc/hosts` with domain mappings
- **Smart Validation**:
  - Prevents duplicate entries
  - Skips blank fields
  - Blocks overwrites without cleanup
- **Safety First**: Appends to files without overwriting existing content

## Installation ⚙️
```bash
# Clone repository
git clone https://github.com/domm-t/ezenv.git
cd ezenv

# Install dependencies
sudo apt install python3-tk

# Make script executable
chmod +x ezenv.py

# Make the script global
sudo cp ezenv.py /usr/local/bin/ezenv
sudo chmod +x /usr/local/bin/ezenv

# Run tool globally!
ezenv
