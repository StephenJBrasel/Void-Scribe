import PromptFlattener
import json

promptFile = r'C:\Users\thepe_000\Desktop\PP5\Void-Web\Enviorment\data\PromptTemplates\follow.1.json'

with open(promptFile) as f:
    template = json.load(f)

print(PromptFlattener.generatePromptFromTemplate(template))