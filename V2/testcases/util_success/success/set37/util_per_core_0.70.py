"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439995, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439995, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.167788, 'e_o_k': [0.694631, 0.555705], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 1.256999, 'e_o_k': [0.127744, 0.102195, 0.081756, 0.065405], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 2.911486, 'e_o_k': [0.259830, 0.207864, 0.166291, 0.133033, 0.106427], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 36.472660, 'e_o_k': [3.706571, 2.965257, 2.372206, 1.897764], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 2.299943, 'e_o_k': [0.383324, 0.306659], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 1.288186, 'e_o_k': [0.114962, 0.091970, 0.073576, 0.058860, 0.047088], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 2.219694, 'e_o_k': [0.272913, 0.218331, 0.174664], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 1.475016, 'e_o_k': [0.131635, 0.105308, 0.084246, 0.067397, 0.053918], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 167.439995
    return processors, tasks, B_BUDGET
