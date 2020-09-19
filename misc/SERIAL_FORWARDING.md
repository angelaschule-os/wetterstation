# Serial forwarding


On the raspberry pi:

```shell
ssh pi@raspberry socat /dev/ttyUSB0 tcp4-listen:23366
```


On the other pc:

```shell
socat  pty,link=tty0,raw  tcp:raspberry:23366
```
