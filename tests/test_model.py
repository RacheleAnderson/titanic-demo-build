from src.model import train_and_score

def test_model_runs():
    score = train_and_score("data/titanic.csv")
    assert 0 <= score <= 1, "Score should be between 0 and 1"
