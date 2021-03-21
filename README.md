# Python Time Lapse
Basically, this program connects to a GoPro from a Unix based OS and take a picture every N seconds. Then, it'll send it encoded in b64 to a remote server.

## Setup

 First of all, install the packages (I recommend you make a virtual env before)
 ```bash
 pip3 install -r requirements.txt
 ```

 Then fill out the required environment variables in `dotenv` and rename it to `.env`

 At this point I believe you are ready to run the app.
 ```bash
 python3 main.py
 ```
## Requirements
> developed in Python 3

Required modules:
* [goprocam module by KonradIT](https://github.com/KonradIT/gopro-py-api)
* Wireless module
* Twilio
* python-dotenv


## Notes
>🐻 with me please, I made this when I was 15yo and was learning python in 1 week
* Temporary I'm using `time.sleep()` instead of a coroutine (idk much about that) or a asynchronous function to connect to Wi-Fi and related tasks.

