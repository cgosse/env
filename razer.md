Make a bootable usb using dd on the mac, ubnetbootin didn't work

Make sure you can actually boot, which is something about avoiding a fallback to VESA mode in UEFI
https://forum.manjaro.org/t/qemu-kvm-install-media-fails-to-boot-with-uefi-firmware/14354
```
systemd.mask=mhwd-live.service
```

to get things to lock on suspend no matter what, install slock and remove light-locker.
Then add a systemd script in */etc/systemd/user/suspend.target.wants*

```
[Unit] Description=User suspend actions
Before=suspend.target
[Service]
User=alec
Type=forking
Environment=DISPLAY=:0
ExecStart=/usr/bin/slock
[Install]
WantedBy=suspend.target
```
