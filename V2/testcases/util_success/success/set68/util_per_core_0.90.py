"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280003, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280003, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.020441, 'e_o_k': [0.002513, 0.002011, 0.001608], 'p_i': 10, 'u_i': 3.5457},
        {'id': 1, 'e_m': 0.916181, 'e_o_k': [0.081763, 0.065410, 0.052328, 0.041863, 0.033490], 'p_i': 20, 'u_i': 2.0812},
        {'id': 2, 'e_m': 12.702290, 'e_o_k': [1.032908, 0.826326, 0.661061, 0.528849, 0.423079, 0.338463], 'p_i': 40, 'u_i': 3.4962},
        {'id': 3, 'e_m': 16.712551, 'e_o_k': [2.054822, 1.643858, 1.315086], 'p_i': 80, 'u_i': 3.6650},
        {'id': 4, 'e_m': 38.192231, 'e_o_k': [3.408398, 2.726718, 2.181374, 1.745100, 1.396080], 'p_i': 80, 'u_i': 4.9498},
        {'id': 5, 'e_m': 0.664002, 'e_o_k': [0.067480, 0.053984, 0.043187, 0.034550], 'p_i': 10, 'u_i': 3.9677},
        {'id': 6, 'e_m': 27.680734, 'e_o_k': [2.250905, 1.800724, 1.440579, 1.152464, 0.921971, 0.737577], 'p_i': 80, 'u_i': 3.6488},
        {'id': 7, 'e_m': 26.869639, 'e_o_k': [2.730654, 2.184524, 1.747619, 1.398095], 'p_i': 80, 'u_i': 3.0676},
    ]
    B_BUDGET = 215.280003
    return processors, tasks, B_BUDGET
