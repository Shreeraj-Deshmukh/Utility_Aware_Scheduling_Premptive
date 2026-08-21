"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 114.079997, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.5, "seed": 1073, "set": 73, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}
"""

_SPEC = '{"B": 114.079997, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.5, "seed": 1073, "set": 73, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.599170, 'e_o_k': [0.343786, 0.275029, 0.220023], 'p_i': 10, 'u_i': 3.9348},
        {'id': 1, 'e_m': 4.185659, 'e_o_k': [3.255513, 2.604410], 'p_i': 20, 'u_i': 2.2078},
        {'id': 2, 'e_m': 0.147250, 'e_o_k': [0.069834, 0.055867, 0.044694, 0.035755], 'p_i': 40, 'u_i': 1.5646},
        {'id': 3, 'e_m': 1.074448, 'e_o_k': [0.835682, 0.668545], 'p_i': 80, 'u_i': 4.4075},
        {'id': 4, 'e_m': 0.209273, 'e_o_k': [0.162768, 0.130214], 'p_i': 10, 'u_i': 2.2030},
        {'id': 5, 'e_m': 0.141966, 'e_o_k': [0.081456, 0.065165, 0.052132], 'p_i': 80, 'u_i': 2.4770},
        {'id': 6, 'e_m': 0.313697, 'e_o_k': [0.119041, 0.095233, 0.076186, 0.060949, 0.048759, 0.039007], 'p_i': 80, 'u_i': 1.9604},
        {'id': 7, 'e_m': 1.741302, 'e_o_k': [0.825821, 0.660657, 0.528525, 0.422820], 'p_i': 20, 'u_i': 2.4961},
    ]
    B_BUDGET = 114.079997
    return processors, tasks, B_BUDGET
