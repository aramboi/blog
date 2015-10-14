Title: Turning my "old" RaspberryPi into a simple NAS
Date: 2015-08-19
Category: misc
Slug: turning-raspberrypi-into-a-simple-nas-server
Tags: raspberrypi, nas, samba
Summary: This is my step-by-step guide on how to setup a RaspberryPi with an external USB drive as a network accessed storage (aka NAS)

This is based on a fresh install of Rasbian ...

Some optional optimisations:

```
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install deborphan
sudo apt-get purge wolfram-engine java-common oracle-java8-jdk
sudo apt-get remove --auto-remove --purge libx11-.*
sudo apt-get autoremove --purge $(deborphan)
```

Installing needed dependencies:

```
sudo apt-get install samba samba-common-bin ntfs-3g hdparm
```

Get the drive identifier (ex. sda):

```
sudo fdisk -l
```

If you want to spin-down your external hard drive when it's inactive for 20 min
(handy if you always want to keep everything powered)

```
sudo hdparm -S 240 /dev/sdx
```

If you are getting this error:

```
HDIO_DRIVE_CMD(setidle) failed: Invalid argument

```

Try this (this worked for me):

```
sudo ls -al /dev/disk/by-id/
sudo hdparm -B127 -S180 /dev/disk/by-id/ata-ST2000DM001-1E6164_W1E842SW
```

Set the permissions on the shared folder:

```
sudo mkdir /media/HDD
sudo chmod -R 777 /media/HDD/
```

Add this to `/etc/fstab` in order to mount the drive properly:

```
/dev/sdx1       /media/HDD      ntfs-3g defaults,noatime  0       0
```

And run the following command:

```
sudo umount /dev/sdx1 && sudo mount /dev/sdx1
```

In the samba config `/etc/samba/smb.conf` uncomment the following:

```
security = user
socket options = TCP_NODELAY
```

And add this under the

```
[media]
    comment = Media share
    path = /media/HDD
    valid users = @users
    force group = users
    create mask = 0660
    directory mask = 0771
    writeable = yes
    browseable = yes
    guest ok  = no
    read only = no
```

Test configuration and restart the server:

```
testparm
sudo service samba restart
```

Creating a user and adding it to samba:

```
sudo useradd <USERNAME> -m -G users
sudo passwd <USERNAME>
sudo smbpasswd -a <USERNAME>
```

