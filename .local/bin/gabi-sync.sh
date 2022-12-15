#!/bin/sh

echo "Sincronizando Documentos"
rsync -av --delete-after gabi-sv:/mnt/datos/Gabi/Backups/Documentos/ $HOME/Documentos

echo "Sincronizando Imágenes"
rsync -av --delete-after gabi-sv:/mnt/datos/Gabi/Backups/Imágenes/ $HOME/Imágenes

echo "Sincronizando .gnupg"
rsync -av --delete-after gabi-sv:/mnt/datos/Gabi/Backups/.gnupg/ $HOME/.gnupg

echo "Sincronizando .password-store"
rsync -av --delete-after gabi-sv:/mnt/datos/Gabi/Backups/.password-store/ $HOME/.password-store

echo "Sincronizando .ssh"
rsync -av --delete-after gabi-sv:/mnt/datos/Gabi/Backups/.ssh/ $HOME/.ssh
