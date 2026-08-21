"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119998, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119998, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.018491, 'e_o_k': [0.245454, 0.196363, 0.157090, 0.125672, 0.100538, 0.080430], 'p_i': 10, 'u_i': 4.7051},
        {'id': 1, 'e_m': 2.282810, 'e_o_k': [0.380468, 0.304375], 'p_i': 20, 'u_i': 3.8234},
        {'id': 2, 'e_m': 19.438306, 'e_o_k': [1.734737, 1.387790, 1.110232, 0.888185, 0.710548], 'p_i': 40, 'u_i': 4.4045},
        {'id': 3, 'e_m': 13.627633, 'e_o_k': [2.271272, 1.817018], 'p_i': 80, 'u_i': 2.9927},
        {'id': 4, 'e_m': 1.886871, 'e_o_k': [0.314478, 0.251583], 'p_i': 20, 'u_i': 2.7411},
        {'id': 5, 'e_m': 31.984923, 'e_o_k': [5.330820, 4.264656], 'p_i': 80, 'u_i': 1.3548},
        {'id': 6, 'e_m': 7.549248, 'e_o_k': [0.613880, 0.491104, 0.392883, 0.314306, 0.251445, 0.201156], 'p_i': 40, 'u_i': 4.0744},
        {'id': 7, 'e_m': 17.792843, 'e_o_k': [1.446855, 1.157484, 0.925987, 0.740790, 0.592632, 0.474105], 'p_i': 40, 'u_i': 4.8199},
    ]
    B_BUDGET = 263.119998
    return processors, tasks, B_BUDGET
