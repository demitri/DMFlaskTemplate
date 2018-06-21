from .helper_functions import post_json, json_response

# ==========
# Search tests
# ==========

def test_user_query(client):
    response = client.get('/search_api/users?q=muna')
    json = json_response(response)
    print(json)
    assert(response.status_code == 200)
    assert(json['numFound'] == 1)

