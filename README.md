# honeytrap
![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=FFE873)

## Description and aim of the project
This is going to be another little project to keep training myself with what I know and to learn something new in the cybersecurity field.
It aims to develop a honeypot, a fake vulnerable SSH server via the paramiko library in Python (https://docs.paramiko.org/en/stable/index.html). When a malevolent user tries to access the server via different passwords, the honeypot blocks them and register their IP addresses, usernames and passwords. These will be stored in a SQLite DB. 
Finally, I'll add a simple UI using Flask.

## Roadmap
- [ ] Build a Python script
- [ ] Managing the SQLite DB
- [ ] Developing the UI via Flask
