"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.330362, 'e_o_k': [0.272615, 0.218092, 0.174474], 'p_i': 10, 'u_i': 2.7301},
        {'id': 1, 'e_m': 0.095834, 'e_o_k': [0.016232, 0.012986, 0.010389, 0.008311], 'p_i': 20, 'u_i': 2.9329},
        {'id': 2, 'e_m': 3.019103, 'e_o_k': [0.511366, 0.409093, 0.327274, 0.261819], 'p_i': 40, 'u_i': 4.3550},
        {'id': 3, 'e_m': 1.448272, 'e_o_k': [0.215414, 0.172331, 0.137865, 0.110292, 0.088234], 'p_i': 80, 'u_i': 2.2741},
        {'id': 4, 'e_m': 0.768295, 'e_o_k': [0.157438, 0.125950, 0.100760], 'p_i': 10, 'u_i': 2.5808},
        {'id': 5, 'e_m': 3.670463, 'e_o_k': [0.545940, 0.436752, 0.349401, 0.279521, 0.223617], 'p_i': 40, 'u_i': 4.5356},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
