import re


def parse_input(input_str):
    task_pattern = r"Button A: X\+(\d+), Y\+(\d+)\s*Button B: X\+(\d+), Y\+(\d+)\s*Prize: X=(\d+), Y=(\d+)"
    matches = re.findall(task_pattern, input_str)
    tasks = [
        ((int(a_x), int(a_y)), (int(b_x), int(b_y)), (int(prize_x), int(prize_y)))
        for a_x, a_y, b_x, b_y, prize_x, prize_y in matches
    ]
    return tasks


def calculate_button_presses(button_a, button_b, target):
    button_a_x, button_a_y = button_a
    button_b_x, button_b_y = button_b
    target_x, target_y = target

    optimal_a_presses = None
    optimal_b_presses = None

    max_a_presses = target_x // button_a_x
    max_b_presses = target_y // button_b_y

    for a_presses in range(max_a_presses + 1):
        for b_presses in range(max_b_presses + 1):
            position_x = (a_presses * button_a_x) + (b_presses * button_b_x)
            position_y = (a_presses * button_a_y) + (b_presses * button_b_y)

            if position_x == target_x and position_y == target_y:
                if (optimal_a_presses is None) or (a_presses < optimal_a_presses):
                    optimal_a_presses = a_presses
                    optimal_b_presses = b_presses

    if optimal_a_presses is not None:
        return optimal_a_presses, optimal_b_presses
    else:
        return None


def process_input(input_str):
    tasks = parse_input(input_str)
    results = []
    total_weighted_sum = 0

    for button_a, button_b, prize in tasks:
        result = calculate_button_presses(button_a, button_b, prize)

        if result:
            a_presses, b_presses = result
            weighted_sum = (a_presses * 3) + (b_presses * 1)
            results.append(f"Press Button A {a_presses} times and Button B {b_presses} times. Sum: {weighted_sum}.")
            total_weighted_sum += weighted_sum
        else:
            results.append("No valid sequence of button presses found.")

    results.append(f"Total Weighted Sum: {total_weighted_sum}.")
    return results

