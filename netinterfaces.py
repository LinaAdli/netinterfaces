import os
import sys
import subprocess

__version__ = "0.1.0"

def get_interfaces():
    platform = sys.platform
    try:
        if platform.startswith('linux'):
            return _linux_interfaces()
        if platform.startswith('win'):
            return _windows_interfaces()
        if platform == 'darwin':
            return _mac_interfaces()
        raise NotImplementedError()
    except Exception:
        return []

def _linux_interfaces():
    net_path = "/sys/class/net"
    return os.listdir(net_path) if os.path.exists(net_path) else []

def _windows_interfaces():
    try:
        output = subprocess.check_output(['netsh', 'interface', 'show', 'interface'],stderr=subprocess.STDOUT,text=True,encoding='utf-8',errors='ignore')
    except subprocess.CalledProcessError:
        return []
    interfaces = []
    in_table = False
    for line in output.split('\n'):
        line = line.strip()
        if line.startswith('---'):
            in_table = True
            continue
        if in_table and line:
            parts = line.split()
            if len(parts) >= 4:
                interface_name = ' '.join(parts[3:])
                interfaces.append(interface_name)
    return interfaces

def _mac_interfaces():
    try:
        output = subprocess.check_output(['ifconfig'],stderr=subprocess.STDOUT,text=True,encoding='utf-8',errors='ignore')
    except subprocess.CalledProcessError:
        return []

    interfaces = []
    seen = set()
    for line in output.split('\n'):
        if ':' in line and not line.startswith(' '):
            interface = line.split(':', 1)[0].strip()
            if interface and interface not in seen:
                seen.add(interface)
                interfaces.append(interface)
    return interfaces