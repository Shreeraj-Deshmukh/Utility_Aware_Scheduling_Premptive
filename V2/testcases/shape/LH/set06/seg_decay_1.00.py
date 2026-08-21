"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.561850, 'e_o_k': [0.393295, 0.393295], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 1.499211, 'e_o_k': [0.524724, 0.524724, 0.524724, 0.524724], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 6.285193, 'e_o_k': [2.199818, 2.199818, 2.199818, 2.199818], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.158746, 'e_o_k': [0.111122, 0.111122], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 1.379315, 'e_o_k': [0.482760, 0.482760, 0.482760, 0.482760], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 1.465455, 'e_o_k': [1.025818, 1.025818], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.015684, 'e_o_k': [0.004392, 0.004392, 0.004392, 0.004392, 0.004392], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.033297, 'e_o_k': [0.009323, 0.009323, 0.009323, 0.009323, 0.009323], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
