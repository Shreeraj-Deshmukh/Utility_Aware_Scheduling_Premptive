"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400007, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400007, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.287406, 'e_o_k': [0.263813, 0.211050, 0.168840], 'p_i': 10, 'u_i': 1.0054},
        {'id': 1, 'e_m': 1.012025, 'e_o_k': [0.171413, 0.137131, 0.109705, 0.087764], 'p_i': 20, 'u_i': 3.4815},
        {'id': 2, 'e_m': 1.154572, 'e_o_k': [0.320714, 0.256571], 'p_i': 40, 'u_i': 3.3828},
        {'id': 3, 'e_m': 7.183412, 'e_o_k': [1.216703, 0.973362, 0.778690, 0.622952], 'p_i': 80, 'u_i': 4.2011},
        {'id': 4, 'e_m': 19.309471, 'e_o_k': [3.270574, 2.616459, 2.093168, 1.674534], 'p_i': 40, 'u_i': 4.7650},
        {'id': 5, 'e_m': 1.541158, 'e_o_k': [0.315811, 0.252649, 0.202119], 'p_i': 80, 'u_i': 4.1252},
    ]
    B_BUDGET = 110.400007
    return processors, tasks, B_BUDGET
