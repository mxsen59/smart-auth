# smart-auth
Device authentication using OpenCV

## Cloning
```shell
git clone https://github.com/masen-f/smart-auth
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
9. xscreensaver (Linux systems)

## Installing dependencies
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

### Windows systems
```
py -m pip install -r requirements.txt
```

## Getting started
### Linux systems
```shell
cd smart-auth/src/
mkdir dataset/
python3 generate.py
python3 train.py
```

## Getting started
### Windows systems
```shell
.\setup.bat
cd .\src\
py generate.py
py train.py
```

## Running smart-auth
```shell
python3 authorizer.py
```
or
```
py authorizer.py
```
