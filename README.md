# inverted-audio-effect
Inverting an audio file and playing both together to see inverted audio effect in action. As both cancel out each other and we hear nothing.

Download any audio or use the one have.

This uses VLC pip library, make sure you have following libraries installed.

## Installing dependencies
Install VLC player. In my testing installing VLC with snap does not seem to work (Ubuntu 22.04.3 LTS).
```bash
sudo apt install vlc
```

Install python bindings for the VLC.
```python3
python -m pip install python-vlc
```
