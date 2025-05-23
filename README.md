# ALIEN INVASION


## 📄 Documentation

See below for quickstart installation of the required modules


<details open>
<summary>Install</summary>

### Installing on Linux Mint

Linux Mint (like Ubuntu and Debian) now protects the system Python to avoid breaking the OS by discouraging pip3 install globally.

```bash
sudo apt install python3-venv
python3 -m venv pygame-env      # create a viritual environment with name ___
source pygame-env/bin/activate  # activate virtual environment
```

Then install pygame using:
```bash
sudo apt install pygame
```

To **deactivate** the virtual environment, run:
```bash
deactivate
```