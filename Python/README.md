# Streaming sensor data via websockets

Streaming sensor data with <http://websocketd.com/>.

More infos about websockets <https://de.wikipedia.org/wiki/WebSocket>.

## Download websocketd

```shell
curl -OL https://github.com/joewalnes/websocketd/releases/download/v0.3.0/websocketd-0.3.0-linux_amd64.zip
```

## Unzip only binary

```shell
unzip -d . websocketd-0.3.0-linux_amd64.zip websocketd
```

## Start service

Start `websocketd` and tell it about your program:

```shell
./websocketd --port=8080 ./thies.py 
```