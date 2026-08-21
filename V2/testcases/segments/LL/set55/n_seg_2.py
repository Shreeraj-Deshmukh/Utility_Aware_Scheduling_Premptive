"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200018, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200018, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.181209, 'e_o_k': [0.328114, 0.262491], 'p_i': 10, 'u_i': 4.5874},
        {'id': 1, 'e_m': 0.909186, 'e_o_k': [0.252552, 0.202041], 'p_i': 20, 'u_i': 2.7347},
        {'id': 2, 'e_m': 1.009200, 'e_o_k': [0.280333, 0.224267], 'p_i': 40, 'u_i': 4.9671},
        {'id': 3, 'e_m': 5.488802, 'e_o_k': [1.524667, 1.219734], 'p_i': 80, 'u_i': 4.8761},
        {'id': 4, 'e_m': 2.719998, 'e_o_k': [0.755555, 0.604444], 'p_i': 80, 'u_i': 2.5248},
        {'id': 5, 'e_m': 0.142051, 'e_o_k': [0.039459, 0.031567], 'p_i': 10, 'u_i': 4.9532},
        {'id': 6, 'e_m': 0.727869, 'e_o_k': [0.202186, 0.161749], 'p_i': 40, 'u_i': 2.2979},
        {'id': 7, 'e_m': 3.047121, 'e_o_k': [0.846423, 0.677138], 'p_i': 40, 'u_i': 4.0423},
    ]
    B_BUDGET = 55.200018
    return processors, tasks, B_BUDGET
