# Stable Diffusion WebUI Prompt Refactor Extension  

![promptrefactorpreview](https://user-images.githubusercontent.com/37534421/223649787-cb2681fb-3c28-40c3-b67b-247ca4e855dd.png)

## About  
My first extension that I created for [AUTOMATIC1111's Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) that refactors your prompts text to be more legible and ordered.

## Purpose  
If you have many unorganized prompts in your prompt text box, it can be challenging to find the one you want to adjust. This extension helps you keep your prompt text organized and makes it easier to find specific prompts. For example, suppose you have many prompts related to a particular topic. In that case, you can use the extension to sort those prompts alphabetically, making it easier to find them and adjust them as needed.

## Features  
- Sorts prompts alphabetically  
- Sorts prompts that are enclosed with angle brackets are adjusted to the user's preference.
- Auto spacing (No double spaces, adds spaces where there is none)

## Install guide  
1. In your AUTOMATIC1111's Stable Diffusion WebUI, navigate to the **"Extensions > Install from URL"** Tab.
2. Paste the following URL into the "URL for extension's git repository"
```
https://github.com/JakeCarterDPM/stable-diffusion-webui-prompt-refactor
```
3. Click the **"Install"** button!

## How to Use  
1. Paste prompts into **"Source Prompts"**
2. Click on checkbox settings as desired
3. Press **"Run"** button.
4. Get refactored prompts from **"Refactored Prompts"**

## To Do  
- Make it so the output automatically updates the *"txt2img_prompt"*
- Support for other encapsulations such as (), []. 

## License  
GNU General Public License v3.0

## Contact   
I'm still new to stable diffusion and learning the ropes; so if there's something that should be corrected or if you'd like to contribute, you can message me here: https://discord.gg/VZKv4kP
