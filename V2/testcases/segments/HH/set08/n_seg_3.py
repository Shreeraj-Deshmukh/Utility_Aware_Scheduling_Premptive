"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640009, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640009, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.713852, 'e_o_k': [0.409587, 0.327670, 0.262136], 'p_i': 10, 'u_i': 2.0315},
        {'id': 1, 'e_m': 0.102835, 'e_o_k': [0.059003, 0.047203, 0.037762], 'p_i': 20, 'u_i': 1.5871},
        {'id': 2, 'e_m': 5.612205, 'e_o_k': [3.220118, 2.576094, 2.060875], 'p_i': 40, 'u_i': 1.8711},
        {'id': 3, 'e_m': 3.855748, 'e_o_k': [2.212314, 1.769851, 1.415881], 'p_i': 80, 'u_i': 4.9538},
        {'id': 4, 'e_m': 0.273644, 'e_o_k': [0.157009, 0.125607, 0.100486], 'p_i': 20, 'u_i': 2.3994},
        {'id': 5, 'e_m': 4.043450, 'e_o_k': [2.320013, 1.856010, 1.484808], 'p_i': 10, 'u_i': 1.5904},
        {'id': 6, 'e_m': 1.584227, 'e_o_k': [0.908983, 0.727186, 0.581749], 'p_i': 40, 'u_i': 2.4893},
        {'id': 7, 'e_m': 0.773382, 'e_o_k': [0.443744, 0.354995, 0.283996], 'p_i': 10, 'u_i': 4.7173},
    ]
    B_BUDGET = 176.640009
    return processors, tasks, B_BUDGET
