"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 77.280001, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.1, "seed": 1009, "set": 9, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.10"}
"""

_SPEC = '{"B": 77.280001, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.1, "seed": 1009, "set": 9, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.737228, 'e_o_k': [0.482563, 0.386051], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 1.414064, 'e_o_k': [0.191645, 0.153316, 0.122653, 0.098122, 0.078498, 0.062798], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 8.894962, 'e_o_k': [1.323025, 1.058420, 0.846736, 0.677389, 0.541911], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 3.992321, 'e_o_k': [1.108978, 0.887182], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.156022, 'e_o_k': [0.023206, 0.018565, 0.014852, 0.011882, 0.009505], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.352177, 'e_o_k': [0.072168, 0.057734, 0.046187], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 5.127088, 'e_o_k': [0.868409, 0.694727, 0.555782, 0.444626], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 1.297088, 'e_o_k': [0.265797, 0.212637, 0.170110], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 77.280001
    return processors, tasks, B_BUDGET
