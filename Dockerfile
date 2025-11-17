# Multi-stage build for Hugo site + Panel dashboard
FROM python:3.12-slim as dashboard

WORKDIR /app/dashboard
COPY dashboard/ .
RUN pip install --no-cache-dir -r requirements.txt

# Install Hugo
FROM klakegg/hugo:0.152.2-ext as hugo-build
WORKDIR /site
COPY . .
RUN hugo --minify

# Final image with both
FROM python:3.12-slim

# Install nginx
RUN apt-get update && apt-get install -y nginx supervisor && rm -rf /var/lib/apt/lists/*

# Copy dashboard
WORKDIR /app/dashboard
COPY --from=dashboard /app/dashboard .
COPY --from=dashboard /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# Copy Hugo site
COPY --from=hugo-build /site/public /var/www/html

# Nginx config
COPY <<EOF /etc/nginx/sites-available/default
server {
    listen 80;
    server_name _;
    
    # Hugo static site
    location / {
        root /var/www/html;
        try_files \$uri \$uri/ =404;
    }
    
    # Panel dashboard proxy
    location /dashboard-app/ {
        proxy_pass http://localhost:8050/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

# Supervisor config
COPY <<EOF /etc/supervisor/conf.d/supervisord.conf
[supervisord]
nodaemon=true

[program:nginx]
command=/usr/sbin/nginx -g "daemon off;"
autostart=true
autorestart=true

[program:panel]
command=python /app/dashboard/app.py
directory=/app/dashboard
autostart=true
autorestart=true
EOF

EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
