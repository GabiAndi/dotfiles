#!/bin/sh

rsync -av --delete-after gabi-sv:/mnt/datos/Gabi/Backups/Documentos/ $HOME/Documentos
rsync -av --delete-after gabi-sv:/mnt/datos/Gabi/Backups/Imágenes/ $HOME/Imágenes
rsync -av --delete-after gabi-sv:/mnt/datos/Gabi/Backups/.gnupg/ $HOME/.gnupg
rsync -av --delete-after gabi-sv:/mnt/datos/Gabi/Backups/.password-store/ $HOME/.password-store
rsync -av --delete-after gabi-sv:/mnt/datos/Gabi/Backups/.ssh/ $HOME/.ssh
