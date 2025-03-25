from hash_distribution import hash_function3, hash_functionn
from train2 import HashTable
import pytest
from pytest_unordered import unordered
from unittest.mock import patch

a = 'python'
BLANK = object()


def test_should_always_pass():
    assert hash_functionn(a) is not None


def test_should_always_pass2():
    assert hash_functionn(a) == 2606


def test_should_always_pass3():
    assert hash_function3(a, t=True) == (str, 2606)


def test_should_always_pass4():
    assert HashTable(capacity=100) is not None


def test_should_always_pass5():
    assert len(HashTable(capacity=100)) == 0


def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key"] = None
    assert ("key", None) in hash_table.pairs


@pytest.fixture
def hash_table():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data


def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs

    assert len(hash_table) == 3


def test_should_delete_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert ("hola", "hello") in hash_table.pairs
    assert len(hash_table) == 3

    del hash_table["hola"]

    assert "hola" not in hash_table
    assert ("hola", "hello") not in hash_table.pairs
    assert len(hash_table) == 2


def test_should_update_key_value_pair(hash_table):

    assert hash_table['hola'] == 'hello'

    hash_table['hola'] = 'hallo'

    assert hash_table['hola'] == 'hallo'
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 3


def test_should_get_value(hash_table):
    assert unordered(hash_table.values) == ['hello', 37, True]


def test_should_value_empty_hash_table():
    assert HashTable(capacity=100).values == []


def test_should_return_copy_of_values(hash_table):
    assert hash_table.values is not hash_table.values


def test_should_get_keys(hash_table):
    assert hash_table.keys == ["hola", 98.6, False]


def tst_should_get_keys_of_empty_hash_table():
    assert HashTable(capacity=100).keys == set()


def test_should_return_copy_of_keys(hash_table):
    assert hash_table.keys is not hash_table.keys


def test_should_return_pairs(hash_table):
    assert hash_table.pairs == [
        ("hola", "hello"),
        (98.6, 37),
        (False, True)
    ]


def test_should_get_pairs_of_empty_hash_table():
    assert HashTable(capacity=100).pairs == []


def test_should_convert_to_dict(hash_table):
    dctionary = dict(hash_table.pairs)
    assert list(dctionary.keys()) == hash_table.keys
    assert list(dctionary.items()) == hash_table.pairs
    assert list(dctionary.values()) == unordered(hash_table.values)


def test_should_return_length_of_empty_hash_table():
    assert len(HashTable(capacity=100)) == 0


def test_should_not_created_hashtable_with_zero_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=0)


def test_should_not_create_hashtable_with_negative_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=-100)


def test_should_be_report_length(hash_table):
    assert len(hash_table) == 3


def test_should_capacity_of_empty_hash_table():
    assert HashTable(capacity=100).capacity == 100


def test_should_report_capacity(hash_table):
    assert hash_table.capacity == 100


def test_should_create_empty_pairs_slots():
    assert HashTable(capacity=3).pairs == []


def test_should_iterate_over_keys(hash_table):
    for keys in hash_table.keys:
        assert keys in ('hola', 98.6, False)


def test_should_iterate_over_values(hash_table):
    for values in hash_table.values:
        assert values in ('hello', 37, True)


def test_should_iterate_over_pairs(hash_table):
    for keys, values in hash_table.pairs:
        assert keys in hash_table.keys
        assert values in hash_table.values


def test_should_iterate_over_instance(hash_table):
    for key in hash_table:
        assert key in ('hola', 98.6, False)


def test_should_use_dict_literal_for_str(hash_table):
    assert str(hash_table) in {
        "{'hola': 'hello', 98.6: 37, False: True}",
        "{'hola': 'hello', False: True, 98.6: 37}",
        "{98.6: 37, 'hola': 'hello', False: True}",
        "{98.6: 37, False: True, 'hola': 'hello'}",
        "{False: True, 'hola': 'hello', 98.6: 37}",
        "{False: True, 98.6: 37, 'hola': 'hello'}",
    }


def test_should_create_hashtable_from_dict_with_custom_capacity():
    dictionary = {"hola": "hello", 98.6: 37, False: True}

    h_t = HashTable(capacity=100).from_dict(dictionary)

    assert h_t.capacity == len(h_t) * 2
    assert h_t.keys == list(dictionary.keys())
    assert h_t.pairs == list(dictionary.items())
    assert unordered(h_t.values) == list(dictionary.values())


def test_should_have_canonical_string_representation(hash_table):
    assert repr(hash_table) in {
        "HashTable.from_dict({'hola': 'hello', 98.6: 37, False: True})",
        "HashTable.from_dict({'hola': 'hello', False: True, 98.6: 37})",
        "HashTable.from_dict({98.6: 37, 'hola': 'hello', False: True})",
        "HashTable.from_dict({98.6: 37, False: True, 'hola': 'hello'})",
        "HashTable.from_dict({False: True, 'hola': 'hello', 98.6: 37})",
        "HashTable.from_dict({False: True, 98.6: 37, 'hola': 'hello'})",
    }


def test_should_copmpare_equal_to_itself(hash_table):
    assert hash_table == hash_table


def test_should_compare_equal_to_copy(hash_table):
    assert hash_table is not hash_table.copy()
    assert hash_table == hash_table.copy()


def test_should_compare_equal_different_key_value_order(hash_table):
    h1 = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    h2 = HashTable.from_dict({"b": 2, "a": 1, "c": 3})

    assert h1 == h2


def test_should_compare_unequal(hash_table):
    other = HashTable.from_dict({"different": "value"})
    assert hash_table != other


def test_should_compare_unequal_another_data_type(hash_table):
    assert hash_table != 42


def test_should_copy_keys_values_pairs_capacity(hash_table):
    copy = hash_table.copy()
    assert copy is not hash_table
    assert set(hash_table.keys) == set(copy.keys)
    assert unordered(hash_table.values) == copy.values
    assert set(hash_table.pairs) == set(copy.pairs)
    assert hash_table.capacity == copy.capacity


def test_should_compare_equal_different_capacity():
    data = {"a": 1, "b": 2, "c": 3}
    h1 = HashTable.from_dict(data, capacity=50)
    h2 = HashTable.from_dict(data, capacity=100)

    assert h1 == h2


def test_should_detect_hash_collision():
    assert hash("foobar") not in [1, 2, 3]
    with patch("builtins.hash", side_effect=[1, 2, 3]):
        assert hash("foobar") == 1
        assert hash("foobar") == 2
        assert hash("foobar") == 3


with patch("builtins.hash", return_value=24):
    h_t = HashTable(capacity=100)
    h_t['easy'] = 'Requires little effort'
    h_t['difficult'] = 'Needs much skill'


