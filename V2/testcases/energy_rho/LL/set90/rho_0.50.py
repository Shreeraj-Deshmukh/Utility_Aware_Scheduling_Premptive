"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 46.000007, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.5, "seed": 1090, "set": 90, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.50"}
"""

_SPEC = '{"B": 46.000007, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.5, "seed": 1090, "set": 90, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.427962, 'e_o_k': [0.063655, 0.050924, 0.040739, 0.032591, 0.026073], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 1.031123, 'e_o_k': [0.139746, 0.111797, 0.089437, 0.071550, 0.057240, 0.045792], 'p_i': 20, 'u_i': 3.3367},
        {'id': 2, 'e_m': 0.898123, 'e_o_k': [0.184042, 0.147233, 0.117787], 'p_i': 40, 'u_i': 4.5472},
        {'id': 3, 'e_m': 0.364547, 'e_o_k': [0.061746, 0.049397, 0.039517, 0.031614], 'p_i': 80, 'u_i': 1.6834},
        {'id': 4, 'e_m': 1.110849, 'e_o_k': [0.308569, 0.246855], 'p_i': 40, 'u_i': 3.8684},
        {'id': 5, 'e_m': 6.962867, 'e_o_k': [1.934130, 1.547304], 'p_i': 40, 'u_i': 4.7513},
        {'id': 6, 'e_m': 2.975430, 'e_o_k': [0.403254, 0.322603, 0.258082, 0.206466, 0.165173, 0.132138], 'p_i': 40, 'u_i': 2.4512},
        {'id': 7, 'e_m': 0.024091, 'e_o_k': [0.006692, 0.005353], 'p_i': 10, 'u_i': 1.4858},
    ]
    B_BUDGET = 46.000007
    return processors, tasks, B_BUDGET
