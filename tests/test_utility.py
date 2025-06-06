import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utility import lookup_conversion_number_by_id, CONVERSION_FACTORS  # noqa: E402

def test_lookup_conversion_number_by_id(tmp_path):
    csv_file = tmp_path / "c.csv"
    csv_file.write_text("1,,1,2\n2,,2,3\n")
    CONVERSION_FACTORS.clear()
    res1 = lookup_conversion_number_by_id(str(csv_file), "1")
    assert res1 == (10, 100)
    # second call should use cached data
    res2 = lookup_conversion_number_by_id(str(csv_file), "2")
    assert res2 == (100, 1000)
