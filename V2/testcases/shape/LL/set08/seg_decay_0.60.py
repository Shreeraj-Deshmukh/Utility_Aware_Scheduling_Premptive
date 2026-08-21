"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200013, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.200013, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.356926, 'e_o_k': [0.074879, 0.044927, 0.026956, 0.016174, 0.009704, 0.005823], 'p_i': 10, 'u_i': 4.1639},
        {'id': 1, 'e_m': 0.051417, 'e_o_k': [0.011815, 0.007089, 0.004253, 0.002552], 'p_i': 20, 'u_i': 2.0315},
        {'id': 2, 'e_m': 2.806103, 'e_o_k': [0.608541, 0.365124, 0.219075, 0.131445, 0.078867], 'p_i': 40, 'u_i': 1.5871},
        {'id': 3, 'e_m': 1.927874, 'e_o_k': [0.602461, 0.361476], 'p_i': 80, 'u_i': 1.8711},
        {'id': 4, 'e_m': 0.136822, 'e_o_k': [0.042757, 0.025654], 'p_i': 20, 'u_i': 4.9538},
        {'id': 5, 'e_m': 2.021725, 'e_o_k': [0.438438, 0.263063, 0.157838, 0.094703, 0.056822], 'p_i': 10, 'u_i': 2.3994},
        {'id': 6, 'e_m': 0.792114, 'e_o_k': [0.247536, 0.148521], 'p_i': 40, 'u_i': 1.5904},
        {'id': 7, 'e_m': 0.386691, 'e_o_k': [0.098646, 0.059187, 0.035512], 'p_i': 10, 'u_i': 2.4893},
    ]
    B_BUDGET = 55.200013
    return processors, tasks, B_BUDGET
