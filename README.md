# inverted-audio-effect <a href="https://www.buymeacoffee.com/parthmandaliya" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" align="right"></a>
Inversing an audio file 180 degrees and playing it together with the original audio to see the inverse audio effect in action. As both cancel out each other.

Download any audio or use the one have.

This uses VLC pip library, make sure you have the following libraries installed.

## Installing dependencies

Install VLC player. In my testing installing VLC with snap does not seem to work (Ubuntu 22.04.3 LTS).
```bash
sudo apt install vlc
```

Install python bindings for the VLC.
```python3
python -m pip install python-vlc
python -m pip install pydub
python -m pip install matplotlib
```
