"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439994, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439994, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.753977, 'e_o_k': [0.245774, 0.196619, 0.157295, 0.125836, 0.100669], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 2.605231, 'e_o_k': [0.211849, 0.169479, 0.135583, 0.108467, 0.086773, 0.069419], 'p_i': 20, 'u_i': 1.3163},
        {'id': 2, 'e_m': 1.988157, 'e_o_k': [0.202049, 0.161639, 0.129311, 0.103449], 'p_i': 40, 'u_i': 1.2768},
        {'id': 3, 'e_m': 24.067994, 'e_o_k': [2.959180, 2.367344, 1.893875], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 10.469163, 'e_o_k': [1.287192, 1.029754, 0.823803], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 1.179520, 'e_o_k': [0.105264, 0.084211, 0.067369, 0.053895, 0.043116], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 1.553709, 'e_o_k': [0.258952, 0.207161], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 18.021046, 'e_o_k': [1.608256, 1.286605, 1.029284, 0.823427, 0.658742], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 167.439994
    return processors, tasks, B_BUDGET
