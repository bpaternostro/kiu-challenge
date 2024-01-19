import pytest

from ..solution import PackageController

from .constants import DUMMY_DATE, DUMMY_RATE

class TestPackageController:
    
    @pytest.mark.parametrize("test_input,expected", [(20, 160.0), (30, 240.0), (40, 320.0)]) # cheking with multiple rates
    def test_generate_total_ok(self, mocker_open_file, test_input, expected):
        input_file = "input_fake.txt"
        processing_date = "2024-01-18"
        rate = test_input # subtotal with mocked input must be 160.0
        pc = PackageController(p_date=processing_date, input_file = input_file, rate=rate)
        resp = pc.generate_total_report()
        assert isinstance(resp, list)
        assert pc.total == expected
        assert len(pc.sub_totals) == 4 # there is 4 registers
    
    def test_generate_total_empty_result(self, mocker_open_file):
        input_file = "input_fake.txt"
        pc = PackageController(p_date=DUMMY_DATE, input_file = input_file, rate=DUMMY_RATE)
        resp = pc.generate_total_report()
        assert isinstance(resp, list)
        assert not len(resp)
        assert not len(pc.sub_totals) # there is no registers

    def test_export_results_ok(self, mocker_open_file):
        input_file = "input_fake.txt"
        output_name = "result1.txt"
        processing_date = "2024-01-18"
        pc = PackageController(p_date=processing_date, input_file = input_file, rate=DUMMY_RATE)
        resp = pc.generate_total_report()
        result = pc.export_results(resp, output_name)
        assert result

    def test_export_results_empty_data(self, mocker_open_file):
        input_file = "input_fake.txt"
        output_name = "result1.txt"
        pc = PackageController(p_date=DUMMY_DATE, input_file = input_file, rate=DUMMY_RATE)
        data_to_be_exported = []
        result = pc.export_results(data_to_be_exported, output_name)
        assert not result

    def test_wrong_input_format(self):
        input_file = "input.wrong"
        pc = PackageController(p_date=DUMMY_DATE, input_file = input_file, rate=DUMMY_RATE)
        with pytest.raises(Exception) as e:
            pc.generate_total_report()

    def test_wrong_output_format(self):
        data_to_be_exported = []
        input_file = "input.text"
        output_name = "result.wrong"
        pc = PackageController(p_date=DUMMY_DATE, input_file = input_file, rate=DUMMY_RATE)
        with pytest.raises(Exception) as e:
            pc.export_results(data_to_be_exported, output_name)

    def test_check_file_format(self):
        input_file = "input.txt"
        wrong_file = "input.text2"
        pc = PackageController(p_date=DUMMY_DATE, input_file = input_file, rate=DUMMY_RATE)
        assert pc._check_file_format(input_file) is None
        with pytest.raises(Exception) as e:
            pc._check_file_format(wrong_file)

    def test_normalize_values(self):
        check = "input\n"
        check2 = "input"
        pc = PackageController(p_date=DUMMY_DATE, input_file = check, rate=DUMMY_RATE)
        assert pc._normalize_values(check) == check2
        assert check2 == check2