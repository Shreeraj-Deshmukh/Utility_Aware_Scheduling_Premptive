"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639977, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.639977, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.713852, 'e_o_k': [0.166565, 0.166565, 0.166565, 0.166565, 0.166565, 0.166565], 'p_i': 10, 'u_i': 4.1639},
        {'id': 1, 'e_m': 0.102835, 'e_o_k': [0.035992, 0.035992, 0.035992, 0.035992], 'p_i': 20, 'u_i': 2.0315},
        {'id': 2, 'e_m': 5.612205, 'e_o_k': [1.571417, 1.571417, 1.571417, 1.571417, 1.571417], 'p_i': 40, 'u_i': 1.5871},
        {'id': 3, 'e_m': 3.855748, 'e_o_k': [2.699023, 2.699023], 'p_i': 80, 'u_i': 1.8711},
        {'id': 4, 'e_m': 0.273644, 'e_o_k': [0.191551, 0.191551], 'p_i': 20, 'u_i': 4.9538},
        {'id': 5, 'e_m': 4.043450, 'e_o_k': [1.132166, 1.132166, 1.132166, 1.132166, 1.132166], 'p_i': 10, 'u_i': 2.3994},
        {'id': 6, 'e_m': 1.584227, 'e_o_k': [1.108959, 1.108959], 'p_i': 40, 'u_i': 1.5904},
        {'id': 7, 'e_m': 0.773382, 'e_o_k': [0.360912, 0.360912, 0.360912], 'p_i': 10, 'u_i': 2.4893},
    ]
    B_BUDGET = 176.639977
    return processors, tasks, B_BUDGET
