# Workshop with FactoryBoy

## How to start
0. Clone repo and create virtual env.
1. ```pip install -r requirements.txt```
2. Create environment variable TEST_DB_URL with the url you want to use for this workhop.
3. Create database:
    * Manually on your local server and restore with backup from _data_ folder
    
    OR
    * Run script _setup.py_. The database from url doesn't have to exist yet. (You will need psycopg2 library for that.)


## Links
- [FactoryBoy documentation](https://factoryboy.readthedocs.io/en/stable/introduction.html)
- [Faker providers](https://faker.readthedocs.io/en/master/providers.html)


## Troubleshooting
Problems I got on my WSL and what helped:
* error while installing psycopg2 

```sudo apt-get install libpq-dev```

```sudo apt install python3-dev```

* proxy error on wsl (ubuntu 18.04)

```export http_proxy=http://gateway.schneider.zscaler.net:9480```

```export https_proxy=https://gateway.schneider.zscaler.net:9480```
> Created a proxy.conf file in /etc/apt/apt.conf.d/
> 
>Inside this file put: Acquire::http::Proxy "http://myproxy:myproxyport";

source -> https://github.com/microsoft/WSL/issues/1570
