"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640015, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.640015, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.505787, 'e_o_k': [0.442563, 0.265538], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.195219, 'e_o_k': [0.139442, 0.083665, 0.050199], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 10.184228, 'e_o_k': [8.911199, 5.346720], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 6.561179, 'e_o_k': [3.854076, 2.312445, 1.387467, 0.832480, 0.499488, 0.299693], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 4.539403, 'e_o_k': [3.971977, 2.383186], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 6.765491, 'e_o_k': [4.352798, 2.611679, 1.567007, 0.940204], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 1.084629, 'e_o_k': [0.658605, 0.395163, 0.237098, 0.142259, 0.085355], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.372698, 'e_o_k': [0.266213, 0.159728, 0.095837], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 176.640015
    return processors, tasks, B_BUDGET
