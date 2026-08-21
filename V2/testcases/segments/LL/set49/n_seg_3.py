"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.000930, 'e_o_k': [0.000190, 0.000152, 0.000122], 'p_i': 10, 'u_i': 1.4564},
        {'id': 1, 'e_m': 0.515106, 'e_o_k': [0.105555, 0.084444, 0.067555], 'p_i': 20, 'u_i': 1.4719},
        {'id': 2, 'e_m': 0.249987, 'e_o_k': [0.051227, 0.040981, 0.032785], 'p_i': 40, 'u_i': 1.0831},
        {'id': 3, 'e_m': 1.651906, 'e_o_k': [0.338505, 0.270804, 0.216643], 'p_i': 80, 'u_i': 3.5025},
        {'id': 4, 'e_m': 8.382844, 'e_o_k': [1.717796, 1.374237, 1.099389], 'p_i': 40, 'u_i': 4.4776},
        {'id': 5, 'e_m': 0.849274, 'e_o_k': [0.174032, 0.139225, 0.111380], 'p_i': 20, 'u_i': 3.2024},
        {'id': 6, 'e_m': 0.094741, 'e_o_k': [0.019414, 0.015531, 0.012425], 'p_i': 10, 'u_i': 1.4405},
        {'id': 7, 'e_m': 0.857443, 'e_o_k': [0.175706, 0.140564, 0.112452], 'p_i': 10, 'u_i': 3.4151},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET
