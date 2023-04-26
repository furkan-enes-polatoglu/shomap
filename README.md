<h1 align="center">shomap</h1> <br>

<p align="center">
  <img src="https://img.shields.io/badge/Author-bulletproof-red">&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Open%20Source-Yes-cyan?style=flat-square">&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Made%20in-Turkey-blue">&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>


<p align="center">
  <img width="730" height="500" src="https://i.hizliresim.com/o73aqmy.jpg">
</p>


### Description :

***This tool is coded to provide some convenience in external penetration testing. When you enter the IP address, it performs passive scanning on Shodan.io and detects open ports. Then it learns the services running on the server and their versions by performing nmap scanning on open ports. Then, using this information, it tries to find possible exploit codes on Exploit-DB. Sometimes it may not find the correct exploit codes. So a false positive situation is possible. We will continue to make improvements.***

<br>

### Installation
```
git clone https://github.com/furkan-enes-polatoglu/shomap.git
cd shomap
pip3 install -r requirements.txt
```

### Usage

```
usage: python3 shomap.py [IP]
```
<br>

### Features:

 - Multi platform (Supports most linux)
 - Easy to use
 - Possible error diagnoser
 - 77 Website templates

<br>

 ### Requirements
<ul>
  <li>shodan==0.7.1 </li>
  <li>nmap==0.6.1 </li>
  <li>requests==2.26.0 </li>
  <li>beautifulsoup4==4.9.3 </li>
  <li>pyfiglet==0.8.post1 </li>
  <li>termcolor==1.1.0 </li>
</ul>

