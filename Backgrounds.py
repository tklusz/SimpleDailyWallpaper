import pwd 
import os 
import subprocess
import datetime
import re
import calendar

global photo_directory
 
# If you want to change your wallpaper directory to a specific directory, change the following line.
# Example : photo_directory = "home/myname/Pictures/Wallpapers/Daily"
photo_directory = pwd.getpwuid(os.getuid()).pw_dir + "/Pictures/Wallpapers/"

def choosePic():
    """
    This determines what picture to use based on the set number.
    e.g. if today is day 200, you have two images - 205.png, 180.jpeg,
         it will use 180.jpeg.
    It will only use a number before or on today's number.
    """
    
    # Creating a new list to store pics that are on or before today.
    filtered_pics = []
    
    # Retrieves all pics in photo directory.
    all_pics = os.listdir(photo_directory)
    
    # Gets today's day number e.g. 200 (July 19th)
    today = int(datetime.datetime.now().strftime('%j'))
    
    # Gets today's year number e.g. 2018
    current_year = int(datetime.datetime.now().strftime('%Y'))
    
    # If this year is leap year it has 366 days. In order to mantain the same wallpaper each day of the year
    # we have to substract one day from the 29th of February (60 day of the year) onwards.
    if calendar.isleap(current_year) and today > 60:
        today = today - 1
    
    # Current_max and pic_to_use are used in the for loop.
    current_max = -367
    pic_to_use = ""

    # Looping through every pic in the directory.
    for pic in all_pics:
        
        # Using a regex to remove the file extension of the pic (e.g. .jpg).
        date_number_on_pic = re.sub('\.[a-zA-Z]*','',pic)

        # We want to display the wallpaper that's before today's date, and that's closest to today's date.
        # If the pic number is before today, the day number will be smaller. (e.g. 100 vs 150)
        # Subtracting will give us a negative number in this case (e.g. 100-150 = -50).
        # The farther away the pic is from today, the larger the negative number will be (-100 vs -1).
        date_calc = int(date_number_on_pic) - today
    
        # Only negative numbers or 0 will be used, we want to display the closest to 0.
        # Current max is the the negative number closest to 0. 
        # It gets updated whenever a closer number is found.
        if  date_calc <=0 and date_calc > current_max:
            current_max = date_calc
            pic_to_use = pic

    # Note that at the beginning of the year until the first wallpaper in our directory (e.g. 5.png), 
    # the current_max will be -367 (the default value). This is because no pics will make date_calc <=0.
    # As a result, on a new year, we don't change the background until we reach 
    # the first wallpaper for the year.
    if current_max != -367:
        # After we loop through all of the pics,
        # the image number closest to 0 (aka pic_to_use) will be used as our background.
        setWallpaper(pic_to_use)

def setWallpaper(photoname):
    """
    This sets the wallpaper given the relative path of the file.
    Note that this requires gsettings (see README.md).

    input: photoname. This is the entire photo name that the background will be changed to.
           e.g. 129.png
    """

    # This file formatting is required for gsettings. Example:
    # 'file:///home/username/Pictures/Wallpaper/110.png'
    long_file = "'file://" + photo_directory + photoname + "'"

    # This will call the gsettings command to change the background to the new wallpaper.
    # If you are using a different desktop enviornment, you can change the following command:
    subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", long_file])


choosePic()
