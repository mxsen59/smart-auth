# smart-auth
Device authentication using OpenCV for Linux systems

## Installing
```
git clone https://github.com/masen-f/smart-auth
```

## Getting started
### Ubuntu based systems
```
cd src/
mkdir dataset/
python3 generate.py
python3 train.py
```

## Running smart-auth
```
python3 authorizer.py
```

## Custom shell script to run smart-auth
my_shell_script_name.sh
```shell
#!/bin/bash

cd /home/masen/Projects/smart-sys-auth/src/

python3 authorizer.py
```

## Adding smart-auth to .bashrc for simple system wide execution
```
sudo nano .bashrc
```
then add at the bottom of .bashrc file
```shell
alias smart-auth='/path/to/your/custom/shell/script.sh &'
```

## Dependencies
1. python 3.9
2. opencv 4.2.0
3. imutils
4. numpy
5. h5py
6. dlib
7. face-recognition
8. xscreensaver
9. xdotool
