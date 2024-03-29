import homework_fullstack.utils as hwu


def test_cantons_count():
    cantons = hwu.read_data("../dataset/canton.csv")
    assert len(cantons.index) == 26


def test_codes():
    codes = hwu.read_codes()
    assert "id" in codes
    assert "canton" in codes
    assert "code" in codes
    assert len(codes["id"]) == 26


def test_to_int():
    assert hwu.to_int("123 456") == 123456
    assert hwu.to_int("123 abc") == 123
    assert hwu.to_int("123:") == 123


def test_normalize_string():
    assert hwu.normalize_string("hommes") == "hommes"
    assert hwu.normalize_string("canton ") == "canton"
    assert hwu.normalize_string("E_trangers") == "etrangers"


def test_validate_column_names():
    assert hwu.validate_column_names(
        ["hommes", "canton", "suisses", "femmes", "etrangers"]
    )
    assert not hwu.validate_column_names(["hommes", "suisses", "femmes", "etrangers"])
