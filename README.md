# Allegro Hand ZMQ Interface
Adapted from https://github.com/simlabrobotics/allegro_hand_linux_v4 and https://github.com/michguo/allegro_hand_linux_v4.

This interface allows communicating with a v4 Allegro hand via ZMQ.

# Required hardware
1. [Allegro hand v4](http://wiki.wonikrobotics.com/AllegroHandWiki/index.php/Allegro_Hand_v4.0)
2. [PCAN-USB interface](https://www.peak-system.com/PCAN-USB.199.0.html?&L=1)

# Setup instructions
## Prerequisites
### 1. PCAN-USB driver
Download, build, and install PCAN-USB driver for Linux: [libpcan](https://www.peak-system.com/fileadmin/media/linux/can-version-history.php)
```bash
tar -xzvf peak-linux-driver-x.x.tar.gz
cd peak-linux-driver-x.x
make NET=NO
sudo make install
```
#### Troubleshooting
* If encounter 
  ```bash
  src/pcan-settings.c:47:10: fatal error: popt.h: No such file or directory
     47 | #include <popt.h>
      |      	^~~~~~~~
  compilation terminated.
  ```
  Run
  ```bash
  sudo apt install libpopt-dev
  ```

### 2. `libpcanbasic`
Download, build, and install PCAN-Basic API for Linux: [libpcanbasic](https://www.peak-system.com/PCAN-Basic-Linux.433.0.html)
```bash
tar -xzvf PCAN_Basic_Linux-x.x.x.tar.gz
cd PCAN_Basic_Linux-x.x.x/libpcanbasic
make
sudo make install
```

### 3. `libBHand` grasping library
Download, build, and install Grasping Library for Linux: [libBHand](https://www.allegrohand.com/v4-main/grasping-library-for-linux)
```bash
unzip LibBHand_{32|64}.zip
cd libBHand_{32|64}
sudo make install
sudo ldconfig
```


## Installing this interface
Build using cmake "out of source build" style.
```bash
cd allegro_hand_zmq
./build.sh
```

# Usage
## Launching the ZMQ server
1. Connect PCAN-USB and Allegro Hand (make sure to power off Allegro Hand)
1. Start the ZMQ server: `./run_zmq_server.sh`. Keep this running.
1. Power on the Allegro Hand.

## Controlling the hand
Refer to `allegro_zmq/examples/run_rock_paper_scissors.py` for a programming example.
1. Run the user code in a separate terminal after launching the ZMQ server.