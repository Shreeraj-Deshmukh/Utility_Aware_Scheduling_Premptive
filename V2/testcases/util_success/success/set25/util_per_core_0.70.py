"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440003, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440003, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.799020, 'e_o_k': [0.466503, 0.373203], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 9.074665, 'e_o_k': [1.115738, 0.892590, 0.714072], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 5.113892, 'e_o_k': [0.519705, 0.415764, 0.332611, 0.266089], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 13.272858, 'e_o_k': [2.212143, 1.769714], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 1.818227, 'e_o_k': [0.147852, 0.118282, 0.094625, 0.075700, 0.060560, 0.048448], 'p_i': 40, 'u_i': 4.9580},
        {'id': 5, 'e_m': 2.487958, 'e_o_k': [0.202312, 0.161850, 0.129480, 0.103584, 0.082867, 0.066294], 'p_i': 20, 'u_i': 2.0799},
        {'id': 6, 'e_m': 5.547127, 'e_o_k': [0.924521, 0.739617], 'p_i': 40, 'u_i': 1.2465},
        {'id': 7, 'e_m': 0.640749, 'e_o_k': [0.078781, 0.063025, 0.050420], 'p_i': 10, 'u_i': 3.7304},
    ]
    B_BUDGET = 167.440003
    return processors, tasks, B_BUDGET
