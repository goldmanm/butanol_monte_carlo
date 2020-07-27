
# coding=utf8

modelChemistry = 'CCSD(T)-F12/cc-pVTZ-F12//B3LYP/CBSB7'
useHinderedRotors = True
useBondCorrections = False

species(label = 'propene3ol',
    E0 = (
        ***u_E0***-135.363,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(58.0419, 'amu')),
        NonlinearRotor(
            inertia = ([29.8977, 85.5332, 110.802], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([287.84, 574.197, 618.888, 889.926, 953.173, 997.129, 1018.38, 1043.7, 1134.23, 1216.8, 1321.52, 1384.17, 1417.99, 1447.37, 1500.07, 1715.48, 2971.18, 3054.78, 3137.75, 3154.01, 3235.16, 3830.62], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.859618, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.677929, -1.38692, -3.65452, -0.309963, 0.256682],
                    [-1.26216, 2.13948, -0.3067, -0.726765, -0.326581],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (7.30003, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.0471908, -2.22587, -5.26186, -0.626651, 0.0950649],
                    [-1.35757, 3.09268, -1.26467, 0.104805, -0.392701],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('C=CCO'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'OH',
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

species(label = 'disub_c4ether',
    E0 = (
        ***u_E0***-328.806,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(88.0524, 'amu')),
        NonlinearRotor(
            inertia = ([96.3307, 151.65, 218.331], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([114.503, 265.593, 326.69, 445.323, 554.757, 711.166, 857.648, 893.745, 935.537, 963.993, 993.826, 1097.75, 1128.97, 1147.96, 1169.52, 1185.15, 1256.23, 1282.07, 1326.45, 1345.29, 1404.61, 1421.63, 1460.66, 1504.02, 1505.69, 1539.93, 3027.2, 3033.86, 3046.79, 3054.31, 3082.31, 3098.45, 3100.35, 3809.53], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.94616, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11163.3, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.871339, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.09781, -4.2384, -2.60554, 0.0386657, 0.0159963],
                    [-7.59597, 2.16361, 0.881012, -0.0646185, -0.0856098],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 2,
    structure = SMILES('OC1OCC(C)1'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'H2O',
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

species(label = 'gQOOHa',
    E0 = (
        ***u_E0***-207.458,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([156.812, 243.251, 347.039], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([242.716, 300.076, 350.621, 431.175, 465.662, 549.744, 631.593, 836.573, 861.399, 938.517, 952.222, 1000.55, 1084.72, 1113.41, 1173.21, 1215.19, 1279.96, 1297.24, 1334.24, 1371.2, 1375.59, 1406.78, 1416.37, 1461.66, 1476.24, 1500.64, 1513.13, 2945.27, 3032.62, 3039.67, 3090.21, 3102.13, 3109.79, 3176.1, 3720.73, 3785.88], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.350716, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.04326, -4.49204, 1.17238, 0.074067, -0.19232],
                    [-8.57006, 4.77135, -0.365759, 0.128258, -0.116887],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (12.0284, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.27802, -6.45794, -7.2721, 1.84206, -2.35942],
                    [-13.1939, -0.850627, 4.74263, -0.948484, -0.203161],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (29.7351, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-8.453, -1.48401, -10.1193, 0.949773, -2.86578],
                    [5.24228, -6.28322, 3.37936, -1.65191, -1.44937],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (13.6608, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-10.1553, -4.25983, -2.09241, 0.0248208, -0.135452],
                    [-1.45003, -2.29927, 1.84578, 1.91358, -0.81851],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.648396, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-14.5856, -5.09088, -0.538103, -1.92589, 0.949759],
                    [2.37949, 6.95786, -4.58524, -1.37682, 0.538234],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.06923, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11125.6, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('OOCC([CH]O)C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'propene1ol',
    E0 = (
        ***u_E0***-159.36,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(58.0419, 'amu')),
        NonlinearRotor(
            inertia = ([12.3112, 129.08, 138.269], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([296.895, 302.677, 543.135, 805.493, 935.549, 963.657, 1067.76, 1112.93, 1140.89, 1268.76, 1341.26, 1401.17, 1429.92, 1486.14, 1506.93, 1742.48, 3020.08, 3059.97, 3096.35, 3123.74, 3187.48, 3824.82], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.814398, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.22099, -8.14349, -1.75583, 0.267156, -0.00843202],
                    [-0.00167476, -0.0165493, -0.0023873, 0.00546691, 0.000959118],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.31671, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (8393.44, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('CC=CO'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'gQOOHb',
    E0 = (
        ***u_E0***-196.637,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([162.637, 216.903, 319.365], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([182.316, 279.898, 363.567, 427.38, 472.379, 594.61, 779.124, 850.544, 911.8, 945.237, 957.135, 991.071, 1002.47, 1010.42, 1150.06, 1245.39, 1300.67, 1332.92, 1344.4, 1370.48, 1401.92, 1408.68, 1468.09, 1479.08, 1494.06, 1495.08, 1507.25, 2974.8, 3035.18, 3039.57, 3043.66, 3091.61, 3094.87, 3115.49, 3571.28, 3830.98], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.677505, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-15.4145, -8.38045, -1.8679, -2.92657, 0.690579],
                    [-2.33145, 1.50711, -1.40772, 0.591676, 1.47174],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (15.1382, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.787334, -6.90199, -7.53575, -3.71364, -2.29051],
                    [6.21021, 3.93559, -4.82025, 0.919234, 0.0343537],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (34.3852, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-8.1883, -7.20132, -4.46927, -2.06105, -0.538853],
                    [-0.93476, -3.53912, 0.786005, 0.0175033, 0.463828],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (17.7617, 'amu*angstrom^2'),
            symmetry = 1,
            barrier = (29497.9, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.853992, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.77231, -10.7374, -0.797403, 1.02012, -0.0795389],
                    [20.0543, -7.93759, -2.10949, 0.402721, 0.423262],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.92551, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.232107, -0.341834, -0.414732, 0.0638207, -0.0233353],
                    [-0.168067, -0.116024, 0.83498, -0.144311, -0.346018],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('OC[C](COO)C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'ipropylOOH',
    E0 = (
        ***u_E0***-0.98977,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(75.0446, 'amu')),
        NonlinearRotor(
            inertia = ([56.4336, 155.568, 173.096], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([243.415, 394.481, 419.021, 600.751, 848.484, 882.492, 941.467, 952.919, 998.465, 1138.23, 1154.02, 1280.14, 1357.76, 1377.9, 1386.76, 1415.17, 1461.57, 1480.43, 1490.46, 2984.53, 2994.25, 3046.65, 3058.09, 3095.64, 3186.6, 3792.42], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.38664, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.30216, -4.338, 1.21162, 0.0757063, -0.0374393],
                    [7.45972, -3.97788, -0.639817, 0.287322, -0.0680831],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (10.8566, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [1.93472, -2.10282, -6.47214, -0.0218246, -0.329084],
                    [3.19067, 2.493, -2.4371, -0.366382, 0.19092],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (11.8923, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [0.248933, -2.5914, -0.847449, 0.378428, -0.310006],
                    [0.12525, 1.1943, -0.435991, 0.0557241, 0.157857],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.58297, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.00932785, -0.00574481, -0.368152, -0.0266807, 0.00123826],
                    [0.00456983, -0.00157491, -0.049402, -0.00386721, 0.00699093],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('C[CH]COO'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'galdoxy',
    E0 = (
        ***u_E0***-151.619,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(87.0446, 'amu')),
        NonlinearRotor(
            inertia = ([90.8605, 193.059, 259.439], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([205.959, 289.055, 367.578, 462.614, 642.735, 715.33, 811.37, 926.419, 934.057, 1017.29, 1060.19, 1083.3, 1156.03, 1198.53, 1292.2, 1329.6, 1354.27, 1361.57, 1408.38, 1421.72, 1501, 1513.22, 1808.08, 2876.27, 2885.07, 2959.02, 3015.12, 3044.41, 3108.01, 3134.98], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (8.55445, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.05552, -0.269922, -1.85425, 0.339135, 0.0486026],
                    [0.257198, 0.704793, 0.880306, -0.472848, -0.0235605],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (7.2133, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.65357, -0.955743, -5.31671, -0.0925347, 1.6303],
                    [-3.50166, -2.18565, 3.66362, 0.437788, 0.781761],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.98582, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.017252, 0.0822449, -5.85534, -0.0668887, -0.00509765],
                    [-0.0408958, 0.0506072, -0.199208, 0.0491962, -0.0195864],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('O=CC(C)C[O]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'galkene',
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

species(label = 'CH2O',
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

species(label = 'O2',
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

species(label = 'gRO2',
    E0 = (
        ***u_E0***-235.915,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([149.785, 269.607, 396.749], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([190.278, 285.715, 347.525, 390.747, 495.281, 514.928, 853.866, 900.283, 931.374, 962.518, 963.791, 1069.77, 1102.01, 1145.75, 1178.71, 1195.35, 1220.12, 1283.25, 1318.24, 1354.42, 1403.2, 1410.11, 1420.61, 1453.56, 1495.5, 1507.04, 1508.91, 1519.61, 2963.73, 3036.88, 3046.63, 3058.32, 3085.78, 3097.8, 3114.3, 3118.87, 3826.5], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.714502, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.67006, -1.18581, -3.44911, -0.05543, -0.0260402],
                    [4.05365, -0.645316, -0.415798, -0.176382, 0.0320295],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (16.179, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.28423, -2.79764, -8.05122, -0.825827, -0.424091],
                    [4.34997, 4.23548, -5.84407, 0.521959, 0.257811],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (16.3597, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-3.4363, -0.0572375, -8.2527, 1.12112, -0.493833],
                    [1.5606, -0.776094, 0.173303, -0.298663, -0.683431],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (1.5737, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.29032, 3.23437, -2.28802, -0.702321, 0.415024],
                    [-0.523251, 1.36325, -0.502517, -0.202589, -0.0541042],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.03125, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11289.3, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('[O]OCC(CO)C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'gQOOHg',
    E0 = (
        ***u_E0***-174.757,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([145.666, 274.518, 394.797], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([191.119, 279.588, 349.57, 381.466, 473.211, 500.816, 543.486, 846.803, 920.273, 922.203, 933.889, 1022.89, 1069.11, 1079.74, 1122.67, 1155.27, 1225.83, 1281.08, 1286.51, 1347.98, 1374.31, 1383.91, 1415.33, 1452.48, 1471.88, 1511.44, 1528.21, 2976.72, 3020.92, 3029.85, 3068.74, 3094.47, 3147.96, 3252.66, 3779.88, 3790.42], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.669726, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-12.3545, -1.5867, -2.98149, -0.272675, -0.0864402],
                    [4.47842, 0.0769908, -1.30771, -0.207776, -0.187848],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (16.4482, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.55284, -5.61271, -9.69431, -1.16462, -0.399533],
                    [4.7126, 3.86299, -4.9741, -0.41118, 0.319095],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (17.7283, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-7.60316, -0.191419, -8.48308, -0.215277, -0.221965],
                    [2.35255, -0.171663, -0.00579945, -0.357465, -0.156058],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.4347, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.5325, 6.70878, -6.53859, -0.381865, 0.127617],
                    [1.87689, -4.31211, 3.11111, -0.621762, -0.778231],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.704679, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.24484, -4.90415, 1.38628, 0.0169414, -0.0653227],
                    [8.364, -4.19928, -0.369804, 0.25407, -0.0322822],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (1.65658, 'amu*angstrom^2'),
            symmetry = 2,
            barrier = (1473.07, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('OOCC(CO)[CH2]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'gR',
    E0 = (
        ***u_E0***-91.0907,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(73.0653, 'amu')),
        NonlinearRotor(
            inertia = ([78.3545, 124.613, 155.677], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([263.538, 367.572, 384.437, 503.416, 648.536, 795.208, 916.577, 942.629, 960.011, 999.983, 1072.62, 1150.86, 1175.44, 1216.52, 1290.58, 1340.05, 1388.33, 1412.92, 1426.71, 1467.47, 1500.48, 1510.17, 1518.97, 2924.12, 2987.29, 3043.05, 3086.66, 3105.09, 3117.01, 3137.44, 3241.06, 3811.21], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.865605, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.87115, -1.61435, -3.06777, 0.0346463, 0.0105385],
                    [-0.272639, 0.634257, -0.508002, -0.290055, 0.0143021],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (13.2694, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.206129, -0.971538, -9.64725, -0.0757256, -0.0443262],
                    [0.561218, 0.642343, -0.0396354, -0.071916, -0.515025],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (1.77284, 'amu*angstrom^2'),
            symmetry = 2,
            fourier = (
                [
                    [-0.265827, -2.38516, 0.0606766, -0.301579, 0.121422],
                    [0.31586, -1.3158, 0.0832413, 0.427185, 0.190482],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.82488, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11943.1, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('OCC([CH2])C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'galdol',
    E0 = (
        ***u_E0***-384.323,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(88.0524, 'amu')),
        NonlinearRotor(
            inertia = ([120.202, 149.535, 246.653], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([237.564, 307.334, 349.495, 469.993, 630.119, 818.861, 917.366, 936.368, 937.425, 1063.04, 1085.84, 1135.27, 1170.97, 1231.58, 1287.02, 1360.16, 1392.19, 1412.29, 1427.45, 1448.5, 1505.45, 1506.73, 1513.64, 1798.64, 2883.03, 2988.95, 3004.06, 3040.93, 3085.2, 3102.95, 3114.26, 3800.78], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (9.31918, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.37683, -3.21964, -1.51756, 0.551702, -0.116305],
                    [-1.09337, -1.98211, 0.962545, 0.250851, 0.154339],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (13.5808, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.14014, -8.53014, -10.5132, 0.507114, 0.854736],
                    [7.95784, 1.32128, -4.11146, -1.33982, 0.1046],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.834228, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.00957, -4.66081, -3.24431, 0.678134, 0.302611],
                    [-2.48498, -0.328717, 2.38662, 0.156994, -0.754104],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.99194, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (10047.4, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 2,
    structure = SMILES('O=CC(C)CO'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'monosub_c4ether',
    E0 = (
        ***u_E0***-272.041,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(88.0524, 'amu')),
        NonlinearRotor(
            inertia = ([76.8816, 192.128, 194.87], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([97.9589, 269.765, 328.527, 586.797, 718.748, 867.672, 883.991, 901.242, 973.533, 1012.16, 1035.11, 1073.84, 1118.45, 1135.36, 1166.35, 1179.35, 1215.47, 1287.34, 1323.87, 1349.62, 1376.46, 1408.63, 1429.11, 1507.35, 1519.43, 1548.38, 2987.24, 2992.2, 3039.82, 3049.84, 3073.4, 3083.81, 3095.15, 3842.55], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.859264, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.19586, -0.524346, 0.677952, -0.131574, 0.0107012],
                    [0.765638, 0.434028, -1.11081, 0.613472, 0.167704],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (14.2585, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.0678731, -0.947244, -6.90903, -0.0485773, 0.106653],
                    [-0.128127, -0.995023, -5.13364, -0.341121, 0.123951],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('OCC1COC1'),
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

species(label = 'gQOOH[O]',
    E0 = (
        ***u_E0***-155.218,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([142.14, 235.777, 338.15], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([200.668, 320.498, 344.256, 398.572, 445.407, 549.599, 755.803, 837.998, 882.851, 913.869, 949.852, 1010.29, 1057.66, 1075.18, 1116.87, 1162.31, 1232.68, 1294.6, 1310.56, 1320.79, 1352.43, 1399.84, 1418.21, 1461.3, 1463.78, 1501.58, 1505.34, 1529.5, 2958.14, 3017.57, 3028.19, 3041.03, 3064.17, 3081.96, 3104.24, 3117.39, 3592.28], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.787812, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-13.114, -6.1563, 1.19167, -2.23699, -1.01123],
                    [-5.36355, 3.2426, -0.636814, -0.883978, 1.6034],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (14.8262, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-3.93725, -14.0186, -3.82734, -2.24637, 0.904959],
                    [9.90995, 4.31763, -7.16352, 0.121776, 0.576807],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (32.4493, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.87688, -4.67389, -10.4565, -0.742269, -0.246775],
                    [-2.70645, -2.16049, 0.220496, -0.407057, 0.396469],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (14.7334, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-7.97561, -6.26796, -9.78001, -0.187643, -0.988368],
                    [-1.07783, -2.23001, -5.02108, -0.539311, 0.658892],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.01281, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11719.6, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('OOCC(C[O])C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(
    label = "bath_gas",
    #structure = SMILES("N#N"),
    E0 = (0,'kJ/mol'),
    molecularWeight = (28.0062,"g/mol"),
    collisionModel = TransportData(sigma=(4.63691,"angstrom"), epsilon=(318.27557,'cm^-1')),
    energyTransferModel = None,
)
thermo('propene3ol', 'NASA')
thermo('OH', 'NASA')
thermo('disub_c4ether', 'NASA')
thermo('H2O', 'NASA')
thermo('disub_epoxy', 'NASA')
thermo('gQOOHa', 'NASA')
thermo('propene1ol', 'NASA')
thermo('gQOOHb', 'NASA')
thermo('ipropylOOH', 'NASA')
thermo('galdoxy', 'NASA')
thermo('galkene', 'NASA')
thermo('CH2O', 'NASA')
thermo('O2', 'NASA')
thermo('gRO2', 'NASA')
thermo('gQOOHg', 'NASA')
thermo('gR', 'NASA')
thermo('galdol', 'NASA')
thermo('monosub_c4ether', 'NASA')
thermo('HO2', 'NASA')
thermo('gQOOH[O]', 'NASA')

transitionState(
    label = 'gRO2Form',
    spinMultiplicity = 2,
    opticalIsomers = 2,
)
reaction(
    label = 'gRO2Form',
    reactants = ['gR', 'O2'],
    products = ['gRO2'],
    transitionState = 'gRO2Form',
    kinetics = Arrhenius(A=(***u_ilt****1.14e-07,'cm^3/(molecule*s)'), n=-1.6269999999999998, Ea=(100.0,'K'), T0=(1,"K")),
)

transitionState(label = 'gAlkoxyIsom',
    E0 = (
        ***u_E0***-136.67,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([137.295, 223.476, 330.823], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([134.782, 196.61, 283.214, 299.281, 359.587, 397.937, 457.385, 530.188, 566.163, 839.494, 861.11, 917.942, 945.963, 976.099, 1027.25, 1038.97, 1088.65, 1125.93, 1175.9, 1237.59, 1295.92, 1309.44, 1315.1, 1345.82, 1400.75, 1405.23, 1421.72, 1433.19, 1471.33, 1505.25, 1508.81, 1682.78, 2950.25, 2975.23, 3031.65, 3035.73, 3046.09, 3096.09, 3103.01, 3106.66], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.01167, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.00641, 0.073478, -7.72613, -0.0341369, -0.00988158],
                    [0.00789086, 0.0186855, 0.850244, 0.0165044, -0.0143849],
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
        ***u_negfreq****-1208.47,
        'cm^-1',
    ),)
reaction(
    label = 'gAlkoxyIsom',
    reactants = ['gRO2'],
    products = ['gQOOH[O]'],
    transitionState = 'gAlkoxyIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'g-aQOOHIsom',
    E0 = (
        ***u_E0***-151.868,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([144.452, 222.781, 322.475], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([119.471, 191.881, 259.978, 311.447, 361.373, 431.878, 536.305, 601.832, 671.036, 810.151, 900.879, 921.209, 948.729, 960.952, 1035.52, 1065.32, 1101.06, 1136.91, 1179.37, 1247.44, 1275.39, 1296.9, 1314.41, 1368.61, 1382.2, 1415.85, 1435.51, 1480.87, 1500.59, 1508.08, 1583.19, 3007.55, 3045.61, 3053.81, 3104.56, 3111.88, 3117.85, 3134.51, 3805.3], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.825615, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.09196, -5.79355, -1.63458, 0.00788992, 0.0292394],
                    [5.23672, -4.35301, 0.468976, 0.568274, 0.0251026],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.96335, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (10189.2, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-1715.01,
        'cm^-1',
    ),
)
reaction(
    label = 'g-aQOOHIsom',
    reactants = ['gRO2'],
    products = ['gQOOHa'],
    transitionState = 'g-aQOOHIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'g-gQOOHIsom',
    E0 = (
        ***u_E0***-134.512,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([98.3046, 318.976, 390.224], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([124.976, 211.214, 315.243, 383.199, 432.215, 455.366, 494.916, 558.967, 643.246, 830.32, 909.125, 937.855, 948.257, 984.784, 1039.99, 1058.15, 1079.89, 1092.72, 1116.89, 1152.5, 1220.61, 1277.69, 1334.2, 1349.57, 1368.74, 1397.57, 1411.12, 1466.57, 1483.87, 1512.52, 1587.42, 3017.62, 3030.53, 3042.48, 3089.02, 3094.9, 3140.24, 3187.46, 3840.37], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (12.8744, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.54504, -0.429239, -9.11692, 0.162223, -0.197779],
                    [1.1717, 0.986537, -1.10189, 0.0117356, -0.0274991],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.826212, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.590329, -2.81191, -2.26223, 0.0157796, -0.00727887],
                    [3.50681, 0.637834, -1.68056, 0.0779531, -0.0158865],
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
        ***u_negfreq****-1631.04,
        'cm^-1',
    ),
)

reaction(
    label = 'g-gQOOHIsom',
    reactants = ['gRO2'],
    products = ['gQOOHg'],
    transitionState = 'g-gQOOHIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'g-bQOOHIsom',
    E0 = (
        ***u_E0***-112.764,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([174.98, 202.266, 299.406], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([146.217, 230.066, 262.319, 325.577, 353.961, 488.743, 546.986, 662.366, 828.778, 886.051, 908.985, 952.625, 959.359, 999.245, 1085.17, 1104.12, 1131.11, 1197.19, 1230.45, 1247.25, 1290.3, 1336.67, 1377.99, 1414.76, 1440.23, 1483.33, 1490.05, 1491.26, 1498.69, 1723.22, 2964.62, 2997.88, 3005.66, 3039.05, 3074.29, 3109.02, 3111.26, 3808.97], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (16.3596, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.91217, -3.68575, -5.115, 1.33701, 1.3833],
                    [-3.70579, -1.20346, 4.9953, 0.408697, -0.411396],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.746218, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-10.1859, -0.908401, -0.43227, -0.261064, 0.0320075],
                    [-4.83294, -1.93932, 2.75954, -0.0346957, -0.122719],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.08859, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0595423, 0.00980574, -4.46437, 0.00337445, -0.0500917],
                    [0.0679062, 0.00555236, 0.250865, 0.0110415, 0.0610362],
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
        ***u_negfreq****-2054.87,
        'cm^-1',
    ),
)
reaction(
    label = 'g-bQOOHIsom',
    reactants = ['gRO2'],
    products = ['gQOOHb'],
    transitionState = 'g-bQOOHIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'gHO2elimFromRO2',
    E0 = (
        ***u_E0***-110.529,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([181.074, 245.225, 330.302], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([129.211, 184.588, 226.719, 314.203, 357.313, 376.188, 515.029, 539.404, 676.834, 764.472, 875.971, 925.338, 988.96, 999.894, 1023.99, 1076.17, 1093.67, 1187.73, 1244.03, 1284.14, 1329.76, 1373.58, 1408.53, 1423.23, 1424.3, 1495.83, 1507.43, 1520.92, 1573.31, 1595.05, 2997.75, 3033.9, 3070.62, 3088.6, 3113.57, 3171.74, 3267.25, 3828.53], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (16.5056, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.64837, -1.31898, -8.04897, -0.00288243, 0.181819],
                    [-0.397061, 1.41778, -1.65726, 0.0504239, 0.342702],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.829486, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.88474, -3.45475, -2.34312, 0.264784, -0.208499],
                    [2.3054, 0.338485, -1.62432, 0.11936, 0.0334426],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.04631, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0284793, 0.00969014, -3.92888, -0.0174217, -0.0184519],
                    [0.0356109, -0.0446612, 0.408414, -0.0386811, 0.0210266],
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
        ***u_negfreq****-944.099,
        'cm^-1',
    ),
)
reaction(
    label = 'gHO2elimFromRO2',
    reactants = ['gRO2'],
    products = ['galkene', 'HO2'],
    transitionState = 'gHO2elimFromRO2',
    tunneling = 'Eckart',
)

transitionState(label = 'gHO2elimFromb',
    E0 = (
        ***u_E0***-133.112,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([172.351, 229.742, 281.036], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([134.459, 246.252, 289.58, 335.621, 396.395, 440.436, 598.948, 813.763, 882.068, 919.09, 962.588, 986.628, 995.852, 1032.34, 1046.45, 1069.99, 1206.73, 1310.83, 1371.08, 1398.3, 1410.69, 1433.16, 1462.89, 1474.28, 1489.75, 1517.3, 1546.25, 3007.46, 3018.29, 3046.94, 3107.04, 3124.51, 3141.2, 3231.71, 3662.48, 3717.2], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.77327, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.05612, -17.1888, -0.976972, 0.512078, -0.0417437],
                    [4.29278, 7.39704, -1.51242, -3.12059, -0.533478],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (14.6189, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [1.01303, -1.85793, -1.93641, -2.18205, -1.41171],
                    [0.55082, -5.41218, -4.8256, -0.193405, -0.632902],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (18.021, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.73595, -2.9041, 0.804641, -0.905389, -0.195694],
                    [-2.63915, -4.64337, 3.12232, 0.518781, -0.625641],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.774301, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.74333, -3.09247, -2.45995, -0.127745, -0.775177],
                    [-1.22226, -0.686286, 0.866778, -0.75891, -0.180347],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.81435, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0461937, 0.00298962, -1.60181, -0.00304644, -0.0625212],
                    [-0.023973, -0.0178219, 0.77502, -0.00373461, 0.0106511],
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
        ***u_negfreq****-519.053,
        'cm^-1',
    ),
)
reaction(
    label = 'gHO2elimFromb',
    reactants = ['gQOOHb'],
    products = ['galkene', 'HO2'],
    transitionState = 'gHO2elimFromb',
    tunneling = 'Eckart',
)

transitionState(label = 'gH2OForm',
    E0 = (
        ***u_E0***-160.171,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([155.506, 227.406, 361.828], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([78.124, 142.12, 246.485, 273.619, 329.073, 341.585, 363.073, 418.039, 479.692, 529.712, 566.547, 828.917, 899.838, 915.51, 945.401, 1018.71, 1054.81, 1108.55, 1135.67, 1165.53, 1240.08, 1281.29, 1293.98, 1318.07, 1353.44, 1419.29, 1432.58, 1451.24, 1502.32, 1511.72, 1546.37, 2865.19, 2973.91, 2982.68, 3039.05, 3048.05, 3101.8, 3114.4, 3180.66, 3827.99], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.05632, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11710, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-765.909,
        'cm^-1',
    ),
)
reaction(
    label = 'gH2OForm',
    reactants = ['gQOOHa'],
    products = ['galdoxy', 'H2O'],
    transitionState = 'gH2OForm',
    tunneling = 'Eckart',
)

transitionState(label = 'gC4EtherFroma',
    E0 = (
        ***u_E0***-134.628,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([123.725, 296.433, 377.23], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([95.5732, 128.49, 204.956, 235.917, 280.484, 370.37, 396.663, 530.959, 604.683, 694.646, 826.506, 931.742, 961.769, 1006.38, 1046.01, 1101.75, 1115.23, 1159.98, 1204.2, 1247.51, 1261.99, 1323.17, 1349.9, 1381.06, 1413.88, 1470.94, 1500.95, 1510.86, 1527.65, 3017.1, 3043.58, 3056.91, 3085.79, 3104.01, 3123.91, 3181.66, 3821.71, 3842.65], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.543905, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.79317, -8.09852, -0.675949, -0.169556, 0.0160953],
                    [-9.53733, 5.11306, 0.432602, -0.570757, 0.151164],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.839378, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.31799, 1.27253, 0.349613, -0.164994, 0.0193387],
                    [-6.73541, 4.82663, -0.756595, 0.055162, 0.0103605],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.92095, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0205797, 0.0138843, -6.01467, -0.0203984, 0.026762],
                    [-0.00987849, 0.0318789, -0.289245, 0.034061, -0.027333],
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
        ***u_negfreq****-647.949,
        'cm^-1',
    ),
)
reaction(
    label = 'gC4EtherFroma',
    reactants = ['gQOOHa'],
    products = ['disub_c4ether', 'OH'],
    transitionState = 'gC4EtherFroma',
    tunneling = 'Eckart',
)

transitionState(label = 'gC4EtherFromg',
    E0 = (
        ***u_E0***-93.6856,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([128.345, 277.058, 316.376], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([92.9809, 191.086, 256.239, 287.866, 349.678, 397.508, 515.112, 550.063, 712.55, 814.039, 846.797, 915.853, 954.198, 978.051, 1021.27, 1054.16, 1092.52, 1123.89, 1137.83, 1190.76, 1221.11, 1291.85, 1327.35, 1343.29, 1388.5, 1450.91, 1467.28, 1521.85, 1533.67, 2984.39, 3022.51, 3039.67, 3066.94, 3089.5, 3161.51, 3273.77, 3774.31, 3814.88], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.728481, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-12.8347, 2.31709, 0.0963775, -0.0790149, -0.0062549],
                    [4.99535, -3.55036, 0.849346, -0.167153, 0.00382442],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (16.9184, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.978038, -3.23652, -12.8648, -2.85524, -1.46149],
                    [0.712193, -0.0212166, -0.471415, -0.100575, 0.0862223],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.508144, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-3.86927, -2.40467, -1.53503, -0.157379, 0.496847],
                    [-0.249843, 0.0892271, -0.744796, 1.14926, 0.100635],
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
        ***u_negfreq****-756.008,
        'cm^-1',
    ),
)
reaction(
    label = 'gC4EtherFromg',
    reactants = ['gQOOHg'],
    products = ['monosub_c4ether', 'OH'],
    transitionState = 'gC4EtherFromg',
    tunneling = 'Eckart',
)

transitionState(label = 'gEpoxyFromb',
    E0 = (
        ***u_E0***-154.113,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([155.3, 260.876, 371.807], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([86.0131, 173.652, 232.042, 258.389, 326.253, 376.431, 419.143, 531.906, 772.581, 898.484, 944.301, 977.731, 1003.67, 1019.61, 1072.53, 1102.51, 1181.53, 1214.88, 1269.02, 1296.07, 1349.54, 1402.81, 1411.9, 1441.61, 1474.45, 1487.05, 1492.1, 1531.93, 2956.22, 2991.66, 2995.64, 3041.63, 3071.05, 3100.84, 3122.17, 3742.99, 3805.9], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.801937, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.74622, -2.16601, 0.860762, -0.0402602, -0.000493689],
                    [-5.9714, 2.76135, 0.224625, -0.0761507, 0.000398418],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (17.0865, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.51389, -7.0899, -5.89755, -1.29335, -0.496521],
                    [2.47927, -0.960778, -1.20241, -0.22714, -0.109578],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.666283, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-10.541, -4.80386, -4.06934, 0.132895, 1.18389],
                    [-0.244687, -1.37004, 0.991349, 1.29209, 0.469647],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.00473, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.0494054, 0.00768538, -1.02959, 0.00828809, 0.0309595],
                    [-0.0100726, 0.00221911, -0.291436, 0.0045395, 0.0109213],
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
        ***u_negfreq****-631.601,
        'cm^-1',
    ),
)
reaction(
    label = 'gEpoxyFromb',
    reactants = ['gQOOHb'],
    products = ['disub_epoxy', 'OH'],
    transitionState = 'gEpoxyFromb',
    tunneling = 'Eckart',
)

transitionState(label = 'gDoublebscissionFroma',
    E0 = (
        ***u_E0***-106.362,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([101.727, 421.954, 469.67], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([68.7375, 123.787, 201.58, 271.174, 290.906, 364.176, 419.002, 468.953, 646.299, 762.026, 825.993, 862.732, 922.184, 1045.9, 1069.41, 1128.19, 1136.77, 1226.44, 1243.94, 1252.39, 1328.82, 1358.1, 1404.68, 1422.25, 1483.8, 1516.25, 1527.3, 1540.76, 2930.61, 2986.76, 3024.33, 3089.26, 3133.68, 3148.32, 3212.48, 3787.37, 3803.66], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.836218, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-3.08737, -16.2861, -0.113997, 0.935549, -0.000592075],
                    [0.509057, -0.91405, 0.0097981, 0.299159, 0.064985],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.776363, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.70779, -0.0556036, 0.0959655, -0.0580895, 0.00679468],
                    [5.86725, -3.46811, 0.0779069, -0.00525724, -0.0106765],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (12.3452, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [25.0503, 8.57184, -31.6401, 13.8374, -2.15891],
                    [49.7047, -45.5213, 18.0043, 1.29109, -2.82702],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.76634, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (12889.5, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-600.736,
        'cm^-1',
    ),
)
reaction(
    label = 'gDoublebscissionFroma',
    reactants = ['gQOOHa'],
    products = ['propene1ol', 'CH2O', 'OH'],
    transitionState = 'gDoublebscissionFroma',
    tunneling = 'Eckart',
)

transitionState(label = 'gDoublebscissionFromg',
    E0 = (
        ***u_E0***-67.3751,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([144.621, 311.768, 429.865], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([88.3724, 155.546, 242.929, 266.976, 337.959, 348.762, 399.283, 459.55, 509.485, 822.015, 859.136, 874.937, 886.993, 965.612, 1056.38, 1100.56, 1133.82, 1183.66, 1236.45, 1243.4, 1255.79, 1316.96, 1352.84, 1421.7, 1469.67, 1502.75, 1517.03, 1544.81, 2966.46, 3005.75, 3072.74, 3077.89, 3133.72, 3141.89, 3240.28, 3702.07, 3792.42], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.587611, 'amu*angstrom^2'),
            symmetry = 1,
            barrier = (15768.5, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (16.9254, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.36462, -9.82143, -5.96563, 0.886313, 0.944572],
                    [-4.52629, -1.14749, 6.49104, 0.585639, -1.22395],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (17.3568, 'amu*angstrom^2'),
            symmetry = 1,
            barrier = (26299.4, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.836612, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.26518, -1.47568, 0.089592, -0.0144304, -0.00615843],
                    [-6.05552, 3.5736, -0.112186, -0.0155442, 0.0121486],
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
        ***u_negfreq****-778.879,
        'cm^-1',
    ),
)
reaction(
    label = 'gDoublebscissionFromg',
    reactants = ['gQOOHg'],
    products = ['propene3ol', 'CH2O', 'OH'],
    transitionState = 'gDoublebscissionFromg',
    tunneling = 'Eckart',
)

transitionState(label = 'g-bscissionFromAlkoxy',
    E0 = (
        ***u_E0***-112.936,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([172.318, 231.077, 365.171], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([177.574, 249.891, 302.953, 329.919, 402.821, 535.948, 645.407, 812.994, 858.369, 900.431, 926.359, 1032.34, 1056.58, 1103.74, 1139.18, 1154.13, 1249.66, 1281.6, 1320.84, 1404.6, 1415.25, 1441.31, 1468.14, 1487.42, 1491.68, 1505.07, 1605.21, 2929.18, 2970.09, 2998.17, 3002.76, 3053.04, 3066.84, 3115.91, 3162.83, 3494.84], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.98772, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0811909, 0.042885, -3.38898, -0.0323424, 0.0973292],
                    [-0.013927, -0.0252572, 0.160698, -0.013071, -0.00398281],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (13.3429, 'amu*angstrom^2'),
            symmetry = 1,
            barrier = (40216, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (35.8779, 'amu*angstrom^2'),
            symmetry = 1,
            barrier = (36133.6, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (15.8024, 'amu*angstrom^2'),
            symmetry = 1,
            barrier = (33094.9, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.770782, 'amu*angstrom^2'),
            symmetry = 1,
            barrier = (34834.5, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-252.83,
        'cm^-1',
    ),
)
reaction(
    label = 'g-bscissionFromAlkoxy',
    reactants = ['gQOOH[O]'],
    products = ['CH2O', 'ipropylOOH'],
    transitionState = 'g-bscissionFromAlkoxy',
    tunneling = 'Eckart',
)

transitionState(label = 'gAlkoxyHabs',
    E0 = (
        ***u_E0***-86.704,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([145.149, 229.099, 313.021], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([101.255, 225.763, 286.576, 345.092, 404.973, 547.702, 615.814, 688.782, 838.881, 875.496, 913.297, 952.174, 1002.99, 1019.4, 1078.82, 1134.29, 1150.32, 1164.35, 1214, 1294.75, 1316.09, 1346.82, 1367.86, 1410.97, 1420.96, 1502.41, 1504.82, 1520.12, 1561.76, 1756.93, 2994.89, 3033.55, 3045.21, 3077.02, 3098.19, 3104.42, 3120.91, 3373.91], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.04451, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0247049, -0.0181068, -6.5275, 0.0384181, -0.0216507],
                    [-0.0606012, -0.00744921, 0.297075, -0.0185457, -0.0520026],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (15.4919, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.710662, -9.5017, -7.41751, -3.5446, -1.16387],
                    [3.70644, -6.9009, 0.440399, 1.66727, 0.8255],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.731085, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.42097, -5.11132, -2.61437, -0.600573, -0.00979367],
                    [6.69632, 1.22579, -2.29641, -1.51158, -0.355712],
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
        ***u_negfreq****-1382.85,
        'cm^-1',
    ),
)
reaction(
    label = 'gAlkoxyHabs',
    reactants = ['gQOOH[O]'],
    products = ['galdol', 'OH'],
    transitionState = 'gAlkoxyHabs',
    tunneling = 'Eckart',
)

transitionState(label = 'gAldolFroma',
    E0 = (
        ***u_E0***-116.664,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([154.286, 251.485, 346.715], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([72.0973, 112.595, 211.301, 290.103, 327.925, 345.889, 394.85, 468.157, 531.501, 574.802, 846.222, 910.014, 934.556, 948.323, 976.769, 1038.35, 1091.36, 1113.12, 1174.22, 1228.85, 1266.91, 1299.99, 1332.26, 1350.48, 1390.29, 1421.46, 1461.01, 1505.84, 1508.21, 1573.23, 2762.77, 2951.64, 2965.22, 3040.42, 3084.38, 3102.35, 3113.75, 3194.88, 3809.54], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.487121, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.84763, -0.0681959, 0.170823, 0.737564, -0.352091],
                    [-3.82686, 3.81997, -1.6115, 0.184491, 0.431336],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.06321, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (9645.76, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-950.701,
        'cm^-1',
    ),
)
reaction(
    label = 'gAldolFroma',
    reactants = ['gQOOHa'],
    products = ['galdol', 'OH'],
    transitionState = 'gAldolFroma',
    tunneling = 'Eckart',
)

network(
    label = 'C4H9O3',
    isomers = ['gRO2', 'gQOOH[O]', 'gQOOHa', 'gQOOHg', 'gQOOHb'],
    reactants = [['gR', 'O2']],
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
