"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.439041, 'e_o_k': [0.251909, 0.201527, 0.161221], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 0.880194, 'e_o_k': [0.505030, 0.404024, 0.323219], 'p_i': 20, 'u_i': 2.6488},
        {'id': 2, 'e_m': 7.606803, 'e_o_k': [4.364559, 3.491647, 2.793318], 'p_i': 40, 'u_i': 4.8206},
        {'id': 3, 'e_m': 0.610708, 'e_o_k': [0.350406, 0.280325, 0.224260], 'p_i': 80, 'u_i': 3.3334},
        {'id': 4, 'e_m': 0.933835, 'e_o_k': [0.535807, 0.428646, 0.342916], 'p_i': 20, 'u_i': 2.1081},
        {'id': 5, 'e_m': 0.975572, 'e_o_k': [0.559754, 0.447804, 0.358243], 'p_i': 20, 'u_i': 1.8691},
        {'id': 6, 'e_m': 0.921104, 'e_o_k': [0.528502, 0.422802, 0.338241], 'p_i': 80, 'u_i': 3.0834},
        {'id': 7, 'e_m': 0.583852, 'e_o_k': [0.334997, 0.267998, 0.214398], 'p_i': 80, 'u_i': 3.6806},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
