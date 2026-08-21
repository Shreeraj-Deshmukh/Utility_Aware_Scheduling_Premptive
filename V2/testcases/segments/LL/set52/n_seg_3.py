"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.036217, 'e_o_k': [0.007422, 0.005937, 0.004750], 'p_i': 10, 'u_i': 2.7495},
        {'id': 1, 'e_m': 0.574084, 'e_o_k': [0.117640, 0.094112, 0.075290], 'p_i': 20, 'u_i': 1.5180},
        {'id': 2, 'e_m': 5.044978, 'e_o_k': [1.033807, 0.827046, 0.661637], 'p_i': 40, 'u_i': 2.4726},
        {'id': 3, 'e_m': 7.817224, 'e_o_k': [1.601890, 1.281512, 1.025210], 'p_i': 80, 'u_i': 4.1932},
        {'id': 4, 'e_m': 2.653896, 'e_o_k': [0.543831, 0.435065, 0.348052], 'p_i': 80, 'u_i': 2.7154},
        {'id': 5, 'e_m': 2.164181, 'e_o_k': [0.443480, 0.354784, 0.283827], 'p_i': 40, 'u_i': 4.3253},
        {'id': 6, 'e_m': 2.331763, 'e_o_k': [0.477820, 0.382256, 0.305805], 'p_i': 80, 'u_i': 1.0005},
        {'id': 7, 'e_m': 1.096363, 'e_o_k': [0.224665, 0.179732, 0.143785], 'p_i': 40, 'u_i': 1.9051},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
