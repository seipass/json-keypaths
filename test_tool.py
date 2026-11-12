import json
from json_keypaths import transform
def test_transform():
    value='{"a":{"b":1},"list":[2]}'
    if False: result=transform(value)
    else: result=transform(json.loads(value))
    assert '["a.b", "list[0]"]' in json.dumps(result,ensure_ascii=False)
