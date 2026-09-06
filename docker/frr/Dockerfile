FROM frrouting/frr:latest

RUN apk add --no-cache openssh

RUN ssh-keygen -A

RUN echo 'root:netlab123' | chpasswd

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/bin/sh", "-c", "/usr/sbin/sshd && /usr/lib/frr/docker-start"]