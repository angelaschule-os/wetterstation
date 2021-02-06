package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/http/httputil"
	"os"
	"runtime"
	"strings"
	"time"

	"github.com/joho/godotenv"
	"go.bug.st/serial"
)

// Sensor IDs
const (
	WIND_VELOCITY  = "601e947fe443a0001b961372"
	WIND_DIRECTION = "601e947fe443a0001b961373"
	TEMPERATURE    = "601e947fe443a0001b961374"
	REL_HUMIDITY   = "601e947fe443a0001b961375"
	AIR_PRESSURE   = "601e947fe443a0001b961376"
	RADIATION      = "601e947fe443a0001b961377"
	PRECIPITATION  = "601e947fe443a0001b961378"
)

var senseBoxID string
var authorization string

func init() {
	var envFile string
	envFile = ".env"

	err := godotenv.Load(envFile)

	if err != nil {
		log.Fatal("Error loading .env file")
	}

	runtime.GOMAXPROCS(2)

	senseBoxID = os.Getenv("SENSEBOXID")
	authorization = os.Getenv("AUTHORIZATION")

}

func backgroundTask(mode *serial.Mode, opensensemapAPI string) {
	// this creates a new ticker which will
	// `tick` every 10 second.
	ticker := time.NewTicker(60 * time.Second)

	// for every `tick` that our `ticker`
	// emits, we ...
	for _ = range ticker.C {

		port, err := serial.Open("/dev/ttyUSB0", mode)

		if err != nil {
			log.Fatal(err)
		}

		reader := bufio.NewReader(port)
		text, _ := reader.ReadString('\n')

		log.Println("Bytes:", len(text))

		if len(text) >= 100 {

			text = strings.TrimSuffix(text, "\n")
			log.Println(text)

			senseArray := strings.Fields(text)

			log.Println("Temperature", senseArray[3])

			values := map[string]string{"601e947fe443a0001b961372": senseArray[1], "601e947fe443a0001b961373": senseArray[2], "601e947fe443a0001b961374": senseArray[3], "601e947fe443a0001b961375": senseArray[4], "601e947fe443a0001b961376": senseArray[5], "601e947fe443a0001b961377": senseArray[6], "601e947fe443a0001b961378": senseArray[7]}
			jsonValue, _ := json.Marshal(values)

			//var jsonStr = []byte(`{"601e947fe443a0001b961374":` + senseArray[3] + `}`)

			// https://medium.com/@nate510/don-t-use-go-s-default-http-client-4804cb19f779
			timeout := time.Duration(60 * time.Second)
			client := http.Client{
				Timeout: timeout,
			}

			request, err := http.NewRequest("POST", opensensemapAPI, bytes.NewBuffer(jsonValue))
			request.Header.Set("User-Agent", "Angela-Client")
			request.Header.Set("Authorization", authorization)
			request.Header.Set("Content-Type", "application/json")

			if err != nil {
				log.Fatalln(err)
			}

			dump, err := httputil.DumpRequestOut(request, true)

			if err != nil {
				log.Fatalln(err)
			}

			log.Printf("%q\n", dump)

			resp, err := client.Do(request)

			if err != nil {
				log.Fatalln(err)
			}

			defer resp.Body.Close()

			body, err := ioutil.ReadAll(resp.Body)

			if err != nil {
				log.Fatalln(err)
			}

			log.Println(string(body))

		}
		port.Close()
	}
}

func main() {
	mode := &serial.Mode{
		BaudRate: 9600,
		Parity:   serial.OddParity,
		DataBits: 7,
		StopBits: serial.OneStopBit,
	}

	//current limit is 15 requests in one minute.
	opensensemapAPI := "https://api.opensensemap.org/boxes/" + senseBoxID + "/data"
	fmt.Println("URL:>", opensensemapAPI)

	go backgroundTask(mode, opensensemapAPI)

	// This print statement will be executed before
	// the first `tock` prints in the console
	fmt.Println("The rest of the application can continue")
	// here we use an empty select{} in order to keep
	// our main function alive indefinitely as it would
	// complete before our backgroundTask has a chance
	// to execute if we didn't.
	select {}

}
