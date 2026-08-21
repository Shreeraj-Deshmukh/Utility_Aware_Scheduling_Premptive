"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.68, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.68, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.644057, 'e_o_k': [0.146721, 0.117377, 0.093901, 0.075121, 0.060097], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.317213, 'e_o_k': [0.039002, 0.031201, 0.024961], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 1.169415, 'e_o_k': [0.104362, 0.083490, 0.066792, 0.053434, 0.042747], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 12.303905, 'e_o_k': [1.512775, 1.210220, 0.968176], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 2.417694, 'e_o_k': [0.245701, 0.196561, 0.157248, 0.125799], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 1.761783, 'e_o_k': [0.293631, 0.234904], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 1.036762, 'e_o_k': [0.092524, 0.074019, 0.059215, 0.047372, 0.037898], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 2.274347, 'e_o_k': [0.202970, 0.162376, 0.129901, 0.103921, 0.083137], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 95.680000
    return processors, tasks, B_BUDGET
