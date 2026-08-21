"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.624601, 'e_o_k': [0.485801, 0.388641], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 0.610894, 'e_o_k': [0.475140, 0.380112], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 3.088315, 'e_o_k': [2.402023, 1.921618], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 4.046818, 'e_o_k': [3.147525, 2.518020], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 0.371042, 'e_o_k': [0.288588, 0.230870], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 3.248721, 'e_o_k': [2.526783, 2.021427], 'p_i': 40, 'u_i': 2.6468},
        {'id': 6, 'e_m': 0.378075, 'e_o_k': [0.294058, 0.235246], 'p_i': 20, 'u_i': 2.0597},
        {'id': 7, 'e_m': 5.584342, 'e_o_k': [4.343377, 3.474702], 'p_i': 80, 'u_i': 3.8347},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
