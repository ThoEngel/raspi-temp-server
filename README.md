# raspi-temp-server
raspi-temp-server

# Downloads:
Betriebssystem vom Raspi:
[Raspbian Stretch Lite](https://www.raspberrypi.org/downloads/raspbian/).

# Image auf SD Karte flashen:
- mittels [SD Formatter](https://www.chip.de/downloads/SD-Formatter_72605634.html) die SD-Karte formatieren
- mittels [balenaEtcher](https://www.balena.io/etcher/) die SD Karte mit dem Raspi-Image flashen
- eine leere Datei ssh ins Hauptverzeichnis der SD Karte erstellen
- eine Datei wpa_supplicant.conf ind Hauptverzeichnis der SD Karte erstellen (beinhalt die WLAN Konfigration)

wpa_supplicant.conf: 
```
country=DE  #omit if US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
       ssid="Name WLAN1"
       psk="password"
       key_mgmt=WPA-PSK
       id_str="location1"
       priority=1
}
network={
     ssid="Name WLAN2"
       psk="password"
       key_mgmt=WPA-PSK
       id_str="location2"
       priority=2
}
```

# Erste Start
SD Karte in Raspi reinstecken und einschalten.
Im WLAN Router nach der Raspi suchen und die IP Adresse (ip-adresse) ermitteln sowie dem dem Raspi immer die gleiche IPv4-Adresse zuweisen.

Windows Kommandozeile mit "cmd" öffnen.

Mit Raspi verbinden: ssh pi@ip-adresse

Raspi User: pi
Raspi Passwort: raspberry


