#!/bin/sh
# Clean up existing environment
docker-compose down --remove-orphans
# Pull built images
docker-compose pull
# Build the static files into a docker image to host it via nginx
docker-compose build nginx
# Run docker compose
docker-compose -f /root/docker-compose.yml up -d
