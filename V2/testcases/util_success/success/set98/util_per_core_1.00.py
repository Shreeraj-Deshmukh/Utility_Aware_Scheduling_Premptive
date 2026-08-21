"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199992, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199992, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.185441, 'e_o_k': [0.120472, 0.096377, 0.077102, 0.061681], 'p_i': 10, 'u_i': 1.3669},
        {'id': 1, 'e_m': 1.011737, 'e_o_k': [0.168623, 0.134898], 'p_i': 20, 'u_i': 2.1946},
        {'id': 2, 'e_m': 14.906778, 'e_o_k': [1.514916, 1.211933, 0.969547, 0.775637], 'p_i': 40, 'u_i': 4.4370},
        {'id': 3, 'e_m': 18.615868, 'e_o_k': [2.288836, 1.831069, 1.464855], 'p_i': 80, 'u_i': 1.3292},
        {'id': 4, 'e_m': 13.274109, 'e_o_k': [1.079406, 0.863525, 0.690820, 0.552656, 0.442125, 0.353700], 'p_i': 40, 'u_i': 2.0008},
        {'id': 5, 'e_m': 8.746969, 'e_o_k': [1.075447, 0.860358, 0.688286], 'p_i': 20, 'u_i': 3.5253},
        {'id': 6, 'e_m': 3.707235, 'e_o_k': [0.301460, 0.241168, 0.192934, 0.154348, 0.123478, 0.098782], 'p_i': 20, 'u_i': 3.2983},
        {'id': 7, 'e_m': 21.675065, 'e_o_k': [2.664967, 2.131974, 1.705579], 'p_i': 80, 'u_i': 3.1773},
    ]
    B_BUDGET = 239.199992
    return processors, tasks, B_BUDGET
