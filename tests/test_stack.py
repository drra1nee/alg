"""
Тестирование стека
"""
import pytest
from src.modules.stack import Stack

def test_stack_empty():
    s = Stack()
    assert s.is_empty()
    assert len(s) == 0
    with pytest.raises(ValueError):
        s.pop()
    with pytest.raises(ValueError):
        s.peek()
    with pytest.raises(ValueError):
        s.min()

def test_stack_push_pop_peek():
    s = Stack()
    s.push(10)
    assert not s.is_empty()
    assert s.peek() == 10
    assert s.min() == 10
    s.push(5)
    assert s.min() == 5
    s.push(7)
    assert s.peek() == 7
    assert s.pop() == 7
    assert s.min() == 5
    assert s.pop() == 5
    assert s.min() == 10

def test_stack_type_check():
    s = Stack()
    s.push(1)
    s.push(2)
    with pytest.raises(TypeError, match="int"):
        s.push(3.0)  # float в int-стек
    s2 = Stack()
    s2.push(1.5)
    s2.push(2.0)
    with pytest.raises(TypeError, match="float"):
        s2.push(3)

def test_stack_clear():
    s = Stack()
    s.push(1)
    s.push(2)
    s.clear()
    assert s.is_empty()
    assert s._element_type is None

def test_stack_show():
    s = Stack()
    s.push(3)
    s.push(1)
    s.push(4)
    assert s.show() == "[4, 1, 3]"
    s.pop()
    assert s.show() == "[1, 3]"
