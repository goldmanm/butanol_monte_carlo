# coding=utf8

modelChemistry = 'CCSD(T)-F12/cc-pVTZ-F12//B3LYP/CBSB7'
useHinderedRotors = True
useBondCorrections = False

species(    label = 'OH',
    E0 = (28.4187, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(17.0027, 'amu')),
        LinearRotor(inertia=(0.90166, 'amu*angstrom^2'), symmetry=1),
        HarmonicOscillator(frequencies=([3719.11], 'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('[OH]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(    label = 'bQOOH[O]',
    E0 = (
        ***u_E0***-183.68,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([150.661, 240.873, 276.394], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([225.57, 275.496, 339.268, 356.201, 432.579, 479.589, 570.43, 733.818, 751.139, 868.217, 921.203, 941.943, 971.276, 1010.45, 1082.13, 1092.82, 1182.33, 1216.1, 1270.6, 1327.31, 1358.98, 1362.4, 1399.09, 1416.39, 1486.39, 1494.35, 1505.2, 1520.84, 2888.71, 2946.86, 3049.53, 3053.84, 3120.24, 3124.17, 3127.31, 3134.17, 3788.93], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.11668, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0454547, 0.00644376, -6.3599, 0.0213479, 0.0754018],
                    [0.0225323, 0.0043139, 0.330272, 0.00886047, -0.00161386],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.07259, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11996.1, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (8.53579, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.23222, 3.33464, -7.24607, -1.10538, 0.679083],
                    [0.291256, -2.41491, 2.50191, -0.758419, -0.508159],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (11.9624, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.966123, -1.47053, -10.5595, 0.136714, -0.22223],
                    [-0.0649455, -2.31891, 0.392134, 0.342041, -0.453554],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.696488, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-7.23427, -4.41635, 0.227621, 0.322446, -0.149028],
                    [-12.9214, 5.8334, 0.650221, -0.0319144, -0.144618],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('[O]CC(C)(C)OO'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(    label = 'acetone',
    E0 = (
        ***u_E0***-227.687,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(58.0419, 'amu')),
        NonlinearRotor(
            inertia = ([49.7447, 59.6293, 103.139], 'amu*angstrom^2'),
            symmetry = 2,
        ),
        HarmonicOscillator(
            frequencies = ([379.836, 485.39, 537.96, 782.556, 881.948, 885.789, 1087.47, 1120.77, 1235.4, 1388.03, 1390.3, 1466, 1472.27, 1476.19, 1493.43, 1811.07, 3036.06, 3043.18, 3091.49, 3098.84, 3152.24, 3153.38], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.98557, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (2526.62, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.98559, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (2526.62, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('CC(=O)C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(    label = 'H2O',
    E0 = (
        -252.377,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(18.0106, 'amu')),
        NonlinearRotor(
            inertia = ([0.630578, 1.15529, 1.78586], 'amu*angstrom^2'),
            symmetry = 2,
        ),
        HarmonicOscillator(frequencies=([1644.8, 3824.65, 3922], 'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('O'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(    label = 'balkoxyketone',
    E0 = (
        ***u_E0***-170.127,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(87.0446, 'amu')),
        NonlinearRotor(
            inertia = ([107.394, 169.352, 180.067], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([246.201, 270.682, 325.42, 387.88, 459.154, 535.982, 705.737, 776.111, 900.714, 933.231, 985.024, 1019.51, 1076.77, 1138.82, 1269.78, 1345.81, 1382.68, 1417.53, 1475.79, 1486.26, 1495.19, 1504.07, 1837.69, 2949.72, 3049.43, 3056.7, 3125.73, 3131.32, 3135.5, 3137.74], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.03383, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (8541.51, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.06346, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0288122, -0.0532172, -6.16356, 0.0711928, -0.0131231],
                    [0.0435162, 0.0976283, -0.302757, 0.0984989, 0.0372977],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (6.54126, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.56132, -0.672317, -2.83333, -0.610876, 0.576976],
                    [7.04506, -3.24931, -0.601482, -0.10222, -0.0407423],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('CC(C)([O])C=O'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(    label = 'ibutenol',
    E0 = (
        ***u_E0***-192.771,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(72.0575, 'amu')),
        NonlinearRotor(
            inertia = ([60.415, 134.931, 189.106], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([266.605, 273.676, 360.058, 448.874, 583.561, 817.418, 849.082, 977.192, 1015.73, 1047.49, 1104.54, 1172.81, 1201.01, 1317.78, 1391.69, 1418.66, 1429.15, 1479.03, 1493.2, 1500.32, 1508.41, 1773.69, 3009.39, 3016.95, 3047.95, 3052.54, 3097.16, 3137.25, 3152.2, 3895.04], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.9945, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (10526.5, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.97371, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (4763.43, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.375121, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.447, -5.93738, -1.28329, 0.323354, -0.0403791],
                    [0.0149421, 0.0212545, 0.00463222, -0.00272066, 0.00269864],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('CC(C)=CO'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(    label = 'trisub_epoxy',
    E0 = (
        ***u_E0***-337.779,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(88.0524, 'amu')),
        NonlinearRotor(
            inertia = ([90.1114, 166.987, 201.665], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([223.05, 283.149, 362.446, 400.597, 532.379, 551.453, 692.773, 794.744, 914.792, 958.511, 1002.83, 1042.59, 1123.24, 1150.51, 1165.24, 1260.64, 1307.27, 1374.3, 1418.08, 1431, 1472.45, 1481.88, 1490.46, 1505.81, 1524.31, 3037.43, 3045.53, 3096.77, 3104.43, 3120.54, 3122.72, 3130.35, 3836.69], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.98628, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0120909, -0.0162932, -2.88503, 0.0335141, 0.00223636],
                    [-0.00675956, -0.0237039, -0.330621, -0.000334559, 0.00842816],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.03538, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (9112.12, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.871924, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.61082, -0.445028, -0.162812, -0.30709, -0.00374357],
                    [3.74167, -1.06677, -1.52635, 0.33858, -0.0125998],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 2,
    structure = SMILES('CC1(C)OC1O'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(    label = 'bQOOHg',
    E0 = (
        ***u_E0***-198.475,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([171.209, 202.722, 264.412], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([228.24, 292.241, 343.405, 363.394, 386.248, 516.137, 565.065, 610.395, 754.336, 837.832, 856.204, 893.348, 969.063, 1007.62, 1085.27, 1099.35, 1218.79, 1240.48, 1297.15, 1337.66, 1386.04, 1403.32, 1434.75, 1453.45, 1493.67, 1508.13, 1511.61, 3027.61, 3048.94, 3095.67, 3114.72, 3128.86, 3160.24, 3278.24, 3798.14, 3806.52], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.05014, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.091024, 0.039176, -5.97367, 0.00169525, 0.0906778],
                    [0.0414564, -0.0124568, -0.222985, -0.01655, 0.052962],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.820017, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.47726, -3.96356, -2.89264, -0.17257, 0.0522568],
                    [-0.53801, -0.909976, -0.279811, 0.45949, 0.282173],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (13.7535, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-10.8756, -1.15946, -11.3992, -0.257784, 0.866063],
                    [0.440261, 1.93947, -1.40103, 0.538994, -0.174058],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (10.7529, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.44468, 0.585583, -9.24563, -1.49423, 2.80173],
                    [0.729655, -3.86419, 4.7625, -2.96766, 1.14041],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.627564, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.81744, -5.33476, 0.836404, 0.0326989, -0.0370857],
                    [9.76824, -4.19435, -0.492051, 0.0304911, 0.0219645],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (1.74643, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [0.262836, -4.16619, -0.2621, -0.0388514, -0.0600981],
                    [-0.136919, -0.447395, 0.185646, -0.134795, 0.221285],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('OCC(C)([CH2])OO'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(    label = 'CH2O',
    E0 = (
        -118.348,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(30.0106, 'amu')),
        NonlinearRotor(
            inertia = ([1.7758, 12.9429, 14.7187], 'amu*angstrom^2'),
            symmetry = 2,
        ),
        HarmonicOscillator(
            frequencies = ([1206.61, 1274.85, 1544.87, 1833.79, 2881.4, 2930.99], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('C=O'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(    label = 'galkene',
    E0 = (
        ***u_E0***-173.609,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(72.0575, 'amu')),
        NonlinearRotor(
            inertia = ([67.3251, 128.856, 172.688], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([258.999, 399.463, 423.397, 564.989, 727.708, 829.221, 937.605, 955.801, 980.622, 1037.35, 1061.01, 1076.35, 1210.39, 1306.53, 1366.89, 1410.85, 1420.84, 1454.88, 1480.06, 1502.64, 1511.06, 1719.73, 3012.61, 3029.38, 3071.51, 3084.96, 3122.99, 3136.3, 3215.91, 3829.79], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.91741, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (7554.91, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.868351, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.03857, -3.42747, -2.76472, 0.0923589, 0.0184095],
                    [0.665301, -0.378836, -0.868407, -0.0340856, 0.0234027],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (11.7164, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.1115, -2.39344, -5.82712, 0.189686, 0.245336],
                    [1.53982, -2.47364, 1.95825, -0.289002, -0.136428],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('CC(CO)=C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(    label = 'O2',
    E0 = (
        -7.71678,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(31.9898, 'amu')),
        LinearRotor(inertia=(11.6246, 'amu*angstrom^2'), symmetry=2),
        HarmonicOscillator(frequencies=([1647.57], 'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    structure = SMILES('[O][O]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'bR',
    E0 = (
        ***u_E0***-108.517,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(73.0653, 'amu')),
        NonlinearRotor(
            inertia = ([67.0893, 142.538, 191.909], 'amu*angstrom^2'),
            symmetry = 2,
        ),
        HarmonicOscillator(
            frequencies = ([244.65, 305.025, 356.285, 499.667, 773.713, 916.485, 944.786, 976.91, 1002.86, 1046.2, 1061.2, 1196.88, 1268.81, 1300.7, 1379.96, 1399.82, 1408.96, 1428.77, 1476.39, 1479.12, 1493.18, 1497.11, 1501.67, 2942.36, 2947.41, 2966.23, 2993.85, 3039.22, 3045.62, 3086.58, 3117.29, 3822.04], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.99771, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0277199, -0.0138505, -1.82009, 0.00228582, -0.0115751],
                    [-0.0095106, -0.018063, -0.445046, -0.00105189, -0.0447398],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.95822, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0803595, 0.00183255, -2.15562, -0.00715282, 0.0713131],
                    [0.039083, -0.0097523, 0.294075, -0.0171181, 0.0059814],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.868663, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.47017, 0.70727, -3.58159, -0.673529, -0.129221],
                    [-2.69971, 1.05373, -0.432139, -1.22649, -0.878116],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (11.1443, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.525228, -4.15138, -0.443625, -0.499894, -0.300916],
                    [0.256909, 2.71777, -0.840048, -0.0227292, -0.940714],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('C[C](C)CO'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'bQOOHa',
    E0 = (
        ***u_E0***-225.6,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([169.351, 202.497, 260.845], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([243.603, 287.28, 338.82, 370.758, 407.894, 466.846, 529.584, 609.073, 765.912, 852.814, 913.652, 929.701, 939.869, 1019.66, 1161.35, 1190.82, 1221.48, 1257.49, 1338.38, 1360.65, 1396.89, 1415.15, 1464.92, 1484.05, 1492.44, 1503.18, 1515.17, 3041.71, 3056.83, 3111.09, 3126.33, 3128.27, 3135.65, 3195.87, 3726.72, 3787.9], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.98657, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (13671.7, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.09762, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.077298, 0.0003382, -4.95101, -0.0187656, -0.0455518],
                    [-0.0555115, 0.0234939, 0.159027, 0.0407615, -0.0395179],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.723235, 'amu*angstrom^2'),
            symmetry = 1,
            barrier = (9344.73, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (13.4755, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.65354, -1.56412, -10.2424, -0.188434, 0.853283],
                    [-2.99288, 2.18514, -1.11584, 1.60808, 0.740851],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (11.6222, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.99636, 0.731206, -5.06973, -2.09624, 0.178627],
                    [7.83999, -3.14281, -0.709427, 0.0580659, -0.018779],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.790405, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-13.0043, -6.60548, -1.82604, -1.82735, 0.261446],
                    [0.182947, -7.89607, 2.91758, 1.45179, 0.761463],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('O[CH]C(C)(C)OO'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'bRO2',
    E0 = (
        ***u_E0***-269.94,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([168.769, 201.076, 255.55], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([256.936, 288.211, 344.004, 372.212, 424.917, 467.49, 577.103, 740.049, 808.541, 896.244, 952.325, 1000.84, 1033.4, 1100.24, 1151.57, 1202.12, 1240.06, 1259.83, 1277.31, 1392.87, 1411.12, 1425.64, 1454.21, 1484.57, 1489.71, 1500.82, 1504.53, 1515.33, 2998.17, 3052.36, 3058.72, 3083.62, 3121.76, 3122.54, 3130.07, 3154.58, 3779.33], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.08961, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.00491272, 0.0265938, -4.98415, -0.0153549, 0.00957685],
                    [-0.0885265, 0.0303172, -0.301758, 0.0120231, -0.061546],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.98414, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0902357, 0.00709386, -5.63717, 0.0297672, -0.0716926],
                    [0.076326, -0.0213939, -0.276065, -0.0224759, 0.0828152],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (10.3968, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-3.70731, -0.897353, -3.02196, 0.268893, -0.13111],
                    [2.01637, 1.47892, -1.26006, -0.254825, -0.141616],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (14.3834, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.27839, -5.56629, -8.26962, -1.41399, -0.521348],
                    [4.00647, 1.95429, -4.77757, 1.01217, 0.254016],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.835301, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-12.3824, -6.50983, -3.29057, 0.135972, -0.0782792],
                    [-1.04999, -0.721571, 0.680778, 0.139565, -0.128374],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('OCC(C)(C)O[O]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'disub_epoxy',
    E0 = (
        ***u_E0***-305.706,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(88.0524, 'amu')),
        NonlinearRotor(
            inertia = ([92.4008, 155.608, 206.358], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([265.488, 359.069, 371.685, 401.531, 548.775, 702.926, 816.291, 892.736, 929.439, 999.327, 1015.63, 1089.1, 1124.71, 1135.75, 1170.93, 1236.61, 1262.25, 1364.58, 1409.26, 1429.83, 1445.89, 1491.13, 1502.32, 1513.5, 1530.57, 2976.78, 3040.54, 3077.99, 3098.77, 3104.5, 3127.14, 3198.36, 3780.52], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.06497, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (8902.84, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.836691, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-10.4168, -8.48195, -3.7212, -0.461196, 0.175728],
                    [4.43787, 1.87685, -0.3623, -1.27727, -0.357081],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (13.2533, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.79637, -4.71997, -6.80588, 0.812952, -0.486837],
                    [-0.541062, 3.31334, -1.16746, -0.633597, -0.95802],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 2,
    structure = SMILES('CC1(CO)OC1'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'HO2',
    E0 = (4.09903, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(32.9977, 'amu')),
        NonlinearRotor(
            inertia = ([0.811985, 14.9938, 15.8058], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(frequencies=([1168.22, 1433.56, 3624.29], 'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('O[O]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(
    label = "bath_gas",
    #structure = SMILES("N#N"),
    E0 = (0,'kJ/mol'),
    molecularWeight = (28.0062,"g/mol"),
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,"angstrom"), epsilon=(318.27557,'cm^-1')),
    energyTransferModel = None,
)

thermo('OH', 'NASA')
thermo('bQOOH[O]', 'NASA')
thermo('acetone', 'NASA')
thermo('H2O', 'NASA')
thermo('balkoxyketone', 'NASA')
thermo('ibutenol', 'NASA')
thermo('trisub_epoxy', 'NASA')
thermo('bQOOHg', 'NASA')
thermo('CH2O', 'NASA')
thermo('galkene', 'NASA')
thermo('O2', 'NASA')
thermo('bR', 'NASA')
thermo('bQOOHa', 'NASA')
thermo('bRO2', 'NASA')
thermo('disub_epoxy', 'NASA')
thermo('HO2', 'NASA')

transitionState(label = 'b-gQOOHIsom',
    E0 = (
        ***u_E0***-123.035,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([165.283, 191.747, 254.272], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([192.832, 253.469, 309.007, 359.831, 393.696, 429.583, 567.771, 582.423, 636.422, 796.767, 831.779, 888.663, 919.137, 970.38, 1004.54, 1020.29, 1092.14, 1124.63, 1141.73, 1217.18, 1251.89, 1265.65, 1385.86, 1413.32, 1447.1, 1460.69, 1488.93, 1501.87, 1506.51, 1702.56, 3004.34, 3049.5, 3079.07, 3111.61, 3115.95, 3132.44, 3213.74, 3784.11], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.10544, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (9095.23, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.828521, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-11.7053, -6.81485, -3.8111, -0.249899, 0.00701994],
                    [-2.48888, -0.429757, 0.399988, 0.673832, 0.283432],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (15.0363, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-7.8984, -6.06987, -8.90402, -0.203178, -0.105119],
                    [1.98264, 0.249766, -3.49305, 1.19931, 0.0897335],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-2213.97,
        'cm^-1',
    ),)
reaction(
    label = 'b-gQOOHIsom',
    reactants = ['bRO2'],
    products = ['bQOOHg'],
    transitionState = 'b-gQOOHIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'bH2OForm',
    E0 = (
        ***u_E0***-163.156,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([157.126, 218.059, 263.782], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([103.279, 162.846, 242.924, 312.015, 343.561, 366.861, 410.215, 431.53, 442.251, 579.448, 624.23, 780.102, 852.655, 897.568, 931.099, 936.868, 1013.1, 1068.67, 1121.03, 1194, 1234.06, 1281.6, 1349, 1389.83, 1412.42, 1480.25, 1491.13, 1497.72, 1513.51, 1549.64, 2674.72, 3042.92, 3049.02, 3109.16, 3121.22, 3129.67, 3136.19, 3188.14, 3819.31], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.09241, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (8762.04, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.965, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (12609.8, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    frequency = (
        ***u_negfreq****-1174.9,
        'cm^-1',
    ),)
reaction(
    label = 'bH2OForm',
    reactants = ['bQOOHa'],
    products = ['balkoxyketone', 'H2O'],
    transitionState = 'bH2OForm',
    tunneling = 'Eckart',
)

transitionState(label = 'bEpoxyFroma',
    E0 = (
        ***u_E0***-196.268,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([140.545, 269.656, 290.593], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([137.998, 179.166, 253.031, 257.067, 352.145, 379.141, 430.565, 452.972, 570.926, 644.959, 755.189, 874.967, 934.31, 973.908, 1006.33, 1025.88, 1161.98, 1187.8, 1227.18, 1301.28, 1365.15, 1401.02, 1413.82, 1467.73, 1478.02, 1503.77, 1510.57, 1525.9, 3032.47, 3047.16, 3097.5, 3113.5, 3136.61, 3142.52, 3238.26, 3781.59, 3819.9], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.11068, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0421401, -0.0027227, -6.73973, -0.0170611, 0.0214864],
                    [-0.0355447, 0.107055, -0.739127, 0.142041, -0.0189997],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.06309, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0119384, -0.054722, -5.71795, 0.0292685, 0.029607],
                    [-0.0911062, -0.150523, 0.707508, -0.170204, -0.127426],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.751512, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.65027, -0.795114, 0.147525, -0.00183192, 0.00446615],
                    [9.3895, -5.05978, 0.0221832, 0.0397464, -0.0301909],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.857597, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.21032, -15.1501, 0.777056, 1.25337, 0.0135381],
                    [6.17008, -2.1771, -0.171309, -0.0713779, -0.137667],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-531.489,
        'cm^-1',
    ),)
reaction(
    label = 'bEpoxyFroma',
    reactants = ['bQOOHa'],
    products = ['trisub_epoxy', 'OH'],
    transitionState = 'bEpoxyFroma',
    tunneling = 'Eckart',
)

transitionState(label = 'bEpoxyFromg',
    E0 = (
        ***u_E0***-158.312,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([176.308, 202.831, 254.228], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([136.265, 220.81, 281.324, 328.843, 372.097, 392.186, 464.359, 479.212, 582.99, 763.323, 773.109, 876.794, 895.029, 969.462, 1004.25, 1050.78, 1097.55, 1120.29, 1240.13, 1246.37, 1317.53, 1398.79, 1414.04, 1451.31, 1458.92, 1489.58, 1503.99, 1504.91, 3024.72, 3045.72, 3089.99, 3113.47, 3127.78, 3169.34, 3293.46, 3757.32, 3814.8], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.0381, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0588838, -0.0395145, -5.29783, 0.0588058, 0.0373694],
                    [-0.0217041, -0.0360414, 0.347399, -0.0353245, -0.0165661],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.556245, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.12963, -9.11258, 1.14458, 2.51594, 0.146228, -1.43724, -0.518683],
                    [-17.165, 7.64721, 2.53515, -0.445672, -1.72902, -0.274512, 1.09255],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.828699, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-18.1005, -8.36519, -3.13031, 0.506109, 0.0737317],
                    [-1.84484, 0.0602456, 0.968601, 0.10591, 0.31864],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (14.8945, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.57394, -3.86771, -6.25109, -1.80878, -2.35105],
                    [1.34446, 1.58822, -2.65506, -3.43745, 0.0207244],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-660.701,
        'cm^-1',
    ),)
reaction(
    label = 'bEpoxyFromg',
    reactants = ['bQOOHg'],
    products = ['disub_epoxy', 'OH'],
    transitionState = 'bEpoxyFromg',
    tunneling = 'Eckart',
)

transitionState(label = 'bHO2elimFromg',
    E0 = (
        ***u_E0***-134.781,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([169.136, 233.546, 282.793], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([210.17, 240.441, 289.018, 332.204, 385.447, 427.204, 508.619, 554.996, 782.365, 789.658, 914.212, 946.812, 972.404, 1036.57, 1057.8, 1099.22, 1227.69, 1304.52, 1336.7, 1383.32, 1399.68, 1430.65, 1448, 1479.93, 1499.08, 1501.59, 1521.78, 2997.7, 3047.64, 3068.51, 3118.6, 3146.97, 3154.89, 3243.02, 3753.19, 3776.49], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.90069, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0378184, -0.00851658, -2.6827, -0.000521895, 0.0611496],
                    [0.0249153, -0.0209006, -0.299209, -0.0216885, 0.0335871],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.667741, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.76499, -17.6168, 0.0261137, 2.06357, 0.203322],
                    [3.5045, -0.742615, -0.28805, -0.56724, -0.0186067],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (8.18314, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.70409, -3.68749, -0.928643, -1.15067, 0.736934],
                    [0.260906, -4.85864, 3.98633, -1.82585, 1.51088],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (15.7502, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.34843, -4.73033, -4.87952, -3.88977, -0.818273],
                    [1.01306, -0.568525, -0.0791337, -0.562666, 2.18315],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.748679, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-11.9793, -6.31519, -3.0201, 0.177089, -0.162071],
                    [-0.315705, 0.0544381, -0.376653, -0.081196, 0.171161],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-448.12,
        'cm^-1',
    ),)
reaction(
    label = 'bHO2elimFromg',
    reactants = ['bQOOHg'],
    products = ['galkene', 'HO2'],
    transitionState = 'bHO2elimFromg',
    tunneling = 'Eckart',
)

transitionState(label = 'b-gHO2elimFromRO2',
    E0 = (
        ***u_E0***-146.517,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([167.379, 243.567, 295.145], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([134.354, 174.224, 205.997, 289.48, 367.945, 407.426, 525.396, 550.798, 639.199, 665.941, 820.027, 909.631, 991.947, 1021.33, 1048.29, 1061.16, 1101.19, 1217.17, 1292.56, 1315.35, 1332.49, 1369.16, 1408.22, 1418.96, 1445.45, 1476.02, 1490.78, 1494.01, 1568.47, 1598.09, 3004.62, 3019.52, 3041.24, 3096.97, 3102.43, 3149.86, 3177.98, 3820.74], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.91966, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0437048, -0.0232711, -3.41655, 0.0439939, -0.050932],
                    [-0.0742708, -0.0323557, 0.130579, 0.00587094, -0.0905097],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.781693, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-7.55711, -5.27641, -3.15174, 0.0646137, -0.0175174],
                    [1.72054, 0.567813, -0.472169, -0.0977705, 0.0568823],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (15.2008, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-3.90548, -6.44388, -5.68013, -0.508362, -0.58997],
                    [-1.81362, -2.35777, 1.19479, -0.813348, -0.357335],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-1047.21,
        'cm^-1',
    ),)
reaction(
    label = 'b-gHO2elimFromRO2',
    reactants = ['bRO2'],
    products = ['galkene', 'HO2'],
    transitionState = 'b-gHO2elimFromRO2',
    tunneling = 'Eckart',
)

transitionState(label = 'b-aHO2elimFromRO2',
    E0 = (
        ***u_E0***-137.263,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([195.885, 219.174, 298.016], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([128.468, 157.677, 193.545, 243.831, 278.605, 364.454, 412.826, 546.793, 570.615, 665.487, 824.239, 938.538, 973.006, 1010.81, 1028.33, 1096.29, 1128.17, 1234.87, 1285.74, 1313.11, 1321.31, 1368, 1413.21, 1420.99, 1471.4, 1477.25, 1481.42, 1499.96, 1582.33, 1620.58, 3013.69, 3018.44, 3059.94, 3086.45, 3094.41, 3123.24, 3154.96, 3848.32], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.00144, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.042821, -0.059253, -4.81247, 0.0552908, -0.0226417],
                    [-0.0846771, -0.00363338, -0.369989, -0.00426732, -0.0823752],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.93159, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0271212, -0.00997313, -3.22652, 0.0159603, -0.0769291],
                    [-0.117325, -0.0477679, 0.34004, -0.0208908, -0.0696184],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.712865, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.95482, -2.07405, -1.03019, -0.0523984, 0.0350098],
                    [-0.561935, -1.74245, 0.930279, 0.237081, 0.0382062],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-1048.12,
        'cm^-1',
    ),)
reaction(
    label = 'b-aHO2elimFromRO2',
    reactants = ['bRO2'],
    products = ['ibutenol', 'HO2'],
    transitionState = 'b-aHO2elimFromRO2',
    tunneling = 'Eckart',
)

transitionState(label = 'bHO2elimFroma',
    E0 = (
        ***u_E0***-171.73,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([182.717, 211.195, 277.522], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([190.235, 229.08, 268.225, 309.114, 339.629, 380.096, 441.935, 578.961, 747.803, 796.896, 919.918, 976.34, 1016.23, 1031.43, 1085.91, 1197.21, 1233.24, 1334.68, 1355.05, 1386.56, 1416.87, 1427.56, 1476.63, 1486.54, 1497.37, 1511.7, 1571.72, 3034.66, 3037.95, 3095.84, 3098.55, 3122.09, 3131.22, 3209.94, 3756.93, 3780.86], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.03775, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0175119, -0.0511513, -3.51385, 0.0283088, -0.0349351],
                    [0.0174923, 0.0214893, -0.813495, 0.0487755, -0.000499333],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.90187, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0843555, -0.0504556, -3.49375, 0.0625243, 0.0515287],
                    [0.0462145, 0.0385806, 1.82913, -0.0272343, -0.0348847],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.796128, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-8.58147, -8.56323, 0.362519, 0.151333, 0.0975612],
                    [0.14422, -5.66756, 1.878, 1.06444, 0.0476272],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (13.5787, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.14764, -3.9621, -4.25984, -0.22443, -0.356296],
                    [0.09623, 0.206809, 0.369538, -0.241018, -0.243934],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.805091, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.5823, -15.7665, 4.62762, 0.37776, -1.19375],
                    [-8.42756, 7.33214, -1.90013, -1.82952, 1.23197],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-406.689,
        'cm^-1',
    ),)
reaction(
    label = 'bHO2elimFroma',
    reactants = ['bQOOHa'],
    products = ['ibutenol', 'HO2'],
    transitionState = 'bHO2elimFroma',
    tunneling = 'Eckart',
)

transitionState(label = 'b-aQOOHIsom',
    E0 = (
        ***u_E0***-151.292,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([172.449, 190.681, 253.477], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([153.336, 255.94, 260.22, 350.156, 376.488, 391.018, 558.52, 621.423, 636.464, 802.664, 841.415, 919.012, 926.155, 949.78, 992.756, 1021.46, 1165.26, 1176.9, 1209.15, 1227.52, 1262.31, 1333.77, 1406.2, 1422.17, 1444.65, 1481.01, 1491.46, 1501.93, 1515.78, 1734.07, 3052.08, 3056.67, 3117.7, 3124.98, 3130.63, 3142.84, 3147.63, 3766.66], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.05353, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0135207, 0.0526798, -5.14734, -0.0361682, 0.0421472],
                    [-0.0776046, 0.0595894, -0.223209, 0.0521162, -0.0419405],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.04333, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0443055, -0.0285879, -4.53707, 0.0473516, 0.0721634],
                    [-0.010315, -0.0378255, -0.174864, -0.0227203, -0.00482543],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.852193, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.04733, -12.1339, -2.50383, -0.162374, -0.158378],
                    [-4.59199, 5.36624, -0.995782, -1.06595, 0.0989847],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-1925.02,
        'cm^-1',
    ),)
reaction(
    label = 'b-aQOOHIsom',
    reactants = ['bRO2'],
    products = ['bQOOHa'],
    transitionState = 'b-aQOOHIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'bAlkoxyIsom',
    E0 = (
        ***u_E0***-181.685,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([151.244, 205.284, 241.179], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([175.102, 263.042, 286.811, 337.417, 392.506, 448.111, 511.507, 546.829, 634.419, 662.083, 810.421, 890.015, 944.997, 956.368, 974.604, 1028.45, 1077.55, 1144.67, 1199.3, 1219.8, 1249.95, 1267.14, 1321.54, 1407.21, 1424.91, 1483.2, 1490.27, 1501.07, 1506.36, 1513.64, 1841.28, 2942.74, 3003.68, 3056.05, 3061.2, 3123.08, 3128.39, 3134.82, 3166.59], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.98011, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0245998, -0.0371085, -4.64642, 0.0323301, 0.0407674],
                    [-0.0338652, -0.0381603, 0.573764, -0.0091743, -0.0414247],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.08136, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0238691, 0.0469741, -4.56907, -0.0173076, -0.0145202],
                    [-0.0293178, -0.000689333, 0.585327, 0.0270949, -0.0601279],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    frequency = (
        ***u_negfreq****-871.872,
        'cm^-1',
    ),)
reaction(
    label = 'bAlkoxyIsom',
    reactants = ['bRO2'],
    products = ['bQOOH[O]'],
    transitionState = 'bAlkoxyIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'bDoublebscission',
    E0 = (
        ***u_E0***-149.026,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([155.142, 266.978, 303.19], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([101.256, 113.705, 195.251, 228.632, 292.058, 343.548, 392.48, 406.12, 536.975, 657.117, 791.758, 905.032, 961.876, 988.352, 1004.51, 1067.09, 1149.42, 1242.88, 1262.9, 1278.26, 1399.81, 1411.71, 1425.3, 1464.38, 1473.3, 1483.99, 1495.77, 1504.33, 1611.25, 2880.41, 2932.67, 3016.13, 3026.55, 3102.47, 3117.29, 3139.81, 3161.18, 3800.54], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.650311, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.21406, 1.53393, -0.00986486, -0.194877, 0.0426039],
                    [4.66316, -3.04569, 0.496842, -0.0263217, -0.0587914],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.028, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.068066, 0.00952888, -6.42025, -0.00289383, 0.0555224],
                    [0.0130936, 0.0679669, -0.354353, 0.0724857, -0.0102929],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.0763, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0121595, -0.0496919, -6.73429, 0.0567136, 0.0153449],
                    [-0.0285372, 0.00726931, 0.658682, 0.0161726, 0.00932828],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    frequency = (
        ***u_negfreq****-216.652,
        'cm^-1',
    ),)
reaction(
    label = 'bDoublebscission',
    reactants = ['bQOOH[O]'],
    products = ['acetone', 'CH2O', 'OH'],
    transitionState = 'bDoublebscission',
    tunneling = 'Eckart',
)

transitionState(
    label = 'bRO2Form',
    spinMultiplicity = 2,
    opticalIsomers = 2,
)
reaction(
    label = 'bRO2Form',
    reactants = ['bR', 'O2'],
    products = ['bRO2'],
    transitionState = 'bRO2Form',
    kinetics = Arrhenius(A=(***u_ilt****1.6200000000000002e-12,'cm^3/(molecule*s)'), n=0.325, Ea=(-210.0,'K'), T0=(1,"K")),
)

network(
    label = 'C4H9O3',
    isomers = ['bRO2', 'bQOOHg', 'bQOOHa', 'bQOOH[O]'],
    reactants = [['bR', 'O2']],
    bathGas = {'bath_gas': 1.0}
)
pressureDependence(
    'C4H9O3',
    Tmin=(180.0,'K'), Tmax=(1500.0,'K'), Tcount=20,
    Pmin=(0.01,'bar'), Pmax=(100.0,'bar'), Pcount=20,
    maximumGrainSize = (0.5,'kcal/mol'),
    minimumGrainCount = 200,
    method = '***u_method***',
    #method = 'reservoir state',
    #method = 'modified strong collision',
    interpolationModel = ('chebyshev', 10, 8),
    activeKRotor = True, 
    activeJRotor = True,
    rmgmode = False,
)

