"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.049022, 'e_o_k': [0.012506, 0.007503, 0.004502], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 2.109402, 'e_o_k': [0.442527, 0.265516, 0.159310, 0.095586, 0.057351, 0.034411], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 2.697147, 'e_o_k': [0.842858, 0.505715], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 4.992978, 'e_o_k': [1.147284, 0.688370, 0.413022, 0.247813], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 19.099547, 'e_o_k': [4.388683, 2.633210, 1.579926, 0.947955], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.082986, 'e_o_k': [0.019069, 0.011441, 0.006865, 0.004119], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 1.458740, 'e_o_k': [0.335188, 0.201113, 0.120668, 0.072401], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 5.890191, 'e_o_k': [1.502600, 0.901560, 0.540936], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
