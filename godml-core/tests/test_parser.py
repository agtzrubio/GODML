from godml.core.parser import load_pipeline

def test_load_pipeline():
    pipeline = load_pipeline("examples/godml.yml")
    assert pipeline.name == "churn-prediction"
