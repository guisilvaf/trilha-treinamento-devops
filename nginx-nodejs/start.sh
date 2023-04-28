#!/bin/dash

node /app/index.js &

nginx -g "daemon off;"