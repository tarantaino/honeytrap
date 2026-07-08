## HoneyTrap

![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=FFE873)
![HTML](https://img.shields.io/badge/HTML5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Description and aim of the project
This is another personal project built to train my skills and learn new concepts in the DevSecOps and Cybsersecurity fields.
It aims to develop a Honeypot, a fake vulnerable SSH server built  via the `paramiko` library in Python (https://docs.paramiko.org/en/stable/index.html). 
When a malevolent user, or a bot, tries to access the server by guessing the passwords (Brute Force Attack), the honeypot blocks the intrusion but secretly and register the attacker's IP address, username and password used during the attempt. 

The collected data is safely stored in a local SQLite DB and displayed in real-time on a web UI dashboard powered by Flask. 

## Key Features

- Custom SSH Server: fully intercepts login attempts on a custom port without exposing the real OS

- Microservices Architecture: separeted backend logic (Honeypot) and frontend visualization (Web Dashboard)

- Security first: built-in protection agaisnt SQL Injection (via parameterized queries) and Stored XSS attacks (via secure DOM manipulation in vanilla JS)

- Dockerizerd Environment: the whole infrastructure can be easily spun up in isolated containers using Docker Compose

## How to Run
You can run this project in two ways: Docker (Recommended) or locally on your machine.

**Docker (Recommended)**
This is the easies way to run the project in a safe, isolated environment.
1. Make sure you have Docker and Docker Desktop installed.
2. Clone this repository and navigate to the project folder.
3. Run the following command in your terminal:
```bash
docker compose up --build
```
4. The HoneyPot is now listening on port `2222` and the web dashboard is available at `http://localhost:5000`.

**Running Locally**
If you prefer to run the scripts directly on your OS:
1. Ensure you have Python 3.x installed.
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Open a terminal and start the HoneyPot engine:
```bash
python core/honeypot.py
```
4. Open a second terminal and start the Flask web server:
```bash
python web/app.py
```

5. Access the dashboard at `http://localhost:5000`.

##How to Test it
To simulate an attack and see the HoneyPot in action, open a new terminal and try to connect to it via SSH:
```bash
ssh root@127.0.0.1 -p 2222
```

Type any random passowrd when prompted. The connection will be dropped (Permission denied), but if you check the Web Dashboard, you will see your attack logged in real-time.

## Troubleshooting
"WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!"

When testing the Honeypot multiple times, or if you rebuild the project, your local SSH client might throw a Man-in-The-Middle (MiTM) warning. This happens beacause the Honeypot generates a new RSA key or your client remembers an old one.

To fix this and reset the known key for the local testing IP, simply run this command in your terminal:
```bash
ssh-keygen -R [127.0.0.1]:2222
```
After running this, try the SSH connection again and accept the new fingerprint. *(Note: the project now saves the `server_rsa.key` persistently to prevent this issue across standards reboots).

## Roadmap
- [x] Build a Python script
- [x] Managing the SQLite DB
- [x] Developing the UI via Flask
- [ ] Maybe add a GeoIP API to track the country of origin of the attackers
- [ ] Maybe implement a fake interactive shell to capture malicious command post-login

## DISCLAIMER
This project is and was created for educational and research purposes ONLY. Do not deploy this in a production environment without proper security hardening and isolation.
The author is not responsbile for any misuse or damage caused by this software. 