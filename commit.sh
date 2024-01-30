#!/usr/bin/bash

read -p 'message: ' message 

echo $message
git add .
git commit -m $message
git push origin main
