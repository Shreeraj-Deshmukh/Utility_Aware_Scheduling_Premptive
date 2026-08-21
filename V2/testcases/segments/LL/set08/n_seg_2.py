"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.356926, 'e_o_k': [0.099146, 0.079317], 'p_i': 10, 'u_i': 2.0315},
        {'id': 1, 'e_m': 0.051417, 'e_o_k': [0.014283, 0.011426], 'p_i': 20, 'u_i': 1.5871},
        {'id': 2, 'e_m': 2.806103, 'e_o_k': [0.779473, 0.623578], 'p_i': 40, 'u_i': 1.8711},
        {'id': 3, 'e_m': 1.927874, 'e_o_k': [0.535521, 0.428416], 'p_i': 80, 'u_i': 4.9538},
        {'id': 4, 'e_m': 0.136822, 'e_o_k': [0.038006, 0.030405], 'p_i': 20, 'u_i': 2.3994},
        {'id': 5, 'e_m': 2.021725, 'e_o_k': [0.561590, 0.449272], 'p_i': 10, 'u_i': 1.5904},
        {'id': 6, 'e_m': 0.792114, 'e_o_k': [0.220032, 0.176025], 'p_i': 40, 'u_i': 2.4893},
        {'id': 7, 'e_m': 0.386691, 'e_o_k': [0.107414, 0.085931], 'p_i': 10, 'u_i': 4.7173},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET
