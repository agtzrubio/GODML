# Copyright (c) 2024 Arturo Gutierrez Rubio Rojas
# Licensed under the MIT License

import yaml
from pathlib import Path
from godml.core.models import PipelineDefinition
from godml.utils.path_utils import normalize_path

def load_pipeline(yaml_path: str) -> PipelineDefinition:
    with open(Path(yaml_path), "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)

    # 🔁 Normalizar rutas si están presentes
    if "dataset" in content and "uri" in content["dataset"]:
        content["dataset"]["uri"] = normalize_path(content["dataset"]["uri"])

    if "deploy" in content and "batch_output" in content["deploy"]:
        content["deploy"]["batch_output"] = normalize_path(content["deploy"]["batch_output"])

    return PipelineDefinition(**content)

