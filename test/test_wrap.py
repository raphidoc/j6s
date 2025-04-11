from j6s import SixS

def test_run():

    s = SixS()
    s.geometry(30, 260, 180,30, 1, 1)
    s.gas()
    s.aerosol(0.04)
    s.target_altitude()
    s.sensor_altitude()
    s.wavelength(445)

    dict_res = s.run()

    assert isinstance(dict_res, dict)
    assert dict_res['6s_version'] == 2.1

def test_test():

    s = SixS()

    dict_res = s.test()

    assert isinstance(dict_res, dict)
    assert dict_res['6s_version'] == 2.1

# def test_wavelength_limit():
#
#     s = SixS()
#     s.geometry(30, 260, 180, 30, 1, 1)
#     s.gas()
#     s.aerosol(0.04)
#     s.target_altitude()
#     s.sensor_altitude()
#     s.wavelength(180)
#
#     dict_res = s.run()
#
#     assert isinstance(dict_res, dict)
#     assert dict_res['6s_version'] == 2.1


if __name__ == '__main__':
    test_run()
    test_test()
    # test_wavelength_limit()