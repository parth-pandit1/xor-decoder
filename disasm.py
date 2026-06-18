import pefile
import math
import re

def extract_strings(filepath, min_len=4):
    with open(filepath, 'rb') as f:
        data = f.read()
    pattern = rb'[\x20-\x7E]{' + str(min_len).encode() + rb',}'
    strings = re.findall(pattern, data)
    return [s.decode() for s in strings]

filepath = 'C:\\Windows\\System32\\notepad.exe'
strings = extract_strings(filepath)

print("=== INTERESTING FINDINGS ===\n")

# URLs dhundo
print("--- URLs ---")
for s in strings:
    if 'http' in s.lower() or 'www.' in s.lower():
        print(f"  {s}")

# IP addresses dhundo
print("\n--- IP ADDRESSES ---")
ip_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
for s in strings:
    if ip_pattern.search(s):
        print(f"  {s}")

# .exe files dhundo
print("\n--- EXE REFERENCES ---")
for s in strings:
    if '.exe' in s.lower() or '.dll' in s.lower():
        if len(s) < 50:
            print(f"  {s}")

print(f"\nTotal strings: {len(strings)}")