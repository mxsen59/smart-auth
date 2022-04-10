echo "Installing dependencies..."

sudo pacman -S python-opencv
sudo pacman -S xscreensaver
pip install sklearn
pip install imutils
pip install numpy
pip install h5py
pip install dlib
pip install face-recognition

echo "Finished installing dependencies"