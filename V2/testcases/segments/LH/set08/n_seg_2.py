"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.356926, 'e_o_k': [0.277609, 0.222087], 'p_i': 10, 'u_i': 2.0315},
        {'id': 1, 'e_m': 0.051417, 'e_o_k': [0.039991, 0.031993], 'p_i': 20, 'u_i': 1.5871},
        {'id': 2, 'e_m': 2.806103, 'e_o_k': [2.182524, 1.746019], 'p_i': 40, 'u_i': 1.8711},
        {'id': 3, 'e_m': 1.927874, 'e_o_k': [1.499457, 1.199566], 'p_i': 80, 'u_i': 4.9538},
        {'id': 4, 'e_m': 0.136822, 'e_o_k': [0.106417, 0.085134], 'p_i': 20, 'u_i': 2.3994},
        {'id': 5, 'e_m': 2.021725, 'e_o_k': [1.572453, 1.257962], 'p_i': 10, 'u_i': 1.5904},
        {'id': 6, 'e_m': 0.792114, 'e_o_k': [0.616088, 0.492871], 'p_i': 40, 'u_i': 2.4893},
        {'id': 7, 'e_m': 0.386691, 'e_o_k': [0.300760, 0.240608], 'p_i': 10, 'u_i': 4.7173},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
