from dataclasses import dataclass
import os
import json
import yaml


@dataclass
class LlmResult:
    content: str
    meta: dict
    path_to_save: str
    
    def save(self, root_path: str = "./results/generated") -> None:
        full_dir_path = f"{root_path}/{self.path_to_save}"
        os.makedirs(full_dir_path, exist_ok=True)
        
        with open(f"{full_dir_path}/content.yaml", "w", encoding='UTF-8') as f:
            yaml.dump(self.extract_yaml_content(), f, allow_unicode=True, default_flow_style=False)
        with open(f"{full_dir_path}/meta.json", "w", encoding='UTF-8') as f:
            json.dump(self.meta, f, ensure_ascii=False, indent=4)
    
    
    def extract_yaml_content(self) -> dict:
        if self.content.startswith("```yaml") and self.content.endswith("```"):
            yaml_content = self.content[len("```yaml"): -len("```")].strip()
        else:
            yaml_content = self.content.strip()
        return yaml.safe_load(yaml_content)