# Exifer (Exif Renamer)

This program will rename all the files in the specified folder with the creation date extracted from the exif data of each file. 
For example a photo taken the 12/24/2019 15:53:02 named img005.jpg will become 20192412_155302.jpg. Or 20192412_155302_img005.jpg if the `-kn` flag is specified.

This program require the library `pymediainfo` and will try to automatically install it if not already installed.

```
Usage: python exifer.py -f folderPath  [-kn]

Options:
   -f folderPath  The program will rename all files in this forder (and all subfolders). 
                  Only files with the following extensions will be renamed: 
	               .jpg, .cr2, .mp4, .mts, .mov and .tif
   -kn            (Optional) Keep the original name.
```
