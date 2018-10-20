# Simple-Daily-Wallpaper
A Python script that allows you to choose your own background each day of the year.

## Getting started
### Creating your Wallpaper directory.
To get started, create the following directory for your wallpapers:

```
home/(username)/Pictures/Wallpapers
```

### Adding your wallpapers.

![](/images/Example.png)

Add as many wallpapers to the directory as you want, up to a maximum of 1 per day (365), and name the pictures in the following way:

> If you want a wallpaper to start showing on the 4th of July, you would name that wallpaper "185", and keep the extension (jpg, png, etc). That wallpaper would continue being shown until you reach another day you have setup. (e.g. 335.jpg will start being displayed on December 1st).

To calculate day numbers, check out [this website.](https://www.epochconverter.com/days/2018)

#### Leap Years.
This script will ignore the 29th of February, and treat it as a second February 28th (day 60). This is to preserve day numbers, for example, Halloween will always be day 304, even on a leap year. As a result, it currently isn't possible to have a unique wallpaper for Februrary 29th.

### Adding this script to your startup.
In order for this script to change your wallpaper daily, it is recomended to add a custom command to your startup:

```
python /(absolute path to this script)/Backgrounds.py
e.g. python /home/tklusz/Programs/Backgrounds.py
```

![](/images/Example-Startup.png)

### Compatability
As of now, this script requires gsettings, which is installed on most Ubuntu-based distros by default. 

This script is confirmed to work with:
 - Elementary OS (Juno and Loki)
 - Ubuntu 18.10, 14.04 LTS

This script should also be compatible with the following:
 - Ubuntu 18.04 LTS
 - Most Ubuntu derivatives (such as Linux Mint) 
 - Manjaro GNOME

If you would like to use this script, but find that it isn't compatible with your system, please provide an alternative command you use to change your wallpaper on this issue: [#4](https://github.com/tklusz/Simple-Daily-Wallpaper/issues/4)

### Modification
The Python script is well commented and easily editable. For example, if you want to change the Wallpaper directory to a different one, only 1 line needs to be changed.
