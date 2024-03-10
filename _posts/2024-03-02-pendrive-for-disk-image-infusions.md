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

NOTE: Use Control-Option-G to get out of the QEMU machine :)

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

And booting it again. We should get into the user command prompt `tc@box:~$ `.


#### Adding scripts

Good idea to check the http://wiki.tinycorelinux.net/doku.php?id=wiki:remastering -- there you will notice an *Overlay using cat* approach, that's what we are going to start with.

Let's extract the *core.gz* (slightly different call for *cpio* on macos):

```bash
mkdir core
cd code
gunzip -c /Volumes/Core/boot/core.gz | cpio -idmv
```

You'll see lots of errors regarding the devices, if you don't like them, run `sudo cpio` instead, but we will not need devices now.

##### Overlay

Simple check of how the *overlay* method works: let's put a *beep* executable into our *disk.img*.

First we configure the QEMU to emulate PC speaker in the machine via the host sound device, by adding these options to
`qemu-system-x86_64` call:

```
-audiodev coreaudio,id=audio0 -machine pcspk-audiodev=audio0
```

Now when you boot into linux, try running:

```bash
echo -ne "\007"
```

You should hear a **BEEP** through your sound system.

Now let's make beeps more variable. The [beep](https://github.com/johnath/beep/) command line tool should do the trick.

As for now, our linux is 32 bit, so we need to build *beep* for 32 bit architecht:

```bash
wget http://www.johnath.com/beep/beep-1.3.tar.gz
tar zxvf beep-1.3.tar.gz
docker run --rm -it -v $(pwd)/beep-1.3:/code --platform=linux/amd64 -w /code ubuntu:22.04 \
  sh -c 'apt update && apt install -y gcc-multilib g++-multilib && gcc -m32 --static -o beep beep.c'
cp beep-1.3/beep ./
```

Voila:

```bash
% file beep
beep: ELF 32-bit LSB executable, Intel 80386, version 1 (GNU/Linux), statically linked, BuildID[sha1]=2ef1d7d5633c8d375334e3a92739a18f4c48a157, for GNU/Linux 3.2.0, not stripped
```

Now the overlay magic, follow the hands:

```bash
% hdiutil attach disk.img
/dev/disk9          	FDisk_partition_scheme
/dev/disk9s1        	DOS_FAT_32                     	/Volumes/BOOTABLE
% echo beep | cpio -o -H newc | gzip -2 > beep.gz
1751 blocks
% cat /Volumes/BOOTABLE/core.gz beep.gz > /Volumes/BOOTABLE/my-core.gz
% cat > /Volumes/BOOTABLE/syslinux/syslinux.cfg <<EOF
DEFAULT vmlinuz
LABEL vmlinuz
    KERNEL ../vmlinuz
    INITRD ../my-core.gz
EOF

% hdiutil detach /Volumes/BOOTABLE
"disk9" ejected.
```

What we just did:

1. attached the *disk.img* (in macos)
2. created a gzipped cpio archive of our *beep* file in *beep.gz*
3. overlayed *beep.gz* on top of base *core.gz* into a new *my-core.gz*
4. updated config for bootloader to use *my-core.gz*
5. detached *disk.img* to be ready for use

Checking in QEMU, boot:

```bash
qemu-system-x86_64 -m 512M -drive file=disk.img,format=raw,index=0,media=disk -boot c \
  -audiodev coreaudio,id=audio0 -machine pcspk-audiodev=audio0
```

And try in linux:

```bash
/beep -f 1500 -l 1000 -d 5000 -r 3
```

You should hear 3 **BEEPs** of 1500Hz pitch with 5 second interval.

##### (TODO) Playing WAV

Some idea about upgrading from maritime sound signals to a voice: the pendrive can use *espeak* to speak or convert stdout and play it on the audio device
of the box. Need to setup sound on tiny core linux.

##### Scripts

Checking the boot process of the TinyCore linux https://wiki.tinycorelinux.net/doku.php?id=wiki:the_boot_process, I've ended
up placing script in the */home/tc* and running it from *.profile*:

```sh
# Run only in interactive shells
if [ ! -z "$PS1" ]; then
    /home/tc/task.sh
fi
```

The *task.sh*:

```sh
#!/bin/sh

set -e

. /etc/init.d/tc-functions

./check-target.sh

echo "${GREEN}Mounting payload partition...${NORMAL}"

sudo mount /dev/sda1 /mnt

echo "${GREEN}Infusing...${NORMAL}"

echo "${YELLOW}"
sudo dd if=/mnt/tails-amd64-6.0.img of=/dev/nvme0n1 bs=4M status=progress oflag=sync
echo "${NORMAL}"

echo "${GREEN}Done${NORMAL}"

sleep 10

sudo poweroff
```

And *check-target.sh*:

```sh
#!/bin/sh

set -e

. /etc/init.d/tc-functions

echo "${GREEN}Checking...${NORMAL}"

if cat /proc/partitions | grep nvme0n1 >/dev/null
then
    echo "${YELLOW}Target system detected${NORMAL}"
    exit 0
else
    echo "${RED}No ${YELLOW}nvme0n1${RED} device detected${NORMAL}"
    exit 1
fi
```

I've placed *tails-amd64-6.0.img* (treating it as a *gold.img* during scripts development) in the *disk.img*.

It appeared that *dd* version of Tiny Core Linux does not support `status=progress` flag, googling a bit for
a workaround, I've found a *pv*, a [Pipe Viewer](http://www.ivarch.com/programs/pv.shtml) -- small utility to
help me. Again, needs building. This time with configure+make. I will not repeat the build commands, they
will differ only in installing *make* (this time I've made a *Dockerfile* for a builder image) and then
configuring for a static 32 bit build:

```bash
./configure --enable-static CFLAGS=-m32
```

Here is the updated version of *task.sh*:

```sh
#!/bin/sh

set -e

. /etc/init.d/tc-functions

./check-target.sh

echo "${GREEN}Mounting payload partition...${NORMAL}"

sudo mount /dev/sda1 /mnt

echo "${MAGENTA}Infusing...${NORMAL}"

echo -n "${CYAN}"
img=tails-amd64-6.0.img
src="/mnt/${img}"
dst=/dev/nvme0n1
total_size=$(ls -l "${src}" | awk '{ print $5 }')
dd if="${src}" bs=4M \
    | /pv --buffer-size 4096 --direct-io --name "${img}" --size "${total_size}" \
    | sudo dd of="${dst}" bs=4M # oflag=sync
echo -n "${NORMAL}"

echo "${GREEN}Done${NORMAL}"

sleep 10

sudo poweroff
```

It works when *pv* is added (via overlay), here is an asciinema recording of it:
[https://asciinema.org/a/jAABMaC8QHzYHJNRr9krJJOjI](https://asciinema.org/a/jAABMaC8QHzYHJNRr9krJJOjI).

This is the call:

```bash
qemu-system-x86_64 -m 512M \
  -drive file=disk.img,format=raw,index=0,media=disk \
  -boot c \
  -drive file=target-big.img,if=none,id=nvm \
  -device nvme,serial=deadbeef,drive=nvm -display curses
```

**NOTES:** after seeing the results of *pv* tool, I'm thiking of announcing the logs
on a tcp port or broadcasting them or publishing to a remote server port...

**NOTE (2):** `-display curses` is a nice option for `qemu-system-*`.

**NOTE (3):** I've dropped the code to a git repo, it must be accompanied by this post
for now, but I have plans of making it fully automatic + tested (maybe even via github
actions): [https://github.com/aleksandr-vin/pfdii](https://github.com/aleksandr-vin/pfdii).
