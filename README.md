# honeytrap
![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=FFE873)
![HTML](https://img.shields.io/badge/HTML5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
## Description and aim of the project
This is going to be another little project to keep training myself with what I know and to learn something new in the cybersecurity field.
It aims to develop a honeypot, a fake vulnerable SSH server via the paramiko library in Python (https://docs.paramiko.org/en/stable/index.html). When a malevolent user tries to access the server via different passwords, the honeypot blocks them and register their IP addresses, usernames and passwords. These will be stored in a SQLite DB. 
Finally, I'll add a simple UI using Flask.

## Roadmap
- [x] Build a Python script
- [x] Managing the SQLite DB
- [x] Developing the UI via Flask
