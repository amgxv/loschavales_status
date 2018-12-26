# loschavales_status
Very simple app that returns information from your Minecraft Server, based on https://api.mcsrvstat.us

**Only tested on Vanilla server**

#### Returns : 
* Favicon 
* Server Name
* Server Version
* Current Users
* Max Users

### Usage

```
docker exec -it --rm -e SERVER=yourserver amgxv/loschavales_status
```

```
    minecraft-status:
      image: amgxv/loschavales_status
      labels:
        - "traefik.enable=true"
        - "traefik.frontend.rule=Host:server.domain"
        - "traefik.frontend.redirect.entryPoint=https"
        - "traefik.port=5000"
      environment:
        SERVER: "server"
      restart: always
      networks:
        - trafnet

```

