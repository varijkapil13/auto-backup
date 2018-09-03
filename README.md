# VK AutoBackups
A simple library to make auto backups of PostgreSQL database instances.

## Installation
There are two ways to install this library:
- Docker
- Directly from sources

### Installation using Docker

1. Clone this repository using `git clone https://github.com/varijkapil13/auto-backup.git`
2. Add your database configuration to `server.ini` file.
    ```
    [localhost]
    url = localhost
    port = 5432
    username = postgres
    password = password
    database = testdb
    ```
    Using this configuration the script will create a folder named `localhost` (taken from the block `[localhost]`) and save the backups in that directory with time stamps
    
    More than one database servers can be added to the file. Below is an example configuration for such a setting:
     
     ```
    [localhost]
    url = localhost
    port = 5432
    username = postgres
    password = password
    database = testdb
    
    [My other server]
    url = otherserver.com
    port = 5432
    username = postgres
    password = password
    database = testdb
    ```
    Using this configuration the script will create two folders named `localhost` and `My other server` and save the backups in these directories with time stamps.
    
3. Create docker container using `docker build -t vk-auto-backup:latest . && docker run -v /Users/varijkapil13/backups:/app/Backups/ --name vk-auto-backup vk-auto-backup:latest`
    
    Replace `/Users/varijkapil13/backups` with path to the folder where you want to store your backups.

4. The application is now in a docker container and will automatically backup your databases everyday at 00:00 Hours.
### Installation from sources

1. Clone this repository using `git clone https://github.com/varijkapil13/auto-backup.git`

2. Install virtualenv.

    `pip install virtualenv`
3. Create a virtual environment and activate it.
    
    `virtualenv venv`
    
    `source venv/bin/activate`
4. Add your database configuration to `server.ini` file.
    ```
    [localhost]
    url = localhost
    port = 5432
    username = postgres
    password = password
    database = testdb
    ```
    Using this configuration the script will create a folder named `localhost` (taken from the block `[localhost]`) and save the backups in that directory with time stamps
    
    More than one database servers can be added to the file. Below is an example configuration for such a setting:
     
     ```
    [localhost]
    url = localhost
    port = 5432
    username = postgres
    password = password
    database = testdb
    
    [My other server]
    url = otherserver.com
    port = 5432
    username = postgres
    password = password
    database = testdb
    ```
    Using this configuration the script will create two folders named `localhost` and `My other server` and save the backups in these directories with time stamps.

5. Run the script using:

    `python3 backup.py`
    
    The script will backup your database at 00:00 Hours to folder `.../path/to/app/auto-backup/Backups/`. **It will only create the backup once. To make it run automoatically you will have to link the script with some external service link `supervisor.d` or in `init.d` in Ubuntu**
