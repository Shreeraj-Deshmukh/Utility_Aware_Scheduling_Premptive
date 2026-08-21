"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279992, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279992, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.909872, 'e_o_k': [0.111869, 0.089496, 0.071596], 'p_i': 10, 'u_i': 3.3502},
        {'id': 1, 'e_m': 0.001776, 'e_o_k': [0.000144, 0.000116, 0.000092, 0.000074, 0.000059, 0.000047], 'p_i': 20, 'u_i': 1.2795},
        {'id': 2, 'e_m': 3.247906, 'e_o_k': [0.399333, 0.319466, 0.255573], 'p_i': 40, 'u_i': 4.0968},
        {'id': 3, 'e_m': 22.286024, 'e_o_k': [3.714337, 2.971470], 'p_i': 80, 'u_i': 1.8773},
        {'id': 4, 'e_m': 17.328775, 'e_o_k': [1.761054, 1.408843, 1.127075, 0.901660], 'p_i': 40, 'u_i': 4.5380},
        {'id': 5, 'e_m': 3.153416, 'e_o_k': [0.256425, 0.205140, 0.164112, 0.131290, 0.105032, 0.084025], 'p_i': 80, 'u_i': 2.5931},
        {'id': 6, 'e_m': 19.485995, 'e_o_k': [3.247666, 2.598133], 'p_i': 40, 'u_i': 2.1006},
        {'id': 7, 'e_m': 31.149129, 'e_o_k': [2.532944, 2.026355, 1.621084, 1.296867, 1.037494, 0.829995], 'p_i': 80, 'u_i': 1.6702},
    ]
    B_BUDGET = 215.279992
    return processors, tasks, B_BUDGET
