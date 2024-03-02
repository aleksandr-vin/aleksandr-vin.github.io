---
title: "Pendrive for disk image infusions"
tags: learning automation vmlinuz bootable pendrive tiny-core-linux hardware
---

If we have an image and we need to provision it on hardware box many times, we do an autoloader.

## The definition

Let's start with names. We call the image we want to install on the box a *gold.img*. The box where
we want that *gold.img* running -- a *target* box. We use a usb pendrive as a device that we want to
plug into the *target* box and then reboot.

The pendrive should be bootable and do 3 things:

1. Check if the box it is running can be classified as a *target* one, that'd be a *check function*.
   If check fails, it should start beeping (short, rapid blasts).

2. Give a beep (one prolonged blast) and do *dd* of the *gold.img* to the *target* box preconfigured
   disk device (we should know the exact */dev/xxxx* name). Would be nice to repeat the beep
   (one prolonged blast) at intervals of not more than two minutes while *dd*
   is active. And in case of errors, it should start beeping (short, rapid blasts).

3. Once *dd* is completed, beep (three short blasts) and wait until the pendrive is detached, then
   perform reboot. Would be nice to repeat beeps (one prolonged blast plus two short blasts) at
   intervals of not more than two minutes while waiting.

## The implementation

That's a learning path.

I'll assume that I already have a *golden.img* and start with creating a pendrive. Then I'll use something
like *tails-amd64-6.0.img* as a *golden.img* for tests of the pendrive.

### Making a bootable pendrive

Doing everything on macos arm64, with the help of QEMU.

Using *qemu-img* to create an blank image file:

```bash
qemu-img create disk.img 10G
```

Creating a FAT32:

```bash
% hdiutil attach -nomount disk.img
/dev/disk7
```

```bash
diskutil eraseDisk FAT32 BOOTABLE MBRFormat /dev/disk7
```

Then we copy Linux kernel from [Tiny Core Linux ISO](http://tinycorelinux.net/downloads.html) (Core is enough)
into the root of our partition on *disk.img*:

```bash
wget http://tinycorelinux.net/15.x/x86/release/Core-current.iso

hdiutil attach Core-current.iso

cp /Volumes/Core/boot/{vmlinuz,core.gz} /Volumes/BOOTABLE
```

#### Bootloader

Next step is to install a bootloader. I'm going for Syslinux. Quickly checking, I didn't feel like
finding a syslinux binay for macos, that I can trust, so we'll go for some linux to perform the
`syslinux --install`.

Because I do want to do all the steps virtual, I'll be using QEMU to run it with a command like:

```bash
qemu-system-x86_64 -m 4G -drive file=disk.img,format=raw,index=0,media=disk -boot d -cdrom Core-current.iso 
```

It appeared that *syslinux* either failed to run (on TinyCore and Alpine) or the Linux distro didn't start
-- was heavy or I didn't wait till it does (Debian, Ubuntu, Puppy). I also don't want to install linux just
for running the *syslinux* tool.  I've tried with these images:

- *Core-current.iso*
- *TinyCore-current.iso*
- *alpine-standard-3.19.1-x86_64.iso*
- *debian-live-12.5.0-amd64-cinnamon.iso*
- *fossapup64-9.5.iso*
- *noble-mini-iso-amd64.iso*
- *tails-amd64-6.0.img*
- *ubuntu-22.04.4-live-server-amd64.iso*

Until it worked on ArchLinux (*archlinux-2024.03.01-x86_64.iso*):

```bash
qemu-system-x86_64 -m 4G -drive file=disk.img,format=raw,index=0,media=disk -boot d -cdrom archlinux-2024.03.01-x86_64.iso
```

Then, following the *3.1.2 Manually* section of https://wiki.archlinux.org/title/syslinux, you install Syslinux:

```bash
mount /dev/sda1 /mnt
mkdir /mnt/syslinux
extlinux --install /mnt/syslinux
```

And MBR, first making the partition active:

```bash
fdisk /dev/sda a 1
```

And then copying the *mbr.bin*:

```bash
dd bs=440 count=1 conv=notrunc if=/usr/lib/syslinux/bios/mbr.bin of=/dev/sda
```

Side note: there is an *altmbr.bin* that will not scan for active partitions, but I decided to not go for that (for now).

We `poweroff` the linux machine and can boot a new one from our *disk.img*:

```bash
qemu-system-x86_64 -m 512M -drive file=disk.img,format=raw,index=0,media=disk -boot c
```

We will see that bootloader configuration is missed, to try to boot we can type in the `boot:` prompt:

```
../vmlinuz
```

It will load the kernel, but fail to mount root fs eventually. Not a problem. Stopping the machine and adding the
bootloader config:

```bash
hdiutil attach disk.img

cat > /Volumes/BOOTABLE/syslinux/syslinux.cfg <<EOF
DEFAULT vmlinuz
LABEL vmlinuz
    KERNEL ../vmlinuz
    INITRD ../core.gz
EOF

hdiutil detach /Volumes/BOOTABLE
```

And booting it again. We should get into the user command prompt.

#### Adding start scripts
