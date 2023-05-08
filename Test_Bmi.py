
import Lab2.Lab2 as bmi

def test_bmi_normal_weight():

    result=bmi.calculate_bmi(1.73,60)
    assert(result==0)
def test_bmi_over_weight():
    # Test over weight
    result = bmi.calculate_bmi(1.73, 85)
    assert (result == 0)
def test_bmi_under_weight():
    # Test under weight
    result = bmi.calculate_bmi(1.73, 50)
    assert (result == -1)