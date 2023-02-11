import homework_fullstack.utils as hwu


def test_cantons_count():
    cantons = hwu.read_data("../dataset/canton.csv")
    assert len(cantons.index) == 26


def test_codes():
    codes = hwu.read_codes()
    assert len(codes.keys()) == 26


def test_to_int():
    assert hwu.to_int("123 456") == 123456
    assert hwu.to_int("123 abc") == 123
    assert hwu.to_int("123:") == 123


def test_normalize_string():
    assert hwu.normalize_string("hommes") == "Hommes"
    assert hwu.normalize_string("canton ") == "Canton"
    assert hwu.normalize_string("E_trangers") == "Etrangers"


def test_validate_column_names():
    assert hwu.validate_column_names(
        ["Hommes", "Canton", "Suisses", "Femmes", "Etrangers"]
    )
