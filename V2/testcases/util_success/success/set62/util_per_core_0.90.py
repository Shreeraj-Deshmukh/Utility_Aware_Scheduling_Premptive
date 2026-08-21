"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279997, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279997, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.425076, 'e_o_k': [0.404179, 0.323344], 'p_i': 10, 'u_i': 4.8534},
        {'id': 1, 'e_m': 7.721688, 'e_o_k': [0.784724, 0.627780, 0.502224, 0.401779], 'p_i': 20, 'u_i': 2.9672},
        {'id': 2, 'e_m': 2.365490, 'e_o_k': [0.192354, 0.153883, 0.123106, 0.098485, 0.078788, 0.063030], 'p_i': 40, 'u_i': 1.4615},
        {'id': 3, 'e_m': 24.185601, 'e_o_k': [2.457886, 1.966309, 1.573047, 1.258438], 'p_i': 80, 'u_i': 3.8621},
        {'id': 4, 'e_m': 7.757659, 'e_o_k': [0.630827, 0.504662, 0.403729, 0.322983, 0.258387, 0.206709], 'p_i': 80, 'u_i': 3.9454},
        {'id': 5, 'e_m': 2.611406, 'e_o_k': [0.321075, 0.256860, 0.205488], 'p_i': 20, 'u_i': 3.6493},
        {'id': 6, 'e_m': 8.373525, 'e_o_k': [1.029532, 0.823625, 0.658900], 'p_i': 20, 'u_i': 1.5799},
        {'id': 7, 'e_m': 13.098671, 'e_o_k': [1.168968, 0.935174, 0.748139, 0.598511, 0.478809], 'p_i': 80, 'u_i': 3.4745},
    ]
    B_BUDGET = 215.279997
    return processors, tasks, B_BUDGET
