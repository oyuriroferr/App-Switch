import os
import win32com.client


def create_file_shortcut(file_path, shortcut_name=None):
    # Initialize the Windows Shell
    shell = win32com.client.Dispatch("WScript.Shell")

    # Get the path to the desktop
    desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")

    # Set the name of the shortcut and the full path where it will be created
    if not shortcut_name:
        shortcut_name = os.path.basename(file_path)  # Use the original file name if no name is provided
    shortcut_path = os.path.join(desktop, shortcut_name + ".lnk")

    # Create the shortcut
    shortcut = shell.CreateShortcut(shortcut_path)

    # Set the path of the target file
    shortcut.TargetPath = file_path

    # Set the working directory (the directory of the target file)
    shortcut.WorkingDirectory = os.path.dirname(file_path)

    # Set an icon (optional, if not set, it will use the default file icon)
    # shortcut.IconLocation = "C:\\path\\to\\icon.ico"

    # Save the shortcut
    shortcut.save()


# Path to the file for which you want to create a shortcut
file_path = r"%appdata%\oi.txt"

# Call the function to create the shortcut (you can specify a custom shortcut name)
create_file_shortcut(file_path, "Oi")