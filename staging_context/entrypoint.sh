# !/bin/bash

set -e

# check env variables
if [ -z "$SITE_NAME" ]; then
    echo "Provide SITE_NAME as env variable"
    exit 1
fi

if [ -z "$SITE_ADMIN_PASSWORD" ]; then
    echo "Provide SITE_ADMIN_PASSWORD as env variable"
    exit 1
fi

# Setup and start mariadb database
sudo service mariadb start
# Wait for mariadb to start
while ! sudo mysqladmin -u root ping --silent > /dev/null 2>&1; do
    echo "waiting for mariadb to start"
    sleep 1
done
until sudo mariadb -e "SET PASSWORD FOR root@localhost = PASSWORD('root');FLUSH PRIVILEGES;"  > /dev/null 2>&1; do
    echo "trying to set mariadb root password"
    sleep 1
done


# Prepare Site
bench new-site --db-host 127.0.0.1 --db-port 3306 --db-root-username root --db-root-password root --admin-password $SITE_ADMIN_PASSWORD $SITE_NAME
bench use $SITE_NAME
bench set-config -g server_script_enabled 1
bench --site all enable-scheduler

# Install apps
while IFS= read -r app; do
    if [[ "$app" != "frappe" ]]; then
        bench install-app $app
    fi
done < /home/frappe/frappe-bench/sites/apps.txt

exec supervisord