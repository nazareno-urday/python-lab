import pytest

def is_valid_hostname_char(char: str) -> bool:
    if "a" <= char <= "z":
        return True
    if "0" <= char <= "9":
        return True
    if char == "-":
        return True
    return False


def check_url_status(url: str) -> tuple[int | str, str]:
    if url == "https://google.com":
        return (200, "OK")
    if url == "https://fakesite123.org/notfound":
        return (404, "HTTP_ERROR (404)")
    if url == "http://httpbin.org/status/503":
        return (503, "HTTP_ERROR (503)")
    if url == "http://localhost:1":
        return ("CONNECTION_ERROR", "CONNECTION_ERROR")
    return ("UNKNOWN", "UNKNOWN")

# Duplicated test logic
def test_valid_a():
    assert is_valid_hostname_char("a") is True

def test_valid_5():
    assert is_valid_hostname_char("5") is True

def test_valid_underscore():
    assert is_valid_hostname_char("_") is False

# Testing with pytest mark.parametrize and pytest.param

@pytest.mark.parametrize("input_char, expected",
    [
        pytest.param("a", True, id="lower_a"),
        pytest.param("7", True, id="digit_7"),
        pytest.param("0", True, id="digit_0"),
        pytest.param("-", True, id="hyphen"),
        pytest.param("A", False, id="upper_A"),
        pytest.param("_", False, id="underscore")
    ]
)

def test_valid_char(input_char : str, expected : bool):
    assert is_valid_hostname_char(input_char) is expected

# Testing with pytest.param

@pytest.mark.parametrize(
    "url, expected_status_code, expected_text",
    [
        ("https://google.com",
         200,
         "OK"),

        ("https://fakesite123.org/notfound",
         404,
         "HTTP_ERROR (404)"),

        ("http://httpbin.org/status/503",
         503,
         "HTTP_ERROR (503)"),

        ("http://localhost:1",
         "CONNECTION_ERROR",
         "CONNECTION_ERROR"),

        ("https://anything.org",
         "UNKNOWN",
         "UNKNOWN")

    ],
    ids = [
    "google",
    "fakesite",
    "httpbin",
    "localhost",
    "anything"
    ]
)

def test_urls_valid(url:str, expected_status_code: int | str , expected_text:str):
    assert check_url_status(url)[0] is expected_status_code
    assert check_url_status(url)[1] is expected_text