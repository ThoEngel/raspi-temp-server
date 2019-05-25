# raspi-temp-server
raspi-temp-server


# Image auf SD Karte flashen:
- [Raspbian Stretch Lite](https://www.raspberrypi.org/downloads/raspbian/) Image herunterladen und entpacken
- mittels [SD Formatter](https://www.chip.de/downloads/SD-Formatter_72605634.html) die SD-Karte formatieren
- mittels [balenaEtcher](https://www.balena.io/etcher/) das Image auf SD Karte flashen
- eine leere Datei ssh ins Hauptverzeichnis der SD Karte erstellen (ermögliche ssh Zugriff auf Raspi)
- eine Datei wpa_supplicant.conf ins Hauptverzeichnis der SD Karte erstellen (beinhalt die WLAN Konfigration)

wpa_supplicant.conf: (WLAN Namen und WLAN Passwort ergänzen)
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
Im WLAN Router nach dem Raspi suchen und die IP Adresse (ip-adresse) ermitteln sowie dem dem Raspi immer die gleiche IPv4-Adresse zuweisen.

Windows Kommandozeile mit "cmd" öffnen.

Mit Raspi verbinden: ssh pi@ip-adresse

Raspi User: pi

Raspi Passwort: raspberry

# Raspi aktualisieren / Software installieren
Raspi Update: 
```
sudo apt-get update
sudo apt-get dist-upgrade
```
Software (GIT) installieren:
```
sudo apt install git
```

# Installation des Sensors: DS18B20
Zuerst lasse ich mir die vom System geladenen Module anzeigen.
```
sudo lsmod
```
Die notwendigen Module: wire und w1-gpio sind nicht vorhanden


Als nächstes erweitern wir die notwendigen Dateien für die automatische Aktivierung des Buses und des Sensors nach einem Neustart.
Die Datei config.txt ist für das Laden der Module zuständig. Diese rufst du mit dem Befehl
```
sudo nano /boot/config.txt
```
Und weiterst die Datei um die folgenden Zeilen:
```
# Temperatursensor an 1-Wire
dtoverlay=w1-gpio
gpiopin=4
```

Danach führst du einen Neustart des Raspberry Pi aus.
```
sudo reboot
```
Nach dem Neustart kannst du mit dem Befehl
```
sudo lsmod
```
die korrekte Aktivierung des 1-Wire Bus überprüfen.
Die notwendigen Module: wire und w1-gpio solten jetzt vorhanden sein.

Das System schreibt immer den aktuellen Wert des Sensors in eine Datei. Diese befindet sich in einem durch die Sensor-Kennung bestimmten Verzeichnis. Dieses findest du, indem du mit
```
cd /sys/bus/w1/devices
```
in das Busverzeichnis wechselst und den Befehl zur Anzeigen des Inhaltsverzeichnisses ausführst.
```
ls
```
Bei einem Sensor werden dir nun zwei Verzeichnisse angezeigt. Ein Verzeichnis ist “w1_bus_master1”, das für uns wichtige Verzeichnis ist das mit einer Code-Bezeichnung, in meinem Fall “28-000005d2e508”.

Mit dem folgenden Befehl kannst du dir nun den Inhalt der Datei “w1_slave” mit dem Sensor-Wert bzw. der Temperatur anzeigen lassen.
```
cat /sys/bus/w1/devices/28-000005d2e508/w1_slave
```
