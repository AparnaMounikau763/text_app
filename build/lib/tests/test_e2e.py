from app.main import run_pipeline

def test_e2e_user_flow():
    user_input = "I am VERY happy with this product!!!"

    output = run_pipeline(user_input)

    assert output in ["positive", "neutral", "negative"]