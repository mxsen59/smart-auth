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
```
#!/bin/bash

cd /home/masen/Projects/smart-sys-auth/src/

python3 authorizer.py
```

## Adding smart-auth to .bashrc for simple system wide execution
```
sudo nano .bashrc
```
then add at the bottom of .bashrc file
```
alias smart-auth='/home/masen/Desktop/run_authorizer.sh &'
```

## Dependencies

