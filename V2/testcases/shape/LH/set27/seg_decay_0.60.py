"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319983, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319983, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.707837, 'e_o_k': [1.098792, 0.659275, 0.395565, 0.237339], 'p_i': 10, 'u_i': 3.9517},
        {'id': 1, 'e_m': 0.074416, 'e_o_k': [0.045187, 0.027112, 0.016267, 0.009760, 0.005856], 'p_i': 20, 'u_i': 3.7467},
        {'id': 2, 'e_m': 1.043073, 'e_o_k': [0.633372, 0.380023, 0.228014, 0.136808, 0.082085], 'p_i': 40, 'u_i': 4.6120},
        {'id': 3, 'e_m': 0.422237, 'e_o_k': [0.369457, 0.221674], 'p_i': 80, 'u_i': 4.9202},
        {'id': 4, 'e_m': 0.946737, 'e_o_k': [0.828395, 0.497037], 'p_i': 80, 'u_i': 4.2451},
        {'id': 5, 'e_m': 0.544998, 'e_o_k': [0.476873, 0.286124], 'p_i': 10, 'u_i': 4.7909},
        {'id': 6, 'e_m': 1.274474, 'e_o_k': [0.819974, 0.491984, 0.295191, 0.177114], 'p_i': 10, 'u_i': 3.3523},
        {'id': 7, 'e_m': 0.014372, 'e_o_k': [0.009247, 0.005548, 0.003329, 0.001997], 'p_i': 40, 'u_i': 1.0347},
    ]
    B_BUDGET = 88.319983
    return processors, tasks, B_BUDGET
