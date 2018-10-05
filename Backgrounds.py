import pwd, os, subprocess, datetime, re;
from calendar import isleap

global home_directory
global photo_directory

# User's home directory.
home_directory = pwd.getpwuid(os.getuid()).pw_dir

# 
# If you want to change your wallpaper directory to a specific directory, change the following line.
# Also, you may remove the lines "global home_directory" and "home_directory = pwd..." above if you change it.
# Example : photo_directory = "home/myname/Pictures/Wallpapers/Daily"
#
photo_directory = home_directory+"/Pictures/Wallpapers/"

def choosePic():
    """
    This determines what picture to use based on the set number.
    e.g. if today is day 200, you have two images - 205.png, 180.jpeg,
         it will use 180.jpeg.
    It will only use a number before or on today's number.
    """

    # Retrieves all pics in photo directory.
    all_pics = os.listdir(photo_directory)
    # Gets today's day number e.g. 200 (July 19th)
    today = int(datetime.datetime.now().strftime('%j'))
    # Get the year. This is to check whether the current year is a leap year
    year = int(datetime.datetime.today().year)
    
    # Creating a new list to store pics that are on or before today.
    filtered_pics = []
    # Current_max and pic_to_use are used in the for loop.
    # Change the value of current max depending whether the current year is a leap year
    if (isleap(year)):
        current_max = -368
    else:
        current_max = -367
    pic_to_use = ""

    # Looping through every pic in the directory.
    for pic in all_pics:
        # Using a regex to remove the file extension of the pic.
        date_number_on_pic = re.sub('\.[a-zA-Z]*','',pic)

        # Calculating the date number on the pic - today's number.
        date_calc = int(date_number_on_pic) - today

        # If the pic number is lower than today's date, it will be negative.
        # Only negative numbers or 0 will be used.
        # The pic we will use is the negative number closest to 0 (or 0).
        if  date_calc <=0 and date_calc > current_max:
            current_max = date_calc
            pic_to_use = pic

    # Note that at the beginning of the year until the first number (e.g. 5.png), pic_to_use will be -367.
    # This is because no pics will make date_calc <=0.
    # As a result, on a new year, we don't change the background
    # until we reach the first number (e.g. 5.png).
    if(pic_to_use != -367)
        # After we loop through all of the pics,
        # The date_calc closest to 0 (aka pic_to_use) will be used as our background.
        setWallpaper(pic_to_use)

def setWallpaper(photoname):
    """
    This sets the wallpaper given the relative path of the file.
    Note that this requires gnome. It will also work with ElementaryOS.

    input: photoname. This is the entire photo name that the background will be changed to.
           e.g. 129.png
    """

    # This file formatting is required for gsettings. Example:
    # 'file:///home/username/Pictures/Wallpaper/110.png'
    long_file = "'file://" + photo_directory + photoname + "'"

    # This will call the gsettings command to change the background to the new pic.
    #
    # If you are using a different desktop enviornment, you can change the following command:
    #
    subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", long_file])


choosePic()
