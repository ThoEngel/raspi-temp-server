# raspi-temp-server
raspi-temp-server

# Downloads:

Betriebssystem vom Raspi:
[Raspbian Stretch Lite](https://www.raspberrypi.org/downloads/raspbian/).


# Image auf SD Karte flashen:
- mittels SDFormatter die SD-Karte formatieren
- mittels balenaEtcher die SD Karte mit dem Image flashen
- eine leere Datei ssh ins Hauptverzeichnis der SD Karte erstellen
- eine Datei wpa_supplicant.conf ind Hauptverzeichnis der SD Karte erstellen (beinhalt die WLAN Konfigration)

wpa_supplicant.conf: 
```
country=DE  #omit if US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
       ssid=""
       psk=""
       key_mgmt=WPA-PSK
       id_str="Musberg"
       priority=1
}
network={
     ssid=""
       psk=""
       key_mgmt=WPA-PSK
       id_str="Woelfershausen"
       priority=2
}
```


The default user is pi, and the password is raspberry
