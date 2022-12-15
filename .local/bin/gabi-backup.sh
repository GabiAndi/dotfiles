#!/bin/sh

rsync -av --delete-after $HOME/Documentos/ gabi-sv:/mnt/datos/Gabi/Backups/Documentos
rsync -av --delete-after $HOME/Imágenes/ gabi-sv:/mnt/datos/Gabi/Backups/Imágenes
rsync -av --delete-after $HOME/.gnupg/ gabi-sv:/mnt/datos/Gabi/Backups/.gnupg
rsync -av --delete-after $HOME/.password-store/ gabi-sv:/mnt/datos/Gabi/Backups/.password-store
rsync -av --delete-after $HOME/.ssh/ gabi-sv:/mnt/datos/Gabi/Backups/.ssh
