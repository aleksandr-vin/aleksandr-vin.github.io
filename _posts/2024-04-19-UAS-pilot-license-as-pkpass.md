---
title: "UAS pilot license as pkpass"
tags: drone certificate pilot uas license pkpass wallet
---

I've got a UAS pilot license (basic one A1/A3), via free online course & exam. It took me around 3 hours.

It's issued as a PDF with a barcode, which contains only a link:

```shell
% zbarimg /Users/aleksandrvin/Desktop/Screenshot\ 2024-04-19\ at\ 20.14.10.png
QR-Code:https://learningzone.eurocontrol.int/ilp/customs/Reports/DACUASComp/Certificate/Validation/13821406/?key=a3cb535bb93a2298410a18364c13cf7f888a6ca53dc6be40859cbfb11f65f1e5
scanned 1 barcode symbols from 1 images in 0,1 seconds
```

I like the concept of using virtual cards instead of plastic. So let's try converting the certificate
data into a pleasant-looking pkpass.

This is the original [post](https://web.archive.org/web/20240106141741/https://tranzer.com/blogs/how-to-create-your-own-wallet-passes-pkpass/) that I am using.

Here are the steps I've followed (with some fixes):

### Create Request Certificate
1. Open the keychain app on your macOS machine
1. Click on Keychain access > Certificate assistant > Request a Certificate From a Certificate Authority
1. Fill in email address and select Save to Disk
1. Click on Continue and Save (*.certSigningRequest*)

### Create Identifier
1. Go to identifiers > create an identifier by clicking on the plus sign
1. Select Pass Type IDs > Click on continue
1. Fill in Description and a unique identifier `pass.com.{{company_name}}.{{project_name}}` > Click on Register
1. Select your registered pass identifier in list > Click on Create Certificate
1. Fill in your Pass certificate Name > Upload *.certSigningRequest* certificate from previous step, click Continue
 
### Create Certificate
1. Download the created certificate (*.cer*)
1. Double click and open in Keychain app, choose *login*, then go to My Certificates > Click on relevant certificate > Export Pass Type ID:… > Save in *.p12* format
1. Choose a password (This is your export password)

### Create a pkpass by command line:
- Create a pass certificate with openssl and pkcs12 hashing type
- The Path to .p12 certificate (created in the previous step) goes as input
- The output will be the private key which will be stored in a *.pem* file
- Replace `<import password>` with your export password

```shell
openssl pkcs12 -in Certificates.p12 -clcerts -nokeys -out passcertificate.pem -passin pass:<import password> -legacy
```

### Create a pass key with the following command
- The Path to .p12 certificate (created in the previous step) goes as input
- Replace <import password> with your export password
- Replace <key password> with a new key password (This will be your key password)

```shell
openssl pkcs12 -in Certificates.p12 -nocerts -out passkey.pem -passin pass:<import password> -passout pass:<key password> -legacy
```

### Export WWDR certificate
1. In the Keychain access app > Certificates tab > Right click on the “Apple Worldwide Developer relations Certification Authority” (a.k.a WWDR)
1. Export “Apple ….” > Save as .pem file and rename it WWDR.pem (for convenience)

### Define the information in your pass in the *pass.json* file
More information about the interface can be found [here](https://web.archive.org/web/20240106141741/https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/Creating.html#//apple_ref/doc/uid/TP40012195-CH4-SW1).

passTypeIdentifier key should have the value of your pass type id (starts with pass.com…)
teamIdetifier key should be filled in, value can be found in the Apple developer account on the top right corner under your name.

## A repo

And this is a nice fork of a tool that automates the process: https://github.com/aleksandr-vin/PKPassCreator
