---
title: "Booting EFI in QEMU"
tags: learning qemu efi boot
---

How you boot a *disk.img* (*dd'd* from a drive) with a EFI bootloader using QEMU.

> On a real computer with UEFI firmware, the firmware is built into the computer's motherboard. This UEFI firmware is responsible for initializing the hardware, finding bootable devices, and then loading and running the EFI boot loaders found on those devices, such as the GRUB boot loader from an EFI System Partition (ESP). When you boot a real computer, the UEFI firmware is already there, performing its role as the bridge between the computer's firmware and the operating system's bootloader.
>
> In contrast, QEMU emulates a virtual machine without inherent UEFI firmware; it defaults to a traditional BIOS firmware emulation. This means that without specifying an alternative, QEMU does not natively provide the UEFI boot process your real system's motherboard firmware does. To emulate a UEFI environment within QEMU, you must explicitly tell QEMU to use an EFI firmware, such as OVMF (Open Virtual Machine Firmware). OVMF is an open-source UEFI firmware designed for use in virtual machines, providing them with UEFI functionality similar to that of real hardware.

From [ChatGPT](https://chat.openai.com/share/c5f31786-2847-4079-9d27-b0e8cf05cf69)

So we need to find a OVMF. I've found a nice notes for [How to set up QEMU working properly on M1 Mac](https://gist.github.com/haharoit/a81fecd847003626ef9ef700e4901d15) (worth checking with
Win10 arm64 installation later), where there is a section on building OVMF. Let's do that.

Don't forget to use the latest appropriate [tag for edk2](https://github.com/tianocore/edk2/tags).

Here is a *Dockerfile* to automate the build process:

```dockerfile
FROM ubuntu:22.04

RUN apt update
RUN apt install -y gcc-multilib g++-multilib git iasl python3 python3-distutils \
                   uuid-dev make g++ nasm gcc-aarch64-linux-gnu

WORKDIR /code

ARG EDK2_TAG=edk2-stable202402

RUN git clone --branch ${EDK2_TAG} https://github.com/tianocore/edk2.git
RUN cd edk2 && git submodule update --init --recursive

# Credits go to https://gist.github.com/haharoit/a81fecd847003626ef9ef700e4901d15
SHELL ["/bin/bash", "-c"]
RUN cd edk2 && \
    source edksetup.sh && \
    make -C BaseTools && \
    build -a X64 -t GCC5 -p OvmfPkg/OvmfPkgX64.dsc

CMD ["cp", "-v", "/code/edk2/Build/OvmfX64/DEBUG_GCC5/FV/OVMF.fd", "/out"]
```

Build the image and get the file out by running the container and mounting current directory as */out*:

```bash
docker build --platform=linux/amd64 -t pfdii-ovmf .

docker run --rm --platform=linux/amd64 -v $(pwd):/out pfdii-ovmf
```

Then booting with QEMU is just:

```bash
qemu-system-x86_64 -m 4G -hda disk.img -boot c -bios OVMF.fd
```

## TBD

These files come with QEMU and look interetsting:

```shell
% find /opt/homebrew/ -name \*.fd
/opt/homebrew//Cellar/qemu/8.2.1/share/qemu/edk2-i386-code.fd
/opt/homebrew//Cellar/qemu/8.2.1/share/qemu/edk2-x86_64-secure-code.fd
/opt/homebrew//Cellar/qemu/8.2.1/share/qemu/edk2-i386-vars.fd
/opt/homebrew//Cellar/qemu/8.2.1/share/qemu/edk2-aarch64-code.fd
/opt/homebrew//Cellar/qemu/8.2.1/share/qemu/edk2-arm-vars.fd
/opt/homebrew//Cellar/qemu/8.2.1/share/qemu/edk2-i386-secure-code.fd
/opt/homebrew//Cellar/qemu/8.2.1/share/qemu/edk2-x86_64-code.fd
/opt/homebrew//Cellar/qemu/8.2.1/share/qemu/edk2-arm-code.fd
```

I managed to run with a combination using:

```
-drive if=pflash,format=raw,readonly,file=$(find /opt/homebrew/ -name edk2-x86_64-code.fd) \
-drive if=pflash,format=raw,file=$(find /opt/homebrew/ -name edk2-i386-vars.fd)
```

But it looks like that run overwritten the *edk2-i386-vars.fd* file inplace and failed to run more (need to investigate it more).


## Reference reading

1. [https://www.rodsbooks.com/efi-bootloaders/](https://www.rodsbooks.com/efi-bootloaders/).
