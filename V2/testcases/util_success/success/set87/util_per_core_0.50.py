"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.055071, 'e_o_k': [0.183401, 0.146721, 0.117377, 0.093901, 0.075121], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.396516, 'e_o_k': [0.048752, 0.039002, 0.031201], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 1.461769, 'e_o_k': [0.130453, 0.104362, 0.083490, 0.066792, 0.053434], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 15.379881, 'e_o_k': [1.890969, 1.512775, 1.210220], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 3.022118, 'e_o_k': [0.307126, 0.245701, 0.196561, 0.157248], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 2.202229, 'e_o_k': [0.367038, 0.293631], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 1.295953, 'e_o_k': [0.115655, 0.092524, 0.074019, 0.059215, 0.047372], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 2.842934, 'e_o_k': [0.253713, 0.202970, 0.162376, 0.129901, 0.103921], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 119.600001
    return processors, tasks, B_BUDGET
