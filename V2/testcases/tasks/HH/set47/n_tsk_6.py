"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.185113, 'e_o_k': [2.477310, 1.981848], 'p_i': 10, 'u_i': 1.2617},
        {'id': 1, 'e_m': 2.093692, 'e_o_k': [0.794510, 0.635608, 0.508486, 0.406789, 0.325431, 0.260345], 'p_i': 20, 'u_i': 4.5683},
        {'id': 2, 'e_m': 3.410608, 'e_o_k': [1.294250, 1.035400, 0.828320, 0.662656, 0.530125, 0.424100], 'p_i': 40, 'u_i': 2.4732},
        {'id': 3, 'e_m': 7.341214, 'e_o_k': [2.785828, 2.228662, 1.782930, 1.426344, 1.141075, 0.912860], 'p_i': 80, 'u_i': 3.5676},
        {'id': 4, 'e_m': 2.542005, 'e_o_k': [1.977115, 1.581692], 'p_i': 20, 'u_i': 2.3263},
        {'id': 5, 'e_m': 1.453470, 'e_o_k': [1.130477, 0.904381], 'p_i': 20, 'u_i': 1.7445},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
