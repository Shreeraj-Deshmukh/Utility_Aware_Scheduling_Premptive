"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440001, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440001, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.768926, 'e_o_k': [0.062527, 0.050021, 0.040017, 0.032014, 0.025611, 0.020489], 'p_i': 10, 'u_i': 3.3901},
        {'id': 1, 'e_m': 5.917137, 'e_o_k': [0.481162, 0.384930, 0.307944, 0.246355, 0.197084, 0.157667], 'p_i': 20, 'u_i': 2.3217},
        {'id': 2, 'e_m': 7.876937, 'e_o_k': [0.800502, 0.640401, 0.512321, 0.409857], 'p_i': 40, 'u_i': 2.1118},
        {'id': 3, 'e_m': 2.269177, 'e_o_k': [0.230607, 0.184486, 0.147589, 0.118071], 'p_i': 80, 'u_i': 4.2305},
        {'id': 4, 'e_m': 25.441395, 'e_o_k': [4.240233, 3.392186], 'p_i': 80, 'u_i': 2.0791},
        {'id': 5, 'e_m': 13.909378, 'e_o_k': [2.318230, 1.854584], 'p_i': 80, 'u_i': 1.4810},
        {'id': 6, 'e_m': 12.663207, 'e_o_k': [2.110534, 1.688428], 'p_i': 80, 'u_i': 3.5439},
        {'id': 7, 'e_m': 1.517876, 'e_o_k': [0.123429, 0.098743, 0.078994, 0.063195, 0.050556, 0.040445], 'p_i': 10, 'u_i': 4.1958},
    ]
    B_BUDGET = 167.440001
    return processors, tasks, B_BUDGET
