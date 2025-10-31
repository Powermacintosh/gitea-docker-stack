## Конфигурация NGINX

### Gitea на корневом пути

```nginx
server {
    listen 80;
    server_name gitea.me www.gitea.me;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name gitea.me www.gitea.me;

    ssl_certificate /etc/letsencrypt/live/gitea.me/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/gitea.me/privkey.pem;

    client_max_body_size 3G;

    location / {
        proxy_pass http://0.0.0.0:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

    }
}
```

### Docker nginx-internal (SWARM)

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://gitea_gitea:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Grafana на поддомене

```nginx
server {
    listen 80;
    server_name grafana.gitea.me;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name grafana.gitea.me;

    ssl_certificate /etc/letsencrypt/live/grafana.gitea.me/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/grafana.gitea.me/privkey.pem;

    location / {
        proxy_pass http://localhost:3010;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

    }
}
```
