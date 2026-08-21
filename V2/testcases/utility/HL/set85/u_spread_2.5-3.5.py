"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399985, "H": 80, "J": 37, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 110.399985, "H": 80, "J": 37, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.488440, 'e_o_k': [0.135678, 0.108542], 'p_i': 10, 'u_i': 2.5602},
        {'id': 1, 'e_m': 0.924655, 'e_o_k': [0.156615, 0.125292, 0.100234, 0.080187], 'p_i': 20, 'u_i': 2.9319},
        {'id': 2, 'e_m': 2.288327, 'e_o_k': [0.340363, 0.272290, 0.217832, 0.174266, 0.139413], 'p_i': 40, 'u_i': 3.1850},
        {'id': 3, 'e_m': 4.657210, 'e_o_k': [0.954346, 0.763477, 0.610782], 'p_i': 80, 'u_i': 2.6189},
        {'id': 4, 'e_m': 0.144768, 'e_o_k': [0.019620, 0.015696, 0.012557, 0.010045, 0.008036, 0.006429], 'p_i': 10, 'u_i': 2.7473},
        {'id': 5, 'e_m': 0.140954, 'e_o_k': [0.028884, 0.023107, 0.018486], 'p_i': 40, 'u_i': 2.6917},
        {'id': 6, 'e_m': 4.924673, 'e_o_k': [1.009154, 0.807323, 0.645859], 'p_i': 20, 'u_i': 2.9436},
        {'id': 7, 'e_m': 3.252657, 'e_o_k': [0.550924, 0.440739, 0.352591, 0.282073], 'p_i': 10, 'u_i': 3.0798},
    ]
    B_BUDGET = 110.399985
    return processors, tasks, B_BUDGET
