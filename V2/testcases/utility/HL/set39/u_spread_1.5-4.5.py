"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 35, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 35, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.435325, 'e_o_k': [0.120924, 0.096739], 'p_i': 10, 'u_i': 1.8309},
        {'id': 1, 'e_m': 3.692417, 'e_o_k': [0.625409, 0.500327, 0.400262, 0.320210], 'p_i': 20, 'u_i': 3.5352},
        {'id': 2, 'e_m': 1.661795, 'e_o_k': [0.225219, 0.180176, 0.144140, 0.115312, 0.092250, 0.073800], 'p_i': 40, 'u_i': 3.0536},
        {'id': 3, 'e_m': 21.880045, 'e_o_k': [2.965354, 2.372283, 1.897827, 1.518261, 1.214609, 0.971687], 'p_i': 80, 'u_i': 2.3290},
        {'id': 4, 'e_m': 0.175787, 'e_o_k': [0.048830, 0.039064], 'p_i': 20, 'u_i': 3.6946},
        {'id': 5, 'e_m': 0.532000, 'e_o_k': [0.147778, 0.118222], 'p_i': 20, 'u_i': 2.4720},
        {'id': 6, 'e_m': 0.171451, 'e_o_k': [0.025501, 0.020401, 0.016321, 0.013057, 0.010445], 'p_i': 10, 'u_i': 1.7821},
        {'id': 7, 'e_m': 4.085336, 'e_o_k': [0.837159, 0.669727, 0.535782], 'p_i': 20, 'u_i': 2.3948},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
