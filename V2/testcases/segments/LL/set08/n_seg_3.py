"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.356926, 'e_o_k': [0.073141, 0.058512, 0.046810], 'p_i': 10, 'u_i': 2.0315},
        {'id': 1, 'e_m': 0.051417, 'e_o_k': [0.010536, 0.008429, 0.006743], 'p_i': 20, 'u_i': 1.5871},
        {'id': 2, 'e_m': 2.806103, 'e_o_k': [0.575021, 0.460017, 0.368013], 'p_i': 40, 'u_i': 1.8711},
        {'id': 3, 'e_m': 1.927874, 'e_o_k': [0.395056, 0.316045, 0.252836], 'p_i': 80, 'u_i': 4.9538},
        {'id': 4, 'e_m': 0.136822, 'e_o_k': [0.028037, 0.022430, 0.017944], 'p_i': 20, 'u_i': 2.3994},
        {'id': 5, 'e_m': 2.021725, 'e_o_k': [0.414288, 0.331430, 0.265144], 'p_i': 10, 'u_i': 1.5904},
        {'id': 6, 'e_m': 0.792114, 'e_o_k': [0.162318, 0.129855, 0.103884], 'p_i': 40, 'u_i': 2.4893},
        {'id': 7, 'e_m': 0.386691, 'e_o_k': [0.079240, 0.063392, 0.050714], 'p_i': 10, 'u_i': 4.7173},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
