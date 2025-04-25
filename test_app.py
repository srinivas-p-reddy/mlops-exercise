import os
import app

def test_model_file_created():
    result = app.main()
    assert os.path.exists('models/model.pkl')

def test_model_score():
    score = app.main()
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0
