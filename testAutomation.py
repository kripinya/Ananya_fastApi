import requests

testcases = [
    {
        "url": "http://localhost:8000/add/2/2",
        "expected": 4,
        "description": "Test addition"
    },
    {
        "url": "http://localhost:8000/subtract/2/2",
        "expected": 0,
        "description": "Test subtraction"
    },
    {
        "url": "http://localhost:8000/multiply/2/2",
        "expected": 4,
        "description": "Test multiplication"
    }
]

def test():
    for case in testcases:
        response = requests.get(case["url"])
        result = response.json()["result"]

        assert result == case["expected"], f"Failed: {case['description']}"
        print(f"Passed: {case['description']}")

    print("All tests passed!")

test()