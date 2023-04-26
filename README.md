<h1 align="center">shomap</h1>

<p align="center">
  <img width="670" height="500" src="https://i.hizliresim.com/o73aqmy.jpg">
</p>


### Description :

***This tool is coded to provide some convenience in external penetration testing. When you enter the IP address, it performs passive scanning on Shodan.io and detects open ports. Then it learns the services running on the server and their versions by performing nmap scanning on open ports. Then, using this information, it tries to find possible exploit codes on Exploit-DB.***


#### Installation
```
git clone https://github.com/furkan-enes-polatoglu/shomap.git
cd shomap
pip3 install -r requirements.txt
```

#### Usage

```
usage: python3 shomap.py [IP]
```
### Features:

 - Multi platform (Supports most linux)
 - Easy to use
 - Possible error diagnoser
 - 77 Website templates
 
 ### Requirements
<ul>
  <li>shodan==0.7.1 </li>
  <li>nmap==0.6.1 </li>
  <li>requests==2.26.0 </li>
  <li>beautifulsoup4==4.9.3 </li>
  <li>pyfiglet==0.8.post1 </li>
  <li>termcolor==1.1.0 </li>
</ul>

