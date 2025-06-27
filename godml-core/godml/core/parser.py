import yaml
from pathlib import Path
from godml.core.models import PipelineDefinition

def load_pipeline(yaml_path: str) -> PipelineDefinition:
    with open(Path(yaml_path), "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)
    return PipelineDefinition(**content)
