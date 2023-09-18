ip = input("Enter space seperated elements for an array : ")
try:
    ip = list(map(int,ip.split(' ')))
except:
    ip = ip.split(' ')
    if len(ip) == 1:
        ip = list(ip[0])
print(f"Original array -> {ip}")
rev = ip.copy()
lenn = len(ip)
for i in range(int(lenn/2)):
    temp = rev[i]
    rev[i] = ip[lenn-i-1]
    rev[lenn-i-1] = temp
print(f"Reversed array -> {rev}")