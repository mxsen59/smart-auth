# smart-auth
Device authentication using OpenCV for Linux systems

## Installing
```
git clone https://github.com/masen-f/smart-auth
```

## Getting started
### Ubuntu based systems
```
cd smart-auth/src/
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

cd /path/to/smart-auth/src/directory

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
3. sklearn
4. imutils
5. numpy
6. h5py
7. dlib
8. face-recognition
9. xscreensaver
10. xdotool

## Quick install dependencies
### Ubuntu based systems
```shell
cd smart-auth/install/
chmod +x install_deb.sh
./install_deb.sh
```
### Arch based systems
```shell
cd smart-auth/install/
chmod +x install_arch.sh
./install_arch.sh
```
