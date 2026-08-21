"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.829887, 'e_o_k': [1.423245, 1.138596], 'p_i': 10, 'u_i': 4.8131},
        {'id': 1, 'e_m': 1.807671, 'e_o_k': [0.752838, 0.602270, 0.481816, 0.385453, 0.308362], 'p_i': 20, 'u_i': 1.8577},
        {'id': 2, 'e_m': 1.122762, 'e_o_k': [0.644208, 0.515366, 0.412293], 'p_i': 40, 'u_i': 4.0468},
        {'id': 3, 'e_m': 1.611913, 'e_o_k': [0.671311, 0.537049, 0.429639, 0.343711, 0.274969], 'p_i': 80, 'u_i': 2.5682},
        {'id': 4, 'e_m': 4.641757, 'e_o_k': [1.761444, 1.409155, 1.127324, 0.901859, 0.721487, 0.577190], 'p_i': 80, 'u_i': 1.7800},
        {'id': 5, 'e_m': 0.203879, 'e_o_k': [0.077367, 0.061894, 0.049515, 0.039612, 0.031690, 0.025352], 'p_i': 10, 'u_i': 2.6825},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
