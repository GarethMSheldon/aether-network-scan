import socket
import json
import os
import concurrent.futures
from datetime import datetime

# Configuration from Environment
TARGET = os.getenv("SCAN_TARGET", "127.0.0.1")
PORT_RANGE = os.getenv("SCAN_PORTS", "1-1024")
TIMEOUT = float(os.getenv("SCAN_TIMEOUT", "0.5"))
THREADS = int(os.getenv("MAX_THREADS", "50"))

def get_banner(s):
    """Attempt to grab the service banner."""
    try:
        return s.recv(1024).decode().strip()
    except:
        return "No banner available"

def scan_port(port):
    """Scans a single port and returns data if open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            result = s.connect_ex((TARGET, port))
            if result == 0:
                banner = get_banner(s)
                print(f"[+] FOUND: Port {port} is OPEN")
                return {
                    "port": port,
                    "status": "open",
                    "banner": banner,
                    "timestamp": datetime.now().isoformat()
                }
    except Exception:
        pass
    return None

def main():
    print(f"--- AETHER-SCAN: Mapping {TARGET} ---")
    start_p, end_p = map(int, PORT_RANGE.split('-'))
    ports = range(start_p, end_p + 1)
    
    results = []
    
    # Use threading for high-speed scanning
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        found_ports = list(executor.map(scan_port, ports))
        results = [p for p in found_ports if p is not None]

    # Save to JSON
    output = {
        "target": TARGET,
        "total_open": len(results),
        "results": results
    }
    
    filename = f"/app/logs/aether_{TARGET}_{datetime.now().strftime('%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(output, f, indent=4)
    
    print(f"--- Scan Finished. {len(results)} ports found. Saved to {filename} ---")

if __name__ == "__main__":
    main()
