"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.118502, 'e_o_k': [1.647724, 1.318179], 'p_i': 10, 'u_i': 2.6711},
        {'id': 1, 'e_m': 1.874501, 'e_o_k': [1.457945, 1.166356], 'p_i': 20, 'u_i': 2.3833},
        {'id': 2, 'e_m': 1.286629, 'e_o_k': [1.000712, 0.800569], 'p_i': 40, 'u_i': 4.1647},
        {'id': 3, 'e_m': 1.712942, 'e_o_k': [1.332288, 1.065830], 'p_i': 80, 'u_i': 1.2796},
        {'id': 4, 'e_m': 2.907669, 'e_o_k': [2.261521, 1.809216], 'p_i': 10, 'u_i': 2.4526},
        {'id': 5, 'e_m': 0.484065, 'e_o_k': [0.376495, 0.301196], 'p_i': 10, 'u_i': 3.7482},
        {'id': 6, 'e_m': 7.564502, 'e_o_k': [5.883502, 4.706802], 'p_i': 80, 'u_i': 2.1247},
        {'id': 7, 'e_m': 0.284703, 'e_o_k': [0.221436, 0.177148], 'p_i': 40, 'u_i': 4.6336},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
