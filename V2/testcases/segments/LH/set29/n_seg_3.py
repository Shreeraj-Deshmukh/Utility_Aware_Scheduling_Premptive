"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.277588, 'e_o_k': [0.159272, 0.127417, 0.101934], 'p_i': 10, 'u_i': 2.4751},
        {'id': 1, 'e_m': 0.425730, 'e_o_k': [0.244271, 0.195417, 0.156334], 'p_i': 20, 'u_i': 3.6644},
        {'id': 2, 'e_m': 1.697852, 'e_o_k': [0.974177, 0.779342, 0.623473], 'p_i': 40, 'u_i': 2.2976},
        {'id': 3, 'e_m': 1.741157, 'e_o_k': [0.999024, 0.799220, 0.639376], 'p_i': 80, 'u_i': 4.8639},
        {'id': 4, 'e_m': 2.016691, 'e_o_k': [1.157118, 0.925694, 0.740556], 'p_i': 40, 'u_i': 4.5045},
        {'id': 5, 'e_m': 1.394673, 'e_o_k': [0.800222, 0.640178, 0.512142], 'p_i': 80, 'u_i': 1.0020},
        {'id': 6, 'e_m': 1.783638, 'e_o_k': [1.023399, 0.818719, 0.654975], 'p_i': 40, 'u_i': 4.9529},
        {'id': 7, 'e_m': 1.743023, 'e_o_k': [1.000095, 0.800076, 0.640061], 'p_i': 10, 'u_i': 2.3587},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
