![image](https://github.com/zigaudrey/heidi-ColoringWidget-tools/assets/129554573/d1c61392-f005-4ec8-a347-bb109cf5f07c)

**You can edit the SOL file with the SOL Editor tool from [JPEX Free Flash Decompiler](https://github.com/jindrapetrik/jpexs-decompiler). What you can do is create a list of color with it. I decided to archive this repository.**

# Heidi's ColoringWidget Tools
Python scripts that convert pictures or retrieve color data for Heidi's ColoringWidget Flash App

## Picture Conversion Tool
Convert a picture into a SOL file to resume or modify on the Flash App.

### Steps for SOL Conversion Tool
1. If you don't have PIL, install it with PIP
1. Open the app, choose a picture you want to convert (dimension must be around 550 x 550)
2. A new SOL file will be created. It will be added on the same folder as the original picture
   ~~Go to the directory below:~~
	~~- AppData\Roaming\Macromedia\Flash Player\#SharedObjects\9N8E36RZ\#localWithNet\Users\Your_Username\Documents\Flash Files\ColoringWidget~~
- ~~Place the new file, delete the old one and rename it **ColoringWidget.sol**~~
- ~~Open the Coloring Widget App and the picture is now displayed~~

1. Use the Sol Editor to edit the Cookie.
	- The file can be found in: AppData\Roaming\Macromedia\Flash Player\#SharedObjects\9N8E36RZ\#localWithNet\Users\Your_Username\Documents\Flash Files\ColoringWidget
1. Copy/paste the list of colors in the SOL Editor.
1. Open the Coloring Widget App and the picture is now displayed

## SOL Color Finder
Retrieve color values from the SOL File. A list of color values will be displayed and added in a new TXT aside with the target SOL File.

## Story of Heidi's Coloring Widget Tool
Heidi's Coloring Widget (or as I call DA Pixel Maker) is a Flash App created for [the 2010 contest "Show Your Love"](https://web.archive.org/web/20121114101333/https://heidi.deviantart.com/journal/Show-the-Love-Valentine-s-Day-Contest-214219090).
Though to be made for the Valentine-theme contest, artists use it as a Pixel Art software, even after the end line.

![image](https://github.com/zigaudrey/heidi-ColoringWidget-tools/assets/129554573/ee2cf4a9-f7af-4320-be18-c4429382be80)
 _Preview of the Flash App_

The Flash App can played [in this journal](https://web.archive.org/web/20121114101333/https://heidi.deviantart.com/journal/Show-the-Love-Valentine-s-Day-Contest-214219090) and downloaded [here](http://st.deviantart.com/news/show-the-love/expressinstall.swf) (If you have FlashPoint, launch with Adobe Flash Player 32.0)

Here are exemple of [Pixel Art made with this Flash App](https://web.archive.org/web/20120119161727/http://browse.deviantart.com/contests/2010/showthelove/)

## External Link ##

[Flash Cookie SOL File Format](https://rewiki.miraheze.org/wiki/Flash_Cookie_SOL) on Reverse Engineering Wiki

## Why these tools were made
After the ZDA-Reconstruction-Tool, I decide to take another file to analyze (and take advantage of) and choose the Flash Cookie for Coloring Widget. It was easy to understand until the three bytes after "grid" part. Another factor is that I won't to lose the Art data value and getting the right color is a pain.

I know these Pixel Art are mean to be one-of-the-kind piece of work but these kind of scripts has to exist, right?

The project has been on hold for months and I have yet to find informations about how Flash software write the sol file and what these means. I feel like the sol files are under-analyze.
