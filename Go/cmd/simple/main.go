package main

import (
	"bufio"
	"fmt"
	"log"

	"github.com/jacobsa/go-serial/serial"
)

func main() {
	options := serial.OpenOptions{
		PortName:          "/dev/ttyUSB0",
		BaudRate:          9600,
		DataBits:          7,
		StopBits:          1,
		MinimumReadSize:   4,
		RTSCTSFlowControl: false,
		ParityMode:        serial.PARITY_ODD,
	}
	serialPort, err := serial.Open(options)
	if err != nil {
		log.Fatalf("serial.Open: %v", err)
	}
	defer serialPort.Close()
	reader := bufio.NewReader(serialPort)
	scanner := bufio.NewScanner(reader)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}
