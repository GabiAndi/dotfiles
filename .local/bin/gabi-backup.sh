#!/bin/sh

echo "Sincronizando Documentos"
rsync -av --delete-after $HOME/Documentos/ gabi-sv:/mnt/datos/Gabi/Backups/Documentos

echo "Sincronizando Imágenes"
rsync -av --delete-after $HOME/Imágenes/ gabi-sv:/mnt/datos/Gabi/Backups/Imágenes

echo "Sincronizando .gnupg"
rsync -av --delete-after $HOME/.gnupg/ gabi-sv:/mnt/datos/Gabi/Backups/.gnupg

echo "Sincronizando .password-store"
rsync -av --delete-after $HOME/.password-store/ gabi-sv:/mnt/datos/Gabi/Backups/.password-store

echo "Sincronizando .ssh"
rsync -av --delete-after $HOME/.ssh/ gabi-sv:/mnt/datos/Gabi/Backups/.ssh
