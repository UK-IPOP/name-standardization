# import standard_names
from standard_names import rules


def test__strip_period():
    # check honorifics
    for honorific in rules.HONORIFICS:
        assert '.' not in rules.strip_periods(honorific), f"Found '.' in {honorific}"
    # check titles
    for title in rules.ACADEMIC_TITLES:
        assert '.' not in rules.strip_periods(title), f"Found '.' in {title}"
    # check suffixes
    for suffix in rules.SUFFIXES:
        assert '.' not in rules.strip_periods(suffix), f"Found '.' in {suffix}"
    # specific relevant test cases
    assert rules.strip_periods('Dr.') == 'Dr', 'Doctor test failed'
    assert rules.strip_periods('Ph.D.') == 'PhD', 'Ph.D. test failed'
    assert rules.strip_periods('Ph.D') == 'PhD', 'Ph.D test failed'
