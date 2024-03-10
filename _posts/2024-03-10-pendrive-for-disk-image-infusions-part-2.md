---
title: "Pendrive for disk image infusions, part 2"
tags: learning automation vmlinuz bootable pendrive tiny-core-linux hardware efi qemu
---

This is the continuation of the [previous part]({% post_url 2024-03-02-pendrive-for-disk-image-infusions %}).

The changes is better to follow with the repo [https://github.com/aleksandr-vin/pfdii](https://github.com/aleksandr-vin/pfdii).

This material was of a real good help: [https://www.rodsbooks.com/efi-bootloaders/](https://www.rodsbooks.com/efi-bootloaders/), and some learnings
I've noted [here]({% post_url 2024-03-06-booting-efi-in-qemu %}). Another nice finding made installing the syslinux bootloader as easy as just
copying it's *syslinux.efi* binary under the **fallback** name, which is */EFI/BOOT/bootx64.efi* to the *ESP* partition, saving from the
burden of installing VBR and MBR.

The memory consumption increased with EFI boot, and init ramdisk was not fitting into 128M anymore. Plus linux started complaining about misalignment
between architectures of EFI (64 bit) and linux (32 bit), which effected as not listing */dev/nvme0n1* device (in my test scenario). That forced me to
move to TinyCore pure 64 bit, which also increased the memory requirements. I ended up using 256M and it works for me now.

## Update

1. Booting in system with Secure Boot enabled can be worked around using [PreLoader](http://www.rodsbooks.com/efi-bootloaders/secureboot.html#preloader).

2. TinyCore linux provisions mounts in */etc/fstab* (not automount) when system boots, and it's wise to wait for the records to appear there and
   then just `mount /mnt/sda2`.
