"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.771604, 'e_o_k': [0.114767, 0.091814, 0.073451, 0.058761, 0.047009], 'p_i': 10, 'u_i': 4.5167},
        {'id': 1, 'e_m': 2.288231, 'e_o_k': [0.635620, 0.508496], 'p_i': 20, 'u_i': 2.0571},
        {'id': 2, 'e_m': 8.920614, 'e_o_k': [1.326841, 1.061472, 0.849178, 0.679342, 0.543474], 'p_i': 40, 'u_i': 3.7403},
        {'id': 3, 'e_m': 19.185389, 'e_o_k': [2.600154, 2.080123, 1.664098, 1.331279, 1.065023, 0.852018], 'p_i': 80, 'u_i': 1.1622},
        {'id': 4, 'e_m': 0.020623, 'e_o_k': [0.004226, 0.003381, 0.002705], 'p_i': 40, 'u_i': 4.1752},
        {'id': 5, 'e_m': 1.450798, 'e_o_k': [0.245731, 0.196585, 0.157268, 0.125814], 'p_i': 10, 'u_i': 1.9420},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
