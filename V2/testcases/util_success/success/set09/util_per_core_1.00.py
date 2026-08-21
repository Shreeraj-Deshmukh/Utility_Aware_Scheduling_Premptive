"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199989, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199989, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.135918, 'e_o_k': [0.262613, 0.210090, 0.168072], 'p_i': 10, 'u_i': 4.1073},
        {'id': 1, 'e_m': 6.496741, 'e_o_k': [0.660238, 0.528190, 0.422552, 0.338042], 'p_i': 20, 'u_i': 3.7559},
        {'id': 2, 'e_m': 13.540622, 'e_o_k': [1.376080, 1.100864, 0.880691, 0.704553], 'p_i': 40, 'u_i': 4.2943},
        {'id': 3, 'e_m': 17.784908, 'e_o_k': [2.964151, 2.371321], 'p_i': 80, 'u_i': 1.0411},
        {'id': 4, 'e_m': 1.300513, 'e_o_k': [0.159899, 0.127919, 0.102335], 'p_i': 40, 'u_i': 4.5861},
        {'id': 5, 'e_m': 14.508804, 'e_o_k': [1.294812, 1.035850, 0.828680, 0.662944, 0.530355], 'p_i': 40, 'u_i': 4.2047},
        {'id': 6, 'e_m': 5.622074, 'e_o_k': [0.691239, 0.552991, 0.442393], 'p_i': 20, 'u_i': 1.7569},
        {'id': 7, 'e_m': 4.488151, 'e_o_k': [0.456113, 0.364890, 0.291912, 0.233530], 'p_i': 20, 'u_i': 1.4071},
    ]
    B_BUDGET = 239.199989
    return processors, tasks, B_BUDGET
