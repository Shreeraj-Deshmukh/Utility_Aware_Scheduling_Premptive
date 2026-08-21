"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.399429, 'e_o_k': [0.059411, 0.047528, 0.038023, 0.030418, 0.024335], 'p_i': 10, 'u_i': 2.8237},
        {'id': 1, 'e_m': 2.463878, 'e_o_k': [0.684411, 0.547529], 'p_i': 20, 'u_i': 2.8601},
        {'id': 2, 'e_m': 8.416090, 'e_o_k': [1.425490, 1.140392, 0.912313, 0.729851], 'p_i': 40, 'u_i': 4.7969},
        {'id': 3, 'e_m': 34.116873, 'e_o_k': [5.074499, 4.059599, 3.247680, 2.598144, 2.078515], 'p_i': 80, 'u_i': 4.3760},
    ]
    B_BUDGET = 110.400007
    return processors, tasks, B_BUDGET
