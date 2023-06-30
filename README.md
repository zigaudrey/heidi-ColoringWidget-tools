![image](https://github.com/zigaudrey/heidi-ColoringWidget-tools/assets/129554573/47ca23bc-ef6a-4938-8cb4-1bc2e93e9dbf)

# Heidi's ColoringWidget Conversion Tools
Python scripts that convert pictures or retrieve color data for Heidi's ColoringWidget Flash App

## Picture Conversion Tool
Convert a picture into a SOL file to resume or modify on the Flash App.

### Steps for Picture Conversion Tool
1. After downloading the scripts, create an Virtual Environment in the folder and add the PIL Lib. [Check tutorial here](https://www.youtube.com/watch?v=IAvAlS0CuxI)
1. Open the app, choose a picture you want to convert (dimension must be 550 x 550)
1. A new SOL file will be created. It will be added on the same folder as the original picture
1. Go to the directory below:
	- AppData\Roaming\Macromedia\Flash Player\#SharedObjects\9N8E36RZ\#localWithNet\Users\Your_Username\Documents\Flash Files\ColoringWidget
1. Place the new file, delete the old one and rename it **ColoringWidget.sol**
1. Open the Coloring Widget App and the picture is now displayed

## SOL Color Finder
Retreive color values from the SOL File. A list of color values will be displayed and added in a new TXT aside with the target SOL File.

## Story of Heidi's Coloring Widget Tool
Heidi's Coloring Widget (or as I call DA Pixel Maker) is a Flash App created for [the 2010 contest "Show Your Love"](https://web.archive.org/web/20121114101333/https://heidi.deviantart.com/journal/Show-the-Love-Valentine-s-Day-Contest-214219090).
Though to be made for a Valentine-theme contest, artists use it as a Pixel Art software, even after the end of the contest. Until Flash Reader is no longer available.

![image](https://github.com/zigaudrey/heidi-ColoringWidget-tools/assets/129554573/ee2cf4a9-f7af-4320-be18-c4429382be80)
 _Preview of the Flash App_

The Flash App can be downloaded [here](http://st.deviantart.com/news/show-the-love/expressinstall.swf) (If you have FlashPoint, launch with Adobe Flash Player 32.0)

Here are exemple of [Pixel Art made with this Flash App](https://web.archive.org/web/20120119161727/http://browse.deviantart.com/contests/2010/showthelove/)

## Why these tools were made
After the ZDA-Reconstruction-Tool, I decide to take another file to analyze (and take advantage of) and choose the Flash Cookie for Coloring Widget. It was easy to understand but become a frustration overtime. Another factor is that I won't to lose the Art data value and getting the right color is a pain.
I know these Pixel Art are mean to be one-of-the-kind piece of work but these kind of scripts has to exist, right?
