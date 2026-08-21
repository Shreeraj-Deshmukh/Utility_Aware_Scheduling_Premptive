"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440003, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440003, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.090371, 'e_o_k': [0.009184, 0.007347, 0.005878, 0.004702], 'p_i': 10, 'u_i': 4.0574},
        {'id': 1, 'e_m': 4.316080, 'e_o_k': [0.385181, 0.308145, 0.246516, 0.197213, 0.157770], 'p_i': 20, 'u_i': 2.7090},
        {'id': 2, 'e_m': 6.558488, 'e_o_k': [0.666513, 0.533210, 0.426568, 0.341255], 'p_i': 40, 'u_i': 3.6072},
        {'id': 3, 'e_m': 7.269132, 'e_o_k': [0.591102, 0.472881, 0.378305, 0.302644, 0.242115, 0.193692], 'p_i': 80, 'u_i': 4.5999},
        {'id': 4, 'e_m': 0.676146, 'e_o_k': [0.068714, 0.054971, 0.043977, 0.035182], 'p_i': 20, 'u_i': 4.5815},
        {'id': 5, 'e_m': 7.668353, 'e_o_k': [0.623565, 0.498852, 0.399082, 0.319265, 0.255412, 0.204330], 'p_i': 20, 'u_i': 4.3913},
        {'id': 6, 'e_m': 3.111177, 'e_o_k': [0.518529, 0.414824], 'p_i': 80, 'u_i': 2.4366},
        {'id': 7, 'e_m': 18.568716, 'e_o_k': [1.509946, 1.207957, 0.966366, 0.773093, 0.618474, 0.494779], 'p_i': 40, 'u_i': 1.2704},
    ]
    B_BUDGET = 167.440003
    return processors, tasks, B_BUDGET
