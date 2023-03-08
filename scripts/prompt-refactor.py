#Created by Jake Carter @ https://github.com/JakeCarterDPM/stable-diffusion-webui-prompt-refactor
import re
import gradio as gr
from modules import script_callbacks, scripts, shared
from modules.shared import opts

def on_ui_settings():
    section = ('prompt-refactor', "Prompt Refactor")

def refactor(inputtext, anglebracketslast, addcommaonend):
    #Get prompts
    inputtext = inputtext.rstrip(", \t\n")
    prompts = inputtext.split(',')

    #Sort <> encapsulated prompts first or last?
    if anglebracketslast:
        sorted_prompts = sorted([p.strip() for p in prompts], key=lambda x: (x.startswith('<'), x.lower()))
    else:
        angle_bracket_prompts = sorted([p.strip() for p in prompts if re.match(r'^<.*>$', p)])
        other_prompts = sorted([p.strip() for p in prompts if not re.match(r'^<.*>$', p)])
        sorted_prompts = angle_bracket_prompts + other_prompts
    outputtext = ', '.join(sorted_prompts)

    #Add comma on end?
    if addcommaonend:
        outputtext = outputtext + ","

    #Output
    return outputtext

class PromptsRefactorScript(scripts.Script):
    def __init__(self) -> None:
        super().__init__()

    def title(self):
        return "Prompt Refactor"

    def show(self, is_txt2img):
        return scripts.AlwaysVisible

    def ui(self, is_txt2img):
        with gr.Group():
            with gr.Accordion("Prompt Refactor", open=False):
                promptssourcetxt = gr.Textbox(value="", label="Source Prompts", lines=5)
                promptsrefactoredtxt = gr.Textbox(value="", label="Refactored Prompts", lines=5)
                anglebracketslast = gr.Checkbox(value=True, label='Place <> prompts after.', info="Mainly for lora. Eg, is it at the front, or the back.")
                addcommaonend = gr.Checkbox(value=True, label='Add comma on end.', info="Save you a keypress c:")
                refactorpromptsbtn = gr.Button(label='Refactor Prompts', variant='primary')
            refactorpromptsbtn.click(fn=refactor, inputs=[promptssourcetxt, anglebracketslast, addcommaonend], outputs=[promptsrefactoredtxt])
        return [promptssourcetxt, promptsrefactoredtxt, anglebracketslast, addcommaonend, refactorpromptsbtn]
script_callbacks.on_ui_settings(on_ui_settings)
