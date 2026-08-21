"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679995, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679995, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.256635, 'e_o_k': [0.031553, 0.025243, 0.020194], 'p_i': 10, 'u_i': 2.2542},
        {'id': 1, 'e_m': 0.540076, 'e_o_k': [0.043917, 0.035134, 0.028107, 0.022486, 0.017988, 0.014391], 'p_i': 20, 'u_i': 3.1493},
        {'id': 2, 'e_m': 0.758738, 'e_o_k': [0.077108, 0.061686, 0.049349, 0.039479], 'p_i': 40, 'u_i': 4.3022},
        {'id': 3, 'e_m': 16.196605, 'e_o_k': [1.317054, 1.053643, 0.842915, 0.674332, 0.539465, 0.431572], 'p_i': 80, 'u_i': 4.8493},
        {'id': 4, 'e_m': 10.131188, 'e_o_k': [1.688531, 1.350825], 'p_i': 40, 'u_i': 1.1754},
        {'id': 5, 'e_m': 6.084943, 'e_o_k': [0.494807, 0.395846, 0.316677, 0.253341, 0.202673, 0.162138], 'p_i': 40, 'u_i': 3.0798},
        {'id': 6, 'e_m': 0.825239, 'e_o_k': [0.101464, 0.081171, 0.064937], 'p_i': 10, 'u_i': 3.4237},
        {'id': 7, 'e_m': 0.759590, 'e_o_k': [0.061767, 0.049414, 0.039531, 0.031625, 0.025300, 0.020240], 'p_i': 20, 'u_i': 3.1726},
    ]
    B_BUDGET = 95.679995
    return processors, tasks, B_BUDGET
