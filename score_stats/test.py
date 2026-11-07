import statistics_utils
def test_calculate_average():
    grade = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    assert statistics_utils.calculate_average(grade) == (85 + 90 + 78) / 3

def test_maximum():
    grade = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    assert statistics_utils.maximum(grade) == 90

def test_minimum():
    grade = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    assert statistics_utils.minimum(grade) == 78

def test_pass_fail():
    grade = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 55}
    passed_students, failed_students = statistics_utils.pass_fail(grade)
    assert passed_students == {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    assert failed_students == {'David': 55}

def test_empty_grade():
    grade = {}
    assert statistics_utils.calculate_average(grade) == 0
    assert statistics_utils.maximum(grade) == None
    assert statistics_utils.minimum(grade) == None
    passed_students, failed_students = statistics_utils.pass_fail(grade)
    assert passed_students == {}
    assert failed_students == {}

if __name__ == "__main__":
    test_calculate_average()
    test_maximum()
    test_minimum()
    test_pass_fail()
    test_empty_grade()
    print("All tests passed!")