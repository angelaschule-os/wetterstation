# wetterstation

Seit Dezember 2006 werden Außenlufttemperatur und Luftfeuchte, Globalstrahlung, Regen und Luftdruck von der Wetterstation der Schule aufgezeichnet.

## DATALOGGER

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
