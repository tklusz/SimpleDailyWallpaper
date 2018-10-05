# Simple-Daily-Background
A Python script that allows for a unique background each day of the year. 
Easily modifiable. Requires gsettings.

## Getting started
### Creating your Wallpaper directory.
To get started, create a new directory for your wallpapers:

```
home/(username)/Pictures/Wallpapers
```

### Adding your wallpapers.

![](/images/Example.png)

Add as many wallpapers to your new directory as you want, up to a maximum of 1 per day. There is only one requirement.
Here's how it works:

> If you want a wallpaper to start showing on the 4th of July, you would name that wallpaper "185", and keep the extension (jpeg, png, etc). That wallpaper would continue being shown until you reach a different wallpaper with a closer number (e.g. 186 on July 5th).

To calculate your day numbers, check out [this website.](https://www.epochconverter.com/days/2018)

### Adding this script to your startup.
In order for this script to change your wallpaper daily, it is recomended to add a custom command to your startup:

```
python /(absolute path to this script)/Backgrounds.py
e.g. python /home/tklusz/Programs/Backgrounds.py
```

![](/images/Example-Startup.png)

For the more technically inclined users, its possible to set up a cron-job every 24 hours. This is also useful if you don't turn your computer off every day. If you would like to set this up instead, run:

```
crontab -e
```

Select whichever editor you prefer, then add the following to the end:

```
0 12 * * * python /(absolute path to this script)/Backgrounds.py
```

This script should now run daily at noon.

### Modification
The Python script is well commented and easily editable. If you aren't using gsettings or would like to use a different directory for your wallpapers, you only need to change 1 line each.
