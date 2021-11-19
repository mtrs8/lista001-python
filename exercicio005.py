# 5) Verificar IP Address valido

def verifica_ip(ip):
    is_valid = False
    partes = ip.split(".")
    for i in range(len(partes)):
        if(checa_string(partes[i])):
            is_valid = True
            
    return is_valid

def checa_string(a):
    try: return str(int(a)) == a and 0 <= int(a) <= 255
    except: return False


ip_address = input('Digite um IP: ')
if(verifica_ip(ip_address)):
    print('IP válido')
else:
    print('IP não é válido')
