import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from Calculator import add, subtract, multiply, divide

# Link all scenarios in the feature file
scenarios("calculator.feature")

# ── Fixtures (shared state between steps) ──
@pytest.fixture
def context():
   """Holds numbers and result across Given/When/Then."""
   return {}

# ── Given steps ──
@given(parsers.parse('I have the numbers {a:d} and {b:d}'))
def set_numbers(context, a, b):
    context["a"] = a
    context["b"] = b
    context["error"] = None

# ── When steps ──
@when('I add them')
def when_add(context):
    context["result"] = add(context["a"], context["b"])

@when('I subtract them')
def when_subtract(context):
    context["result"] = subtract(context["a"], context["b"])

@when('I multiply them')
def when_multiply(context):
    context["result"] = multiply(context["a"], context["b"])

@when('I divide them')
def when_divide(context):
    try:
        context["result"] = divide(context["a"], context["b"])
    except ValueError as e:
        context["error"] = e

# ── Then steps ──
@then(parsers.parse('the result should be {expected:f}'))
def check_result(context, expected):
    assert context["result"] == expected

@then('a ValueError should be raised')
def check_error(context):
    assert isinstance(context["error"], ValueError)
    assert "Cannot divide by zero" in str(context["error"])


from Calculator import add, subtract,divide,multiply

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0

def test_subtract():
    assert subtract(10,4) == 6
    assert subtract(0,5) == -5

def test_multiply():
    assert multiply(3,4) == 12
    assert multiply(-2,5) == -10

def test_divide():
    assert divide(10,2) == 5.0
    assert divide(7,2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(5,0)
    assert "cannot divide by zero" in str(exc_info.value)
