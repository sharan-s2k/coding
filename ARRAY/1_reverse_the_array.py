ip = input("Enter space seperated elements for an array : ")
try:
    ip = list(map(int,ip.split(' ')))
except:
    ip = ip.split(' ')
    if len(ip) == 1:
        ip = list(ip[0])
print(f"Original array -> {ip}")
lenn = len(ip)
for i in range(int(lenn/2)):
    ip[i] , ip[lenn-i-1] = ip[lenn-i-1] , ip[i]
print(f"Reversed array -> {ip}")