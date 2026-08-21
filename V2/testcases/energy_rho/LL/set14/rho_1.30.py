"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 60.719994, "H": 80, "J": 20, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.3, "seed": 1014, "set": 14, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.30"}
"""

_SPEC = '{"B": 60.719994, "H": 80, "J": 20, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.3, "seed": 1014, "set": 14, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.361229, 'e_o_k': [0.100341, 0.080273], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 1.543444, 'e_o_k': [0.316279, 0.253024, 0.202419], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 5.606336, 'e_o_k': [1.148839, 0.919071, 0.735257], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 2.233033, 'e_o_k': [0.457589, 0.366071, 0.292857], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.084420, 'e_o_k': [0.014299, 0.011439, 0.009151, 0.007321], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 0.994040, 'e_o_k': [0.134720, 0.107776, 0.086221, 0.068977, 0.055181, 0.044145], 'p_i': 40, 'u_i': 1.9821},
        {'id': 6, 'e_m': 3.955611, 'e_o_k': [0.810576, 0.648461, 0.518769], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 3.462576, 'e_o_k': [0.586480, 0.469184, 0.375347, 0.300278], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 60.719994
    return processors, tasks, B_BUDGET
