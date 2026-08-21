"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 47.104003, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.2, "seed": 1056, "set": 56, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.20"}
"""

_SPEC = '{"B": 47.104003, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.2, "seed": 1056, "set": 56, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.20"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.075032, 'e_o_k': [0.407951, 0.326361, 0.261089, 0.208871, 0.167097, 0.133677], 'p_i': 10, 'u_i': 3.8590},
        {'id': 1, 'e_m': 0.138443, 'e_o_k': [0.057657, 0.046126, 0.036901, 0.029521, 0.023616], 'p_i': 20, 'u_i': 3.6983},
        {'id': 2, 'e_m': 0.518452, 'e_o_k': [0.215919, 0.172735, 0.138188, 0.110550, 0.088440], 'p_i': 40, 'u_i': 3.0670},
        {'id': 3, 'e_m': 0.130830, 'e_o_k': [0.101757, 0.081405], 'p_i': 80, 'u_i': 2.2547},
        {'id': 4, 'e_m': 6.327178, 'e_o_k': [4.921138, 3.936911], 'p_i': 80, 'u_i': 3.3628},
        {'id': 5, 'e_m': 0.084400, 'e_o_k': [0.065644, 0.052515], 'p_i': 10, 'u_i': 1.9431},
        {'id': 6, 'e_m': 1.306253, 'e_o_k': [0.544013, 0.435210, 0.348168, 0.278535, 0.222828], 'p_i': 80, 'u_i': 4.2381},
        {'id': 7, 'e_m': 1.671201, 'e_o_k': [0.958886, 0.767109, 0.613687], 'p_i': 10, 'u_i': 1.5683},
    ]
    B_BUDGET = 47.104003
    return processors, tasks, B_BUDGET
