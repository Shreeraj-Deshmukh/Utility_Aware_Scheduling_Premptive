"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.855925, 'e_o_k': [0.491104, 0.392883, 0.314307], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 2.062245, 'e_o_k': [1.183256, 0.946604, 0.757284], 'p_i': 20, 'u_i': 3.8670},
        {'id': 2, 'e_m': 1.796246, 'e_o_k': [1.030633, 0.824506, 0.659605], 'p_i': 40, 'u_i': 1.6834},
        {'id': 3, 'e_m': 0.729094, 'e_o_k': [0.418333, 0.334666, 0.267733], 'p_i': 80, 'u_i': 3.8684},
        {'id': 4, 'e_m': 2.221698, 'e_o_k': [1.274745, 1.019796, 0.815837], 'p_i': 40, 'u_i': 4.7513},
        {'id': 5, 'e_m': 13.925733, 'e_o_k': [7.990175, 6.392140, 5.113712], 'p_i': 40, 'u_i': 4.4932},
        {'id': 6, 'e_m': 5.950860, 'e_o_k': [3.414428, 2.731543, 2.185234], 'p_i': 40, 'u_i': 1.6064},
        {'id': 7, 'e_m': 0.048181, 'e_o_k': [0.027645, 0.022116, 0.017693], 'p_i': 10, 'u_i': 2.2133},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
