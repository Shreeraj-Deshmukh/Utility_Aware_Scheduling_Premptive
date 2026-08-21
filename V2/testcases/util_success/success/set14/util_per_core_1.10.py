"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120007, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120007, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.793454, 'e_o_k': [0.465576, 0.372461], 'p_i': 10, 'u_i': 2.9155},
        {'id': 1, 'e_m': 2.172265, 'e_o_k': [0.176641, 0.141313, 0.113051, 0.090440, 0.072352, 0.057882], 'p_i': 20, 'u_i': 4.9157},
        {'id': 2, 'e_m': 19.832507, 'e_o_k': [1.612714, 1.290171, 1.032137, 0.825709, 0.660567, 0.528454], 'p_i': 40, 'u_i': 2.9652},
        {'id': 3, 'e_m': 31.415822, 'e_o_k': [3.192665, 2.554132, 2.043306, 1.634644], 'p_i': 80, 'u_i': 4.8689},
        {'id': 4, 'e_m': 16.176001, 'e_o_k': [1.315379, 1.052303, 0.841842, 0.673474, 0.538779, 0.431023], 'p_i': 40, 'u_i': 4.7382},
        {'id': 5, 'e_m': 0.634993, 'e_o_k': [0.078073, 0.062458, 0.049967], 'p_i': 10, 'u_i': 1.0574},
        {'id': 6, 'e_m': 11.102547, 'e_o_k': [1.128308, 0.902646, 0.722117, 0.577694], 'p_i': 80, 'u_i': 3.6223},
        {'id': 7, 'e_m': 25.347979, 'e_o_k': [4.224663, 3.379731], 'p_i': 80, 'u_i': 4.9982},
    ]
    B_BUDGET = 263.120007
    return processors, tasks, B_BUDGET
