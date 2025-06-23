from utils import api_helpers

def test_get_pending_club():
    headers = {
        'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjY0LCJyb2xlIjoiY291bnRyeU93bmVyIiwicHJpbWFyeUNvbnRhY3ROYW1lIjoiSmFtZXMgTGllciIsImlhdCI6MTc1MDcxMjE2NCwiZXhwIjoxNzU4NDg4MTY0fQ.W3wJt_z249ALfsBAiZ-rn50E0QbU6dHooExo7ch6dkQ'
    }
    response = api_helpers.get_all_club(headers)
    data = response.json()
    assert response.status_code == 200
    assert 'data' in data

