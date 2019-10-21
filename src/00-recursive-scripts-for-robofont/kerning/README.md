## Using `import-MM_kerning-from_selected_font.py`

First, make sure to uncomment the lines that allow you to fetch a file to copy from, and all files to copy to.

```
copyFrom = getFile("Select file to copy from", allowsMultipleSelection=False, fileTypes=["ufo"])[0]
importTo = getFile("Select files to copy to", allowsMultipleSelection=True, fileTypes=["ufo"])
```

Also comment *out* the preset lists of file paths.

This will run the script, and print out the paths that it is running on. 

For speed, you can then update the preset paths to the paths on your own system.

After that, you can run the script every time you edit kerning in the main master. 

You can even hook up the script to a hotkey shortcut in RoboFont, so that you can run it easily.
