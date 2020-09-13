# wetterstation

Seit Dezember 2006 werden Außenlufttemperatur und Luftfeuchte,
Globalstrahlung, Regen und Luftdruck von der Wetterstation der Schule
aufgezeichnet.

- [wetterstation](#wetterstation)
  - [openSenseMap](#opensensemap)
  - [Messsystem](#messsystem)
    - [Sensoren](#sensoren)
  - [Test](#test)
  - [Links](#links)

## openSenseMap

Die Daten der Wetterstation können zukünftig auf
[openSenseMap](https://opensensemap.org/) gefunden werden:

<https://opensensemap.org/explore/5f5dc63f84e5a2001b1d5dbc>

## Messsystem

```
Thies CLIMA
DATALOGGER
MeteoLOG TDL 14
Order-No.:9.1740.1X.01X
Software-Version: 3.12
```

### Sensoren

| Sensoren            | Einheit | Produktname         |
| ------------------- | --------| ------------------- |
| Außenlufttemperatur | °C      |                     |
| Außenluftfeuchte    | %       |                     |
| Globalstrahlung     | W/m²    |                     |
| Luftdruck           | hPa     | Barogeber PTB 100 A |
| Regen               | mm/m²   |                     |

[Documentation](docs/9.1740.xx.xxx_TDL14_V3.12_eng.pdf)

## Test

```shell
screen /dev/ttyUSB0
```

```shell
cat /dev/ttyUSB0
```

## Links

- https://opensensemap.org/
- https://www.heise.de/make/artikel/Wettermessgeraet-fuer-OpenSenseMap-einrichten-2803135.html
