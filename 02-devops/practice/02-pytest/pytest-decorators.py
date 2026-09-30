import pytest
import tempfile
from pathlib import Path

"""This code basically creates a new yaml file in order to
test the function. First of all, the function is called, but the parameter
is a decorator called fixture. This decorator does the hard work to crete 
the file from scratch and add information into it, the the function receives
the path as a parameter and asserts within content"""

@pytest.fixture
def fixture_try():
    temp_file = tempfile.NamedTemporaryFile(mode="r+t", encoding="utf-8", prefix="yaml" , delete=False)
    temp_path = Path(temp_file.name)
    temp_file.write("Hello world, my name is: Nazareno")
    temp_file.close()

    yield temp_path
    if temp_path.exists():
        temp_path.unlink()

def test_file(fixture_try : Path) -> None:
    assert fixture_try.exists()
    content = fixture_try.read_text()
    assert "Nazareno" in content