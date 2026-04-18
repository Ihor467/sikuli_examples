# catch the text from an i,age and copy into the clipboard.
# use the script to grab the code snippets from the screen (Youtube ?)

# Import required SikuliX modules
from sikuli import *
import subprocess

def copy_to_clipboard(text):
    """Copy text to clipboard using appropriate method for the OS"""
    # This implementation works for Windows
    # For other OS, you would need different approaches
    subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(text.encode('utf-8'))
    # Alternative for Mac: subprocess.run("pbcopy", universal_newlines=True, input=text)
    # Alternative for Linux: subprocess.run(["xclip", "-selection", "clipboard"], universal_newlines=True, input=text)

# Set up OCR settings for better text recognition
Settings.OcrTextRead = True
Settings.OcrTextSearch = True

# Prompt the user to select a region containing text
popup("Please select a region containing text you want to recognize")

try:
    # User selects region with the mouse
    selected_region = selectRegion("Select region with text")
    
    if selected_region:
        # Recognize text in the selected region
        recognized_text = selected_region.text()
        
        if recognized_text:
            # Print the recognized text to the output
            print("Recognized text:")
            print(recognized_text)
            
            # Copy the recognized text to clipboard
            copy_to_clipboard(recognized_text)
            
            # Notify the user
            popup("Text has been recognized and copied to clipboard!")
        else:
            popup("No text was recognized in the selected region.")
    else:
        popup("No region was selected.")
        
except Exception as e:
    # Error handling
    error_message = "An error occurred: " + str(e)
    print(error_message)
    popup(error_message)