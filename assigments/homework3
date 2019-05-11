sudo mkdir /boot/grml

sudo echo 'menuentry "Install on sdb1" {
    set root=(hd1,1)
    linux /vmlinuz root=/dev/sdb1 ro quiet splash
    initrd /initrd.img
}
' >> /etc/grub.d/40_custom


sudo mv ~/ubuntu.iso /boot/grml/

sudo update-grub
