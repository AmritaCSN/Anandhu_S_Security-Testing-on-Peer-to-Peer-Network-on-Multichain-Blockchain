#!/bin/bash

sudo ufw enable
sleep 4
sudo ufw deny 8571
sleep 4
sudo ufw deny out 8571
sleep 4
sudo ufw deny 8571/tcp
sleep 4
sudo ufw deny 8571/udp
sleep 4
sudo ufw status
