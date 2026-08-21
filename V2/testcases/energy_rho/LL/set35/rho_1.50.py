"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 64.399983, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.5, "seed": 1035, "set": 35, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}
"""

_SPEC = '{"B": 64.399983, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.5, "seed": 1035, "set": 35, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.153313, 'e_o_k': [0.025968, 0.020774, 0.016619, 0.013295], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.148369, 'e_o_k': [0.020108, 0.016087, 0.012869, 0.010295, 0.008236, 0.006589], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 2.270223, 'e_o_k': [0.465210, 0.372168, 0.297734], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 7.275677, 'e_o_k': [1.082175, 0.865740, 0.692592, 0.554073, 0.443259], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 2.680502, 'e_o_k': [0.744584, 0.595667], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 1.468106, 'e_o_k': [0.198969, 0.159175, 0.127340, 0.101872, 0.081498, 0.065198], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 0.569881, 'e_o_k': [0.116779, 0.093423, 0.074739], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.303269, 'e_o_k': [0.084241, 0.067393], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 64.399983
    return processors, tasks, B_BUDGET
