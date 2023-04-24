import shodan
import nmap
import sys
import requests
from bs4 import BeautifulSoup
import pyfiglet
from termcolor import colored

result = pyfiglet.figlet_format("shomap", font = "slant"  )
colored_banner = colored(result, color='blue')
print(colored_banner)

author = "                          by bulletproof\n                Twitter: @nevrotikharman"
colored_author = colored(author, color='red')
print(colored_author)

info = "[*]"
colored_info = colored(info, color='blue')

err = "[-]"
colored_err = colored(err, color='red')

success = "[+]"
colored_success = colored(success, color='yellow')

# Shodan API anahtarınızı buraya girin
SHODAN_API_KEY = "a9tXOqFppFe5aOSkzOstr0E7yDXE32Fp"

# IP adresi
ip = sys.argv[1]

print("\n\n"+colored_info + ' IP: {}'.format(ip))

# Shodan nesnesini oluşturun
api = shodan.Shodan(SHODAN_API_KEY)

# Shodan'a sorgu gönderin
try:
    results = api.host(ip)

    # Açık portları yazdırın
    for port in results['ports']:
        print("---------------------------------------------------------")
        print(colored_info + ' Port: {}'.format(port))
        
        # Nmap taraması yapın
        nm = nmap.PortScanner()
        nm.scan(ip, str(port))
        print(colored_info + " Port is " +  nm[ip]['tcp'][port]['state'])
        product = nm[ip]['tcp'][port]['product']
        version = nm[ip]['tcp'][port]['version']
        if(product):
            print(colored_info + ' Product: {}'.format(product))
        else:
            print(colored_err + ' Product: Not found')
        print(colored_info + ' Version: {}'.format(version))

        # Google araması yapın
        query = '{} {} exploit-db'.format(product, version)
        url = 'https://www.google.com/search?q={}'.format(query)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        # Exploit-DB URL'sini alın
        exploit_db_url = None
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and 'exploit-db.com/exploits' in href:
                exploit_db_url = href
                break

        # Sonuçları yazdırın
        if exploit_db_url:
            print(colored_success + ' Exploit-DB URL: {}'.format(exploit_db_url))
        else:
            print('Exploit-DB URL bulunamadı.')

except shodan.APIError as e:
    print('Hata: {}'.format(e))