# Input string in the specified format
input_string = """
Button A: X+49, Y+27
Button B: X+35, Y+65
Prize: X=4326, Y=4898

Button A: X+82, Y+64
Button B: X+20, Y+67
Prize: X=6818, Y=10409

Button A: X+75, Y+72
Button B: X+95, Y+15
Prize: X=8360, Y=4749

Button A: X+59, Y+26
Button B: X+15, Y+29
Prize: X=7401, Y=3032

Button A: X+77, Y+38
Button B: X+15, Y+46
Prize: X=13582, Y=10664

Button A: X+39, Y+11
Button B: X+27, Y+40
Prize: X=1367, Y=2880

Button A: X+50, Y+28
Button B: X+20, Y+55
Prize: X=7220, Y=383

Button A: X+63, Y+63
Button B: X+21, Y+97
Prize: X=4200, Y=10964

Button A: X+60, Y+31
Button B: X+13, Y+52
Prize: X=5226, Y=4907

Button A: X+13, Y+96
Button B: X+84, Y+22
Prize: X=7154, Y=10948

Button A: X+68, Y+31
Button B: X+21, Y+61
Prize: X=2715, Y=4889

Button A: X+62, Y+19
Button B: X+80, Y+86
Prize: X=6434, Y=4677

Button A: X+69, Y+23
Button B: X+12, Y+51
Prize: X=14678, Y=3050

Button A: X+49, Y+16
Button B: X+74, Y+92
Prize: X=8637, Y=7908

Button A: X+11, Y+78
Button B: X+75, Y+77
Prize: X=1390, Y=5763

Button A: X+13, Y+63
Button B: X+65, Y+13
Prize: X=10429, Y=5841

Button A: X+70, Y+56
Button B: X+36, Y+98
Prize: X=5934, Y=6062

Button A: X+48, Y+20
Button B: X+12, Y+32
Prize: X=4056, Y=3364

Button A: X+17, Y+43
Button B: X+58, Y+46
Prize: X=5494, Y=5538

Button A: X+33, Y+96
Button B: X+67, Y+34
Prize: X=4214, Y=3248

Button A: X+54, Y+21
Button B: X+13, Y+57
Prize: X=5735, Y=2930

Button A: X+24, Y+68
Button B: X+47, Y+34
Prize: X=5685, Y=8670

Button A: X+33, Y+16
Button B: X+14, Y+34
Prize: X=2667, Y=2436

Button A: X+36, Y+11
Button B: X+42, Y+79
Prize: X=13676, Y=1462

Button A: X+66, Y+25
Button B: X+19, Y+56
Prize: X=4719, Y=18733

Button A: X+90, Y+73
Button B: X+27, Y+72
Prize: X=9378, Y=10813

Button A: X+69, Y+39
Button B: X+35, Y+94
Prize: X=2648, Y=5356

Button A: X+63, Y+20
Button B: X+55, Y+91
Prize: X=7525, Y=9081

Button A: X+44, Y+80
Button B: X+97, Y+47
Prize: X=6841, Y=4547

Button A: X+63, Y+24
Button B: X+29, Y+61
Prize: X=16541, Y=2222

Button A: X+62, Y+14
Button B: X+33, Y+78
Prize: X=504, Y=8112

Button A: X+80, Y+38
Button B: X+15, Y+57
Prize: X=4385, Y=8081

Button A: X+38, Y+65
Button B: X+45, Y+14
Prize: X=3503, Y=17060

Button A: X+43, Y+70
Button B: X+33, Y+11
Prize: X=19669, Y=19086

Button A: X+90, Y+53
Button B: X+20, Y+80
Prize: X=3770, Y=6177

Button A: X+84, Y+72
Button B: X+24, Y+75
Prize: X=3084, Y=7542

Button A: X+56, Y+14
Button B: X+12, Y+78
Prize: X=2140, Y=3760

Button A: X+40, Y+14
Button B: X+11, Y+35
Prize: X=16457, Y=9167

Button A: X+30, Y+56
Button B: X+26, Y+11
Prize: X=1758, Y=1911

Button A: X+46, Y+84
Button B: X+49, Y+11
Prize: X=7409, Y=5661

Button A: X+53, Y+16
Button B: X+25, Y+60
Prize: X=7756, Y=10112

Button A: X+12, Y+51
Button B: X+58, Y+23
Prize: X=11192, Y=10037

Button A: X+79, Y+37
Button B: X+18, Y+55
Prize: X=9850, Y=5282

Button A: X+92, Y+40
Button B: X+29, Y+66
Prize: X=10106, Y=8772

Button A: X+47, Y+27
Button B: X+16, Y+50
Prize: X=7125, Y=13151

Button A: X+45, Y+17
Button B: X+28, Y+72
Prize: X=11120, Y=18168

Button A: X+47, Y+11
Button B: X+13, Y+99
Prize: X=1953, Y=9669

Button A: X+69, Y+46
Button B: X+25, Y+52
Prize: X=7600, Y=8494

Button A: X+51, Y+27
Button B: X+23, Y+69
Prize: X=2316, Y=4806

Button A: X+14, Y+71
Button B: X+88, Y+47
Prize: X=1644, Y=3546

Button A: X+18, Y+35
Button B: X+46, Y+11
Prize: X=9558, Y=2941

Button A: X+61, Y+13
Button B: X+41, Y+91
Prize: X=4435, Y=6539

Button A: X+34, Y+98
Button B: X+82, Y+43
Prize: X=7824, Y=7470

Button A: X+15, Y+48
Button B: X+57, Y+18
Prize: X=13853, Y=7208

Button A: X+55, Y+18
Button B: X+13, Y+39
Prize: X=15982, Y=15563

Button A: X+28, Y+41
Button B: X+43, Y+18
Prize: X=199, Y=10125

Button A: X+15, Y+63
Button B: X+92, Y+83
Prize: X=2547, Y=4326

Button A: X+77, Y+29
Button B: X+25, Y+62
Prize: X=1324, Y=1340

Button A: X+72, Y+26
Button B: X+21, Y+57
Prize: X=11162, Y=14636

Button A: X+79, Y+30
Button B: X+22, Y+36
Prize: X=5320, Y=4536

Button A: X+36, Y+12
Button B: X+36, Y+95
Prize: X=2772, Y=2916

Button A: X+35, Y+56
Button B: X+86, Y+18
Prize: X=4732, Y=2548

Button A: X+51, Y+16
Button B: X+45, Y+82
Prize: X=10163, Y=11136

Button A: X+43, Y+14
Button B: X+47, Y+75
Prize: X=15976, Y=14193

Button A: X+11, Y+94
Button B: X+54, Y+35
Prize: X=3924, Y=8798

Button A: X+50, Y+64
Button B: X+56, Y+12
Prize: X=7288, Y=6464

Button A: X+97, Y+12
Button B: X+20, Y+82
Prize: X=9072, Y=7882

Button A: X+19, Y+75
Button B: X+97, Y+68
Prize: X=9149, Y=10608

Button A: X+46, Y+13
Button B: X+25, Y+55
Prize: X=2126, Y=3593

Button A: X+60, Y+27
Button B: X+15, Y+29
Prize: X=14690, Y=7012

Button A: X+56, Y+23
Button B: X+12, Y+68
Prize: X=5392, Y=3476

Button A: X+11, Y+32
Button B: X+58, Y+26
Prize: X=13242, Y=8184

Button A: X+56, Y+13
Button B: X+23, Y+53
Prize: X=16727, Y=19225

Button A: X+28, Y+91
Button B: X+77, Y+39
Prize: X=5796, Y=9542

Button A: X+43, Y+11
Button B: X+52, Y+86
Prize: X=166, Y=11790

Button A: X+28, Y+11
Button B: X+35, Y+51
Prize: X=928, Y=16119

Button A: X+23, Y+51
Button B: X+94, Y+59
Prize: X=4318, Y=3149

Button A: X+64, Y+14
Button B: X+17, Y+29
Prize: X=2692, Y=690

Button A: X+34, Y+17
Button B: X+21, Y+39
Prize: X=18391, Y=696

Button A: X+64, Y+63
Button B: X+17, Y+70
Prize: X=1491, Y=3332

Button A: X+25, Y+38
Button B: X+43, Y+14
Prize: X=1344, Y=1324

Button A: X+11, Y+64
Button B: X+45, Y+15
Prize: X=13983, Y=18172

Button A: X+36, Y+12
Button B: X+24, Y+70
Prize: X=7376, Y=6276

Button A: X+61, Y+73
Button B: X+87, Y+30
Prize: X=11742, Y=7011

Button A: X+43, Y+34
Button B: X+21, Y+79
Prize: X=3308, Y=5673

Button A: X+91, Y+59
Button B: X+31, Y+89
Prize: X=5143, Y=5057

Button A: X+52, Y+16
Button B: X+13, Y+38
Prize: X=2444, Y=3336

Button A: X+89, Y+33
Button B: X+32, Y+89
Prize: X=4360, Y=3545

Button A: X+11, Y+57
Button B: X+56, Y+19
Prize: X=3779, Y=5459

Button A: X+37, Y+14
Button B: X+19, Y+60
Prize: X=5952, Y=13748

Button A: X+36, Y+17
Button B: X+33, Y+62
Prize: X=3267, Y=1682

Button A: X+22, Y+46
Button B: X+38, Y+23
Prize: X=16324, Y=5275

Button A: X+47, Y+32
Button B: X+19, Y+44
Prize: X=2960, Y=5420

Button A: X+69, Y+21
Button B: X+23, Y+73
Prize: X=1710, Y=6310

Button A: X+50, Y+24
Button B: X+32, Y+59
Prize: X=2194, Y=8839

Button A: X+27, Y+12
Button B: X+32, Y+67
Prize: X=4522, Y=5982

Button A: X+31, Y+46
Button B: X+27, Y+13
Prize: X=15443, Y=4011

Button A: X+23, Y+15
Button B: X+30, Y+61
Prize: X=872, Y=1646

Button A: X+45, Y+23
Button B: X+27, Y+56
Prize: X=4670, Y=15089

Button A: X+97, Y+82
Button B: X+17, Y+76
Prize: X=4139, Y=8306

Button A: X+53, Y+21
Button B: X+63, Y+99
Prize: X=9415, Y=8691

Button A: X+29, Y+60
Button B: X+66, Y+34
Prize: X=6790, Y=9804

Button A: X+11, Y+29
Button B: X+81, Y+59
Prize: X=2188, Y=7032

Button A: X+81, Y+99
Button B: X+65, Y+11
Prize: X=5726, Y=4466

Button A: X+65, Y+11
Button B: X+31, Y+88
Prize: X=19762, Y=1948

Button A: X+15, Y+25
Button B: X+82, Y+45
Prize: X=4199, Y=2690

Button A: X+16, Y+31
Button B: X+39, Y+21
Prize: X=13113, Y=12471

Button A: X+67, Y+48
Button B: X+26, Y+96
Prize: X=5306, Y=6432

Button A: X+91, Y+95
Button B: X+92, Y+18
Prize: X=14189, Y=8257

Button A: X+79, Y+78
Button B: X+12, Y+93
Prize: X=6242, Y=8841

Button A: X+31, Y+82
Button B: X+53, Y+33
Prize: X=5683, Y=5921

Button A: X+65, Y+33
Button B: X+13, Y+48
Prize: X=10845, Y=14051

Button A: X+85, Y+46
Button B: X+16, Y+84
Prize: X=8449, Y=7134

Button A: X+42, Y+92
Button B: X+81, Y+51
Prize: X=8385, Y=8885

Button A: X+20, Y+72
Button B: X+40, Y+25
Prize: X=2640, Y=6648

Button A: X+26, Y+77
Button B: X+57, Y+17
Prize: X=11197, Y=19687

Button A: X+91, Y+21
Button B: X+62, Y+68
Prize: X=8675, Y=5653

Button A: X+35, Y+19
Button B: X+14, Y+27
Prize: X=14851, Y=2188

Button A: X+94, Y+94
Button B: X+14, Y+67
Prize: X=8580, Y=9746

Button A: X+74, Y+26
Button B: X+31, Y+47
Prize: X=6350, Y=4542

Button A: X+58, Y+54
Button B: X+74, Y+12
Prize: X=8248, Y=3924

Button A: X+24, Y+42
Button B: X+37, Y+15
Prize: X=14351, Y=6071

Button A: X+18, Y+53
Button B: X+87, Y+66
Prize: X=5571, Y=7846

Button A: X+47, Y+50
Button B: X+14, Y+66
Prize: X=2910, Y=7542

Button A: X+22, Y+47
Button B: X+53, Y+19
Prize: X=12119, Y=4865

Button A: X+55, Y+30
Button B: X+20, Y+53
Prize: X=7885, Y=212

Button A: X+85, Y+11
Button B: X+80, Y+68
Prize: X=4370, Y=2122

Button A: X+81, Y+32
Button B: X+14, Y+63
Prize: X=7128, Y=12371

Button A: X+15, Y+36
Button B: X+47, Y+22
Prize: X=4189, Y=1830

Button A: X+95, Y+77
Button B: X+27, Y+96
Prize: X=9189, Y=13896

Button A: X+14, Y+92
Button B: X+80, Y+20
Prize: X=8268, Y=5784

Button A: X+40, Y+11
Button B: X+49, Y+50
Prize: X=2187, Y=711

Button A: X+17, Y+52
Button B: X+63, Y+23
Prize: X=219, Y=13789

Button A: X+31, Y+59
Button B: X+55, Y+21
Prize: X=974, Y=1268

Button A: X+18, Y+80
Button B: X+81, Y+16
Prize: X=17585, Y=12592

Button A: X+27, Y+66
Button B: X+55, Y+12
Prize: X=6864, Y=6126

Button A: X+88, Y+93
Button B: X+82, Y+20
Prize: X=4452, Y=1372

Button A: X+14, Y+61
Button B: X+73, Y+11
Prize: X=4295, Y=15239

Button A: X+16, Y+86
Button B: X+61, Y+57
Prize: X=3605, Y=3937

Button A: X+47, Y+15
Button B: X+14, Y+47
Prize: X=17126, Y=13036

Button A: X+12, Y+44
Button B: X+57, Y+25
Prize: X=17342, Y=4318

Button A: X+38, Y+11
Button B: X+42, Y+70
Prize: X=18670, Y=18130

Button A: X+12, Y+57
Button B: X+91, Y+66
Prize: X=8885, Y=7410

Button A: X+53, Y+65
Button B: X+72, Y+26
Prize: X=7245, Y=6331

Button A: X+16, Y+46
Button B: X+55, Y+20
Prize: X=3309, Y=1364

Button A: X+39, Y+85
Button B: X+51, Y+11
Prize: X=14393, Y=1461

Button A: X+38, Y+16
Button B: X+15, Y+28
Prize: X=6466, Y=2416

Button A: X+67, Y+22
Button B: X+32, Y+97
Prize: X=1295, Y=3020

Button A: X+17, Y+64
Button B: X+65, Y+27
Prize: X=13599, Y=6874

Button A: X+64, Y+18
Button B: X+30, Y+75
Prize: X=10406, Y=3707

Button A: X+97, Y+21
Button B: X+56, Y+98
Prize: X=5026, Y=2548

Button A: X+42, Y+22
Button B: X+35, Y+68
Prize: X=5530, Y=6572

Button A: X+31, Y+13
Button B: X+24, Y+49
Prize: X=7108, Y=6795

Button A: X+66, Y+94
Button B: X+89, Y+16
Prize: X=4541, Y=3034

Button A: X+46, Y+19
Button B: X+17, Y+51
Prize: X=11761, Y=3838

Button A: X+32, Y+77
Button B: X+58, Y+15
Prize: X=6526, Y=8354

Button A: X+46, Y+35
Button B: X+11, Y+30
Prize: X=2215, Y=19550

Button A: X+26, Y+47
Button B: X+82, Y+17
Prize: X=7708, Y=3304

Button A: X+37, Y+21
Button B: X+25, Y+88
Prize: X=3748, Y=7294

Button A: X+53, Y+16
Button B: X+13, Y+67
Prize: X=7109, Y=12828

Button A: X+31, Y+44
Button B: X+71, Y+18
Prize: X=3327, Y=4060

Button A: X+52, Y+94
Button B: X+25, Y+15
Prize: X=4234, Y=6748

Button A: X+42, Y+20
Button B: X+27, Y+52
Prize: X=13487, Y=10916

Button A: X+72, Y+28
Button B: X+12, Y+36
Prize: X=7448, Y=6064

Button A: X+28, Y+64
Button B: X+68, Y+33
Prize: X=15452, Y=2894

Button A: X+17, Y+47
Button B: X+58, Y+11
Prize: X=4677, Y=1281

Button A: X+22, Y+99
Button B: X+96, Y+41
Prize: X=4342, Y=10546

Button A: X+48, Y+21
Button B: X+13, Y+42
Prize: X=19657, Y=14438

Button A: X+18, Y+97
Button B: X+87, Y+79
Prize: X=6468, Y=12245

Button A: X+22, Y+95
Button B: X+66, Y+41
Prize: X=1188, Y=1958

Button A: X+99, Y+24
Button B: X+77, Y+81
Prize: X=7238, Y=4248

Button A: X+15, Y+37
Button B: X+56, Y+37
Prize: X=846, Y=17898

Button A: X+44, Y+17
Button B: X+18, Y+64
Prize: X=10310, Y=10570

Button A: X+32, Y+57
Button B: X+54, Y+21
Prize: X=10890, Y=11813

Button A: X+39, Y+13
Button B: X+31, Y+48
Prize: X=10480, Y=12892

Button A: X+94, Y+29
Button B: X+58, Y+67
Prize: X=3368, Y=2856

Button A: X+37, Y+54
Button B: X+33, Y+14
Prize: X=3698, Y=10524

Button A: X+14, Y+88
Button B: X+87, Y+78
Prize: X=2740, Y=6908

Button A: X+30, Y+68
Button B: X+40, Y+13
Prize: X=4710, Y=12879

Button A: X+93, Y+49
Button B: X+11, Y+34
Prize: X=3313, Y=3325

Button A: X+29, Y+62
Button B: X+62, Y+27
Prize: X=1821, Y=18681

Button A: X+19, Y+34
Button B: X+77, Y+21
Prize: X=7073, Y=3197

Button A: X+44, Y+19
Button B: X+11, Y+26
Prize: X=8647, Y=6467

Button A: X+93, Y+17
Button B: X+16, Y+72
Prize: X=5651, Y=6559

Button A: X+80, Y+40
Button B: X+57, Y+94
Prize: X=6467, Y=9194

Button A: X+73, Y+89
Button B: X+49, Y+17
Prize: X=7255, Y=5255

Button A: X+97, Y+14
Button B: X+29, Y+51
Prize: X=10836, Y=5590

Button A: X+73, Y+49
Button B: X+11, Y+33
Prize: X=1138, Y=8774

Button A: X+18, Y+45
Button B: X+42, Y+19
Prize: X=12128, Y=15456

Button A: X+72, Y+85
Button B: X+88, Y+28
Prize: X=6656, Y=7023

Button A: X+44, Y+78
Button B: X+73, Y+43
Prize: X=8759, Y=8701

Button A: X+81, Y+61
Button B: X+18, Y+88
Prize: X=8532, Y=12902

Button A: X+14, Y+64
Button B: X+74, Y+22
Prize: X=6620, Y=5474

Button A: X+67, Y+15
Button B: X+29, Y+83
Prize: X=5560, Y=8666

Button A: X+30, Y+65
Button B: X+70, Y+46
Prize: X=4370, Y=6087

Button A: X+15, Y+62
Button B: X+52, Y+16
Prize: X=19725, Y=12474

Button A: X+40, Y+94
Button B: X+27, Y+11
Prize: X=4401, Y=8087

Button A: X+30, Y+16
Button B: X+27, Y+51
Prize: X=5666, Y=12682

Button A: X+95, Y+44
Button B: X+42, Y+82
Prize: X=9014, Y=10242

Button A: X+37, Y+52
Button B: X+91, Y+31
Prize: X=7684, Y=6439

Button A: X+14, Y+62
Button B: X+68, Y+12
Prize: X=3842, Y=1058

Button A: X+48, Y+16
Button B: X+43, Y+69
Prize: X=2989, Y=1379

Button A: X+53, Y+17
Button B: X+17, Y+77
Prize: X=3113, Y=6293

Button A: X+78, Y+27
Button B: X+41, Y+52
Prize: X=7486, Y=4028

Button A: X+50, Y+78
Button B: X+96, Y+17
Prize: X=4470, Y=4318

Button A: X+35, Y+19
Button B: X+27, Y+63
Prize: X=3947, Y=5575

Button A: X+37, Y+75
Button B: X+50, Y+19
Prize: X=3465, Y=2911

Button A: X+13, Y+35
Button B: X+45, Y+30
Prize: X=12234, Y=17425

Button A: X+24, Y+13
Button B: X+27, Y+52
Prize: X=17189, Y=9415

Button A: X+11, Y+44
Button B: X+75, Y+46
Prize: X=9815, Y=5598

Button A: X+18, Y+34
Button B: X+54, Y+23
Prize: X=16874, Y=15442

Button A: X+36, Y+98
Button B: X+88, Y+32
Prize: X=8056, Y=4288

Button A: X+15, Y+44
Button B: X+27, Y+12
Prize: X=1220, Y=5824

Button A: X+44, Y+37
Button B: X+20, Y+70
Prize: X=1696, Y=1958

Button A: X+45, Y+64
Button B: X+41, Y+19
Prize: X=3330, Y=5191

Button A: X+38, Y+12
Button B: X+49, Y+58
Prize: X=4672, Y=2496

Button A: X+29, Y+12
Button B: X+47, Y+63
Prize: X=16601, Y=7430

Button A: X+78, Y+12
Button B: X+15, Y+81
Prize: X=14060, Y=16766

Button A: X+38, Y+13
Button B: X+16, Y+57
Prize: X=3594, Y=787

Button A: X+32, Y+65
Button B: X+61, Y+25
Prize: X=4411, Y=6250

Button A: X+57, Y+16
Button B: X+13, Y+76
Prize: X=6816, Y=9076

Button A: X+86, Y+43
Button B: X+29, Y+88
Prize: X=5382, Y=7395

Button A: X+33, Y+69
Button B: X+94, Y+53
Prize: X=2776, Y=3077

Button A: X+54, Y+39
Button B: X+21, Y+88
Prize: X=5874, Y=8321

Button A: X+69, Y+21
Button B: X+11, Y+47
Prize: X=14267, Y=12383

Button A: X+16, Y+58
Button B: X+64, Y+24
Prize: X=9392, Y=8654

Button A: X+18, Y+57
Button B: X+95, Y+68
Prize: X=10326, Y=10347

Button A: X+16, Y+59
Button B: X+58, Y+50
Prize: X=3214, Y=4805

Button A: X+83, Y+46
Button B: X+37, Y+90
Prize: X=5156, Y=9112

Button A: X+16, Y+17
Button B: X+86, Y+23
Prize: X=2160, Y=1748

Button A: X+99, Y+95
Button B: X+65, Y+14
Prize: X=5569, Y=4957

Button A: X+13, Y+30
Button B: X+90, Y+56
Prize: X=6456, Y=4280

Button A: X+84, Y+44
Button B: X+11, Y+59
Prize: X=8019, Y=7235

Button A: X+12, Y+70
Button B: X+67, Y+13
Prize: X=15733, Y=5321

Button A: X+66, Y+43
Button B: X+12, Y+41
Prize: X=12650, Y=9495

Button A: X+60, Y+14
Button B: X+29, Y+70
Prize: X=4132, Y=5264

Button A: X+51, Y+78
Button B: X+43, Y+16
Prize: X=1046, Y=7094

Button A: X+13, Y+49
Button B: X+78, Y+40
Prize: X=12665, Y=1581

Button A: X+53, Y+12
Button B: X+63, Y+91
Prize: X=6607, Y=7865

Button A: X+20, Y+50
Button B: X+41, Y+30
Prize: X=3615, Y=5050

Button A: X+12, Y+22
Button B: X+53, Y+27
Prize: X=8918, Y=1734

Button A: X+89, Y+89
Button B: X+87, Y+22
Prize: X=9350, Y=6620

Button A: X+89, Y+17
Button B: X+32, Y+49
Prize: X=8106, Y=1677

Button A: X+72, Y+40
Button B: X+16, Y+52
Prize: X=6264, Y=12268

Button A: X+33, Y+16
Button B: X+34, Y+67
Prize: X=2090, Y=4237

Button A: X+56, Y+21
Button B: X+17, Y+59
Prize: X=7083, Y=1672

Button A: X+11, Y+29
Button B: X+68, Y+26
Prize: X=2416, Y=4576

Button A: X+39, Y+20
Button B: X+19, Y+73
Prize: X=3703, Y=4619

Button A: X+74, Y+15
Button B: X+12, Y+76
Prize: X=4960, Y=3286

Button A: X+37, Y+14
Button B: X+13, Y+59
Prize: X=13171, Y=9330

Button A: X+65, Y+15
Button B: X+25, Y+90
Prize: X=6410, Y=5775

Button A: X+24, Y+49
Button B: X+44, Y+12
Prize: X=9004, Y=16546

Button A: X+94, Y+28
Button B: X+67, Y+90
Prize: X=6441, Y=4230

Button A: X+12, Y+93
Button B: X+76, Y+82
Prize: X=6984, Y=10017

Button A: X+14, Y+53
Button B: X+59, Y+20
Prize: X=6128, Y=395

Button A: X+61, Y+23
Button B: X+49, Y+69
Prize: X=2850, Y=2944

Button A: X+48, Y+82
Button B: X+47, Y+12
Prize: X=4376, Y=13904

Button A: X+13, Y+89
Button B: X+51, Y+51
Prize: X=1816, Y=7364

Button A: X+67, Y+30
Button B: X+16, Y+36
Prize: X=3092, Y=5636

Button A: X+74, Y+99
Button B: X+50, Y+11
Prize: X=5626, Y=3223

Button A: X+88, Y+45
Button B: X+48, Y+89
Prize: X=5424, Y=7221

Button A: X+72, Y+51
Button B: X+38, Y+94
Prize: X=2746, Y=3488

Button A: X+24, Y+99
Button B: X+72, Y+59
Prize: X=7080, Y=9451

Button A: X+45, Y+17
Button B: X+32, Y+57
Prize: X=9723, Y=6928

Button A: X+87, Y+48
Button B: X+42, Y+72
Prize: X=4551, Y=3048

Button A: X+46, Y+52
Button B: X+11, Y+93
Prize: X=4550, Y=9494

Button A: X+57, Y+18
Button B: X+14, Y+52
Prize: X=368, Y=14984

Button A: X+99, Y+14
Button B: X+68, Y+87
Prize: X=8855, Y=8062

Button A: X+25, Y+12
Button B: X+64, Y+94
Prize: X=3097, Y=2942

Button A: X+97, Y+15
Button B: X+88, Y+81
Prize: X=11806, Y=5667

Button A: X+87, Y+12
Button B: X+21, Y+60
Prize: X=7938, Y=6120

Button A: X+17, Y+39
Button B: X+49, Y+35
Prize: X=1428, Y=10060

Button A: X+23, Y+52
Button B: X+43, Y+29
Prize: X=600, Y=879

Button A: X+11, Y+49
Button B: X+82, Y+37
Prize: X=7574, Y=9191

Button A: X+16, Y+75
Button B: X+81, Y+20
Prize: X=16020, Y=8530

Button A: X+15, Y+95
Button B: X+67, Y+80
Prize: X=1559, Y=4020

Button A: X+70, Y+51
Button B: X+15, Y+76
Prize: X=4670, Y=9389

Button A: X+86, Y+15
Button B: X+54, Y+73
Prize: X=8976, Y=6970

Button A: X+17, Y+52
Button B: X+29, Y+12
Prize: X=18080, Y=9392

Button A: X+25, Y+11
Button B: X+42, Y+71
Prize: X=17374, Y=11683

Button A: X+27, Y+42
Button B: X+41, Y+17
Prize: X=1569, Y=10566

Button A: X+28, Y+51
Button B: X+57, Y+28
Prize: X=5371, Y=16859

Button A: X+98, Y+58
Button B: X+51, Y+96
Prize: X=5535, Y=9660

Button A: X+49, Y+15
Button B: X+34, Y+71
Prize: X=528, Y=4268

Button A: X+18, Y+47
Button B: X+90, Y+40
Prize: X=4374, Y=4401

Button A: X+38, Y+84
Button B: X+92, Y+41
Prize: X=10726, Y=10883

Button A: X+17, Y+48
Button B: X+72, Y+36
Prize: X=18856, Y=12548

Button A: X+49, Y+18
Button B: X+51, Y+90
Prize: X=5399, Y=7542

Button A: X+57, Y+14
Button B: X+33, Y+67
Prize: X=8741, Y=7213

Button A: X+77, Y+25
Button B: X+14, Y+57
Prize: X=3668, Y=6279

Button A: X+40, Y+87
Button B: X+20, Y+11
Prize: X=4860, Y=8913

Button A: X+64, Y+39
Button B: X+11, Y+21
Prize: X=5378, Y=2393

Button A: X+19, Y+35
Button B: X+50, Y+20
Prize: X=9101, Y=605

Button A: X+72, Y+18
Button B: X+18, Y+56
Prize: X=10970, Y=10150

Button A: X+47, Y+25
Button B: X+12, Y+28
Prize: X=4918, Y=6618

Button A: X+72, Y+44
Button B: X+19, Y+41
Prize: X=17136, Y=7388

Button A: X+92, Y+19
Button B: X+12, Y+16
Prize: X=4884, Y=1536

Button A: X+25, Y+87
Button B: X+83, Y+42
Prize: X=5153, Y=7812

Button A: X+84, Y+99
Button B: X+91, Y+17
Prize: X=8043, Y=7584

Button A: X+16, Y+99
Button B: X+72, Y+60
Prize: X=7568, Y=9048

Button A: X+26, Y+56
Button B: X+75, Y+33
Prize: X=2104, Y=2218

Button A: X+24, Y+62
Button B: X+40, Y+19
Prize: X=16632, Y=2159

Button A: X+23, Y+61
Button B: X+52, Y+13
Prize: X=14004, Y=5554

Button A: X+25, Y+99
Button B: X+87, Y+42
Prize: X=3260, Y=3834

Button A: X+27, Y+74
Button B: X+32, Y+11
Prize: X=1722, Y=1498

Button A: X+42, Y+13
Button B: X+16, Y+41
Prize: X=2384, Y=856

Button A: X+34, Y+51
Button B: X+97, Y+45
Prize: X=6689, Y=3702

Button A: X+68, Y+14
Button B: X+12, Y+77
Prize: X=14516, Y=9258

Button A: X+81, Y+26
Button B: X+15, Y+48
Prize: X=6846, Y=3018

Button A: X+81, Y+33
Button B: X+18, Y+31
Prize: X=3618, Y=1971

Button A: X+15, Y+82
Button B: X+45, Y+25
Prize: X=2565, Y=8718

Button A: X+87, Y+28
Button B: X+12, Y+70
Prize: X=3527, Y=11050

Button A: X+36, Y+68
Button B: X+98, Y+37
Prize: X=10586, Y=8295

Button A: X+35, Y+21
Button B: X+17, Y+49
Prize: X=15639, Y=725

Button A: X+11, Y+23
Button B: X+36, Y+16
Prize: X=4346, Y=10486

Button A: X+13, Y+42
Button B: X+51, Y+23
Prize: X=7943, Y=10168

Button A: X+78, Y+68
Button B: X+28, Y+83
Prize: X=2970, Y=5050

Button A: X+39, Y+98
Button B: X+92, Y+32
Prize: X=6342, Y=3388

Button A: X+38, Y+11
Button B: X+71, Y+83
Prize: X=6017, Y=4427

Button A: X+60, Y+37
Button B: X+12, Y+87
Prize: X=3960, Y=8412
"""

results = process_input(input_string)
for result in results:
    print(result)