FROM fc_base_image

USER root

# Install mariadb
RUN apt-key adv --fetch-keys 'https://mariadb.org/mariadb_release_signing_key.asc' && \
    add-apt-repository 'deb [arch=amd64] https://mariadb.mirror.liquidtelecom.com/repo/10.6/ubuntu focal main' && \
    apt update -y && apt install -y mariadb-server mariadb-client sudo  --fix-broken --fix-missing && \
    rm -rf /var/lib/apt/lists/*

# Add frappe to sudoers
RUN echo 'frappe ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
COPY ./mariadb.cnf /etc/mysql/mariadb.cnf

USER frappe

COPY ./entrypoint.sh /home/frappe/entrypoint.sh

ENTRYPOINT [ "bash" ]
CMD ["/home/frappe/entrypoint.sh"]
