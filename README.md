# Workshop with FactoryBoy

## How to start
1. Clone repo and create virtual env.
2. ```pip install -r requirements.txt```
3. Create environment variable TEST_DB_URL with the url you want to use for this workhop. You don't have to create the database.


## Links
- [FactoryBoy documentation](https://factoryboy.readthedocs.io/en/stable/introduction.html)
- [Faker providers](https://faker.readthedocs.io/en/master/providers.html)


## Troubleshooting
Problems I got on my WSL and what helped:
* error while installing psycopg2 

```sudo apt-get install libpq-dev```

```sudo apt install python3-dev```

* proxy error on wsl (ubuntu 18.04)

1. export env variables http_proxy and https_proxy
2. proxy.conf
> Created a proxy.conf file in /etc/apt/apt.conf.d/
> 
>Inside this file put: Acquire::http::Proxy "http://myproxy:myproxyport";

source -> https://github.com/microsoft/WSL/issues/1570
