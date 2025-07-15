import subprocess
from comfy.model_base import BaseNode, register_node

class ShellCommandNode(BaseNode):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "command": ("STRING", {"default": "ls -la"})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "run"
    CATEGORY = "Custom"

    def run(self, command):
        try:
            output = subprocess.check_output(command, shell=True, text=True)
            return (output.strip(),)
        except subprocess.CalledProcessError as e:
            return (f"Error: {e.output}",)

register_node("ShellCommandNode", ShellCommandNode)
