"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399985, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399985, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.878081, 'e_o_k': [0.224000, 0.134400, 0.080640], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 1.760389, 'e_o_k': [0.369308, 0.221585, 0.132951, 0.079771, 0.047862, 0.028717], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 15.213605, 'e_o_k': [4.754252, 2.852551], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 1.221415, 'e_o_k': [0.256238, 0.153743, 0.092246, 0.055347, 0.033208, 0.019925], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 1.867670, 'e_o_k': [0.476446, 0.285868, 0.171521], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 1.951144, 'e_o_k': [0.409326, 0.245596, 0.147357, 0.088414, 0.053049, 0.031829], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 1.842208, 'e_o_k': [0.469951, 0.281971, 0.169182], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 1.167704, 'e_o_k': [0.364908, 0.218945], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 110.399985
    return processors, tasks, B_BUDGET
