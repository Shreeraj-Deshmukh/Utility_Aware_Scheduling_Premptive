"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.427962, 'e_o_k': [0.332860, 0.266288], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 1.031123, 'e_o_k': [0.801984, 0.641587], 'p_i': 20, 'u_i': 3.8670},
        {'id': 2, 'e_m': 0.898123, 'e_o_k': [0.698540, 0.558832], 'p_i': 40, 'u_i': 1.6834},
        {'id': 3, 'e_m': 0.364547, 'e_o_k': [0.283537, 0.226829], 'p_i': 80, 'u_i': 3.8684},
        {'id': 4, 'e_m': 1.110849, 'e_o_k': [0.863994, 0.691195], 'p_i': 40, 'u_i': 4.7513},
        {'id': 5, 'e_m': 6.962867, 'e_o_k': [5.415563, 4.332450], 'p_i': 40, 'u_i': 4.4932},
        {'id': 6, 'e_m': 2.975430, 'e_o_k': [2.314224, 1.851379], 'p_i': 40, 'u_i': 1.6064},
        {'id': 7, 'e_m': 0.024091, 'e_o_k': [0.018737, 0.014990], 'p_i': 10, 'u_i': 2.2133},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
