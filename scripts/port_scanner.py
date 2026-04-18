#!/usr/bin/env python3
"""
Port Scanner — Educational Demonstration
=========================================
Author: Akshaya | GRC Portfolio
Usage: python port_scanner.py --host 192.168.1.1 --start 1 --end 1024

⚠️  FOR AUTHORISED TESTING ONLY. Never scan systems you do not own
    or do not have explicit written permission to test.
"""

import socket
import sys
import argparse
import threading
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Common port service mapping
SERVICE_MAP = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 5900: "VNC", 6379: "Redis",
    8080: "HTTP-Alt", 8443: "HTTPS-Alt", 27017: "MongoDB",
}

WELL_KNOWN_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143,
    443, 445, 587, 993, 995, 1433, 1521, 3306, 3389,
    5432, 5900, 6379, 8080, 8443, 8888, 27017,
]

def scan_port(host: str, port: int, timeout: float = 0.8) -> dict:
    """Attempt TCP connection to host:port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            service = SERVICE_MAP.get(port, "Unknown")
            return {"port": port, "state": "OPEN", "service": service}
    except (socket.timeout, socket.error):
        pass
    return {"port": port, "state": "closed", "service": ""}

def grab_banner(host: str, port: int, timeout: float = 2.0) -> str:
    """Attempt to grab service banner."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        if port in [80, 8080, 8443]:
            sock.send(b"HEAD / HTTP/1.0\r\nHost: " + host.encode() + b"\r\n\r\n")
        banner = sock.recv(256).decode('utf-8', errors='ignore').strip()
        sock.close()
        return banner[:100]  # truncate
    except Exception:
        return ""

def resolve_host(host: str) -> str:
    """Resolve hostname to IP."""
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        print(f"[!] Cannot resolve: {host}")
        sys.exit(1)

def scan_range(host: str, start: int, end: int,
               threads: int = 100, grab_banners: bool = False) -> list:
    """Scan a port range using thread pool."""
    open_ports = []
    ports = list(range(start, end + 1))
    total = len(ports)
    scanned = 0

    print(f"\n{'='*55}")
    print(f"  PORT SCANNER — AUTHORISED USE ONLY")
    print(f"{'='*55}")
    print(f"  Target:   {host}")
    print(f"  Range:    {start}–{end} ({total} ports)")
    print(f"  Threads:  {threads}")
    print(f"  Started:  {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*55}\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, host, p): p for p in ports}
        for future in as_completed(futures):
            scanned += 1
            result = future.result()
            if result["state"] == "OPEN":
                if grab_banners:
                    result["banner"] = grab_banner(host, result["port"])
                open_ports.append(result)
                svc = result["service"]
                banner = f" | {result.get('banner','')[:50]}" if grab_banners else ""
                print(f"  [OPEN] {result['port']:>5}/tcp  {svc:<15}{banner}")
            if scanned % 500 == 0:
                pct = scanned / total * 100
                print(f"  ... {scanned}/{total} ports scanned ({pct:.0f}%)")

    return sorted(open_ports, key=lambda x: x["port"])

def print_summary(host: str, results: list, elapsed: float) -> None:
    """Print scan summary."""
    print(f"\n{'='*55}")
    print(f"  SCAN COMPLETE")
    print(f"{'='*55}")
    print(f"  Host:        {host}")
    print(f"  Open ports:  {len(results)}")
    print(f"  Duration:    {elapsed:.1f}s")

    if results:
        print(f"\n  OPEN PORTS SUMMARY:")
        print(f"  {'PORT':<8} {'SERVICE':<15} {'RISK NOTE'}")
        print(f"  {'-'*45}")
        high_risk = {23: "CRITICAL: Telnet unencrypted",
                     21: "HIGH: FTP unencrypted",
                     3389: "HIGH: RDP exposed",
                     5900: "HIGH: VNC exposed",
                     6379: "HIGH: Redis often unauthenticated",
                     27017: "HIGH: MongoDB often unauthenticated"}
        for r in results:
            risk = high_risk.get(r["port"], "")
            risk_str = f"⚠️  {risk}" if risk else ""
            print(f"  {r['port']:<8} {r['service']:<15} {risk_str}")
    print(f"{'='*55}")
    print(f"\n  ⚠️  Use this data only for authorised security assessments.")

def main():
    parser = argparse.ArgumentParser(
        description="Port Scanner — For authorised security testing only",
        epilog="Example: python port_scanner.py --host example.com --start 1 --end 1024"
    )
    parser.add_argument("--host", required=True, help="Target host or IP")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--threads", type=int, default=100, help="Thread count (default: 100)")
    parser.add_argument("--well-known", action="store_true",
                        help="Scan well-known ports only (faster)")
    parser.add_argument("--banners", action="store_true",
                        help="Attempt banner grabbing on open ports")
    parser.add_argument("--json", help="Save results to JSON file")
    args = parser.parse_args()

    # Validate range
    if not (1 <= args.start <= 65535) or not (1 <= args.end <= 65535):
        print("[!] Port range must be 1-65535")
        sys.exit(1)

    ip = resolve_host(args.host)
    if ip != args.host:
        print(f"  Resolved: {args.host} → {ip}")

    start_time = datetime.now()

    if args.well_known:
        print(f"  Mode: Well-known ports ({len(WELL_KNOWN_PORTS)} ports)")
        results = []
        for port in WELL_KNOWN_PORTS:
            r = scan_port(ip, port)
            if r["state"] == "OPEN":
                if args.banners:
                    r["banner"] = grab_banner(ip, port)
                results.append(r)
                print(f"  [OPEN] {port}/tcp  {r['service']}")
    else:
        results = scan_range(ip, args.start, args.end, args.threads, args.banners)

    elapsed = (datetime.now() - start_time).total_seconds()
    print_summary(ip, results, elapsed)

    if args.json and results:
        output = {
            "host": args.host, "ip": ip,
            "scan_time": start_time.isoformat(),
            "open_ports": results
        }
        with open(args.json, 'w') as f:
            json.dump(output, f, indent=2)
        print(f"\n  Results saved: {args.json}")

if __name__ == "__main__":
    main()
