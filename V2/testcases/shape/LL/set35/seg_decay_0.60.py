"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.153313, 'e_o_k': [0.035228, 0.021137, 0.012682, 0.007609], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.148369, 'e_o_k': [0.031126, 0.018676, 0.011205, 0.006723, 0.004034, 0.002420], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 2.270223, 'e_o_k': [0.579139, 0.347483, 0.208490], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 7.275677, 'e_o_k': [1.577827, 0.946696, 0.568018, 0.340811, 0.204486], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 2.680502, 'e_o_k': [0.837657, 0.502594], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 1.468106, 'e_o_k': [0.307991, 0.184794, 0.110877, 0.066526, 0.039916, 0.023949], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 0.569881, 'e_o_k': [0.145378, 0.087227, 0.052336], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.303269, 'e_o_k': [0.094772, 0.056863], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
