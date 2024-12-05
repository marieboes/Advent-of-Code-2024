def count_intersecting_mas(grid):
   patterns = ["MAS", "SAM"]
   target_length = len(patterns[0])


   # Dimensions of grid
   rows = len(grid)
   cols = len(grid[0]) if rows > 0 else 0


   def in_bounds(x, y):
       return 0 <= x < rows and 0 <= y < cols


   def find_patterns(x, y, dx, dy, pattern):
       #Check if pattern starts from (x, y) in direction (dx, dy)
       for i in range(target_length):
           if not in_bounds(x + i * dx, y + i * dy) or grid[x + i * dx][y + i * dy] != pattern[i]:
               return False
       return True


   # Positions of 'A'
   positions_first_direction = set()
   positions_opposite_direction = set()


   # Iterate
   for r in range(rows):
       for c in range(cols):
           for pattern in patterns:
               # Check for / (slash)
               if find_patterns(r, c, 1, -1, pattern):
                   positions_first_direction.add((r + 1, c - 1))  # A position


               # Check for \ (backslash)
               if find_patterns(r, c, 1, 1, pattern):
                   positions_opposite_direction.add((r + 1, c + 1))  # A position


   # Calculate intersections
   total_count = len(positions_first_direction & positions_opposite_direction)


   return total_count




if __name__ == "__main__":
   input_data = """
SAMXMAXXAMAMSSSSSMXMAXXMSMMMMASAMXSAMXAMMSMXSAMXSSSSMMMAMXMMMMMSMSMSMMSXXASMXSMSMAAXSSXMXMAMASASAAXXSAMXXMASXMXAMXSSMMSAMXXMXXMAMXMSSSMXXSAS
XMASMSSSXSAXXAXAAXXMAMSASAAMSAXASAMXMMSMAXMAMXMMMMMAASMSSXMASMAMMAAMMASXMMXMASAMMAMXAMXMAXSSXSAMXAASAMXXXMASMASMXMXMAAMSXMMSMMMSAMXAAAXXMXMM
AMXMAAAAASAMMMMSMMMMASMASXMXMASXMAMAMSAMASMSSMMAAXSMMMAXMASASMASXMXMMASAMSAMMMAMSASMXSAXAMAAAMAMASMSXSMSSMAXAMAAAMASMMSAMAAAAAAMMSMMXMMAMASA
SXAMMMMMXMAXXXAXMAMAMXMXMMXSAMMXMSSSXSMMXSAAAMSSMMXXXMMMSAMMSMMXAASMMASMMSASXMMMSASAASMSSSMMSMAMMXASMSMASMASXXSSXSASAMXMASXXXMMSASXSAMAXMAMX
ASXSXXXSAXSAMMSSSMSASMSAASMSASAXSAAXAXXMAMMMSAAXMASMXMXAMASAMAXSSMAXMASAMMAMXXMAXAMMMSMAAAXAAMMMXMAMASMAXMASXAXAXMASXMAXMXMSSMXMASASXSMSXSXS
MMMMMMMAXMXAXAAAAAXAXASXSMAXAMMMMMSMXMAMXSXXXMMSMSSXAMMSSMMAMAMXMAMXMMMAMSSSMMMMSMSXMXMMSMMXXMMXXMMMAXMMSMASMSMMMSXMXMAMMAMAAAXMXMMMXAAMAXAM
XAAAAASMXMSMMMSSMMMSMMMMMMSMSMMAAXAAASXMAMXSMMMSMAMXXXAMAMSXMSAMXSXMMSSMMAMAASAXSXSASASAMASAMSSSMASMSSXMAMAMAAAXAMASAMMXSAMXSMXXSAAASMSMAMAM
SSSSSMSXAMAXAAXMASAMAXMASXMMMAXSAXMMMXAMASASAMXXMASXSSXSAMAAMXASAMAMAAMASMSSMMSMXASMMAMASAMMSAAMSAMXAMXAMAXMSMXMASXMMASASAXXAMAXSXMXSAAMASAM
MAMAMXSMXSMSMMXMXMAXAMMXMAXASMMASXMAMSASASASMMMSMMSAMXASXSMSSSXMASAMSSSXMXXAAAXSMMMMMSMAMAMXMMSMMMSSMSXSXMAMAAXSAMMXXMMASAMSASMMMXMXMXMMAMMM
MMMSMASXXXMAMMMSSXSMMMSSSMMMSAMAAXMAXAAMMMMMMAAAAXMMMMXMASXXAMXAXMMMXXXMMXMSMMSAMXMXAXMMSASAMXAMXAAAAXAMXXXSXSXMASASMXMAMAMSAXAAAASASMSMXSMS
MXAXMASXSMSSXSAAAAMAMAAXXXAASMMMSMMSSMXMMAMASMMSMMAXMMMMMMXSASXMASXSMMMASAMXAMXASMMMASMMSXSXMSXSMMSSMMAMASASAMMSAMXASAMXSSMMXSMMMMSASAAMASAA
SMSSMXSXMASAAMMMXMSAMMXSAXMXSXMAMAAAAXSASASMSAMAAXXMMAMSSXASXMAMAAMAAMSASXXSAMXXSAASAMXASAMXXMAXMAMXMAXSASMMAMAMASAMMSMXMXAMXSXXAXMAMMMSAMMM
XAAMMMMAMMMMMMXXMXMAMXMAMMXAMASAMMMXXMXASASASXMMMSAMMXSAXMMMMSXMSSMSMMMMMMMMMMMMSMMMMMMMMMMXAXMMMXMMXSXMAXXMAMMSAMAXAAMAMSAMAXSXSXMXMAXMAMXX
MMMSAMSAMMAXMASMAXSSMMSMSSMASAMASXSSSSMXMAMAMMSAMAAMSMMMMXAAAXXAXMAMASMMMMXAXXMAMAMAAAAXXXXSMMXAXXMMXMASAMSSXSXMAMXMMMSAMSAMXSSXMASAMSMSSMMS
MAAMMXSMMSXXMAMXMXAASAMXAAXAMASAMMXAAMMAMXMAMAMAMMAMAAMXASMSSXMXSXMXAAAAASMMSSMASASXSSSSMMMXSAMSMSAXSMASAAXAMSASMSSSMXSXMXMXMAXXXXMAMMAAXAMX
SXSSXMXAXSMSSSMSMXSAMMSMSSMXSAMASXMMMMSASMSXMMXSMMAMSSMMXSXAMXSAMAXXXMMSMSAXAASXSXMAAAXAAXAMMXXAASMXAMXSMXXMAMAAAMAAMMMMSMMXSMMSAMXXSMMMSXMX
XAXMXSMMMXAAAAAAAMMSSXMMAMXAMAMAMXAXMASXSASMXSAMASXMMAMXAXMXMASASXMMMXXMAXAMXXSXSXSMASMMSMMSASMMMMXSSSMXXMMXSSSMMMSMMAAAAAAAAAAMAXXAAMAAAMXM
MSMMAAAMAMMMSMMMSXAAMASMMSMMSSMXSSMMSAXAMMMAAMXSAMMASAMMSSSSMXSXMXSAMASMSMSXMASAXMAMXXAXAAMMASMXSXMAAAMSAXMAMXAXMAAASXSSSSMASMMSSMMMMSMSMAMA
MXAMXSSXSAAAXXXXXMMMSAMAXSAXAMXMMAMAMSSMMXMMMSAMXMXASAXSAAAXMXMAMMXASASAAMAASMMAMMXXMXMMMSMMMMMXMASMSMMSAAMMSMMMMSSXMAAMAMMMXMXXXMAAXAAMXSAX
XSXMXXXXMMMSSMSXXMXAMXXSMMSMASXSSXMMSXXMAAXAXMXSSSMMSAMAMXMASMMAMMMXMMSMMMSXMAMXMAMMSSMAAAAMSAMXXMXXAAAMXMMMMAXAXXMXMMMMSMAXMXMMMSSMSXSAXASX
XXSMMMMXMASXMMSAASMMSSMAMSXXMMMAMAMXSXMMSMSASMMAAAXAMXMMXAMSMASASMXSAMXXXXAXSMMXXAAAAAMMSSSMMXMMXSXMMMMSMSXAMMMXXXMXSAAAAMXMMAMAAAAMAAMASAMM
XMAXAAAMAMXAMAMMMMAMAAXAMAAMSASASXMASAXAAXXAAXMXSSMSMSAXSXXAMXXAMAASAMAMSMSXSXSXSMSMSSMXMXMXSMSXAMMSAMXAAXSMMSMMMSMAXXMSSXSASXSMSSSMMSMAXXMA
AXAXSXXXMAXMMAXAASAMSSMSSMSMSASASAMXSAMSSSXSMXMMAMAXAXAMAXSXMAMSMMMSXMASAAXASASMSAAAAXXASAMXMAAMXXAAAXSMSMSMAAAAAXMAMMXXMASAAAMAAAXAXXMMXMAS
SMMXMASXSMSASMMSXSXXXXXXAAMAMAMASXXAMXMMAXAAMASAMMMMSMMMAXSMSMAAAAAXXMMMMSMAMAMAMSMMMSMMMXSAMMMSAMSSMMMAMAXSSSSSSSXAMMASMMMSMXMXMSSSMSASXAAM
MAXASXMAAASMMXAXXMMSMSXSMMMAMAMXMXMASMSMMMSMSASXXSAAXASMXMMAAXMSSMSSMSSXMMMXMMMSMMXMAXMXSASMMSXMXXAAMAMXMMMXMXMAAMMMXAASAMAXMSSXAAAAXSAMSSMS
SXMASAMMMMSAMMXMASAAASXSAMMASMSXAASXMASAMXXAMASMXMMXXAMXMAMXMSAAXXAAAAMASMMXSXAAXMAMSMMAMASAASMSMASMMMSAAXMASAXMMMSASMMMAMASMAAMMMSMMMAMAMXX
AXMXXXMXXXSAMMXSAMSXXSASMMSASMMMSMSASXMAMXMAMXMXSSMSSXMAMMSAAMMAMXSMMMSMMAXAMMSSSSMMXAMXSASMXSAXMXMXXASXSASAXXMMXXSAAXASAMASMMSMSAMXXXAMASAM
SSMSMXMXMASAMMMMMMXSAMXMXAMAXAAAAXSAMMSSMMMAMAAMAAAAMMSXSAMMXMMMSAAASAAASAMASXMAXXMASMMAMASMAMXMMAMMMXSSXXMASMSMSAMXMSMSAMASMXAMMASXSXMSAMXS
XAAAMAXAAAMAMMAMXAXMXMASMSSMSMMMMXMAMMAAASXSSSMMSSMMSASXMASMXSAASXSMMXMXMXSAMXAMXSAAXMASMAMMXSSXMAMXAMMMSXMMMAAAMSMXMAXSAMASXMAXXAMMXAAMMSMA
XMMASMSMSMSMMSMSMXSAMXAXAAAXSASAMMXAMMXSXSAAXAXAMXAAMMSAMAMMASMMSAMXMSSMMMMXMXSXAMMSXSAMMSMSMXMASMSMXAAAAXSAMMMMMXMAXAMSXMASMMMSMAMAXSMAXAXM
SXXXXAAMAMAAMAAMXMAMMMMSAMXMMAMAXSMSSSXXMMMMSSMMSMMMSMXAMSAMMMSMMAMASASAASASXAXMASAXXMASXXAXXXMMXAAXXSMMXMMAMXAASMSMSSXMXMAXAMAAMXMSXMASMMSX
AAASMSSSMSXSSMXMAMXSXSAAAXXXMAMSMXAMAMXXXAAAXAASXMAMXMMAMXAXMASXSAMXMASXMMASAXXXXMMSAMAMAMMMSAMAMSAMXAMMMSSSMSSXSAXMAMAMMSMSSMSMSSXMASAMAMAM
MXMAAXAAAAAAXASMXSAAAMMSMMSMMXXXAMSMAMASMMMXSSMMASASAXXSMSMMMASXSXSAMXMMSMSMMMSSXMASXMASXMAAXMXSXMAMASXMXAAAAXMMMXMMASAMXAAXAAXAMXMSXMASXMAS
SMMMSMSMMMXMMXSAAXMMAMAAAXAAAMAMXMXAXMASAAXAMAXMXMMMXSAAMMMSSMSASAMXSXAAXXMAXAXXSMASXSAMXSXSXXAMXMAMAMAMMMSMMMXMMAXSAMASMMAMMAMSMAASAMXMAMAM
SAAXAAAAAXMXMAMMMMMXXMSMSXSMMMSMASXAMMXSXMMASAMMSSMXAMXMMAAAAAMAMXMASAMMSSSXMMSMXMAXAMSMXMAMMMXXAXMMXXAMAMAMXXAMSSXMXSAMAXSAMSAAMXMSAMASXMMS
SXMSSMSXSXAAMXXMXSMAXXAAXMMXSAASASXSAXXMASMXMMSMAAXMXSSMSMSSMMMXMMMXSAMXXMASMSMASXSMXMAXAMXMXAXMMMMXMMMXMXAXSXMXAMAAXMMMSMXAMXSMMSAMXMAMMSAA
SAXAMXMAMXXXSMMSAAMSSMMSMAXAMAXMXXAAXMSAMXMXSAAMSMMSMXMASAAXAAXAXXXMSAMXSMAMXAASAAMMXMAXSSSMMMSAMASASASASXMMSAMMSSMMMSAAMMSAMAMMAXAMMMXSAAMM
SSMASAMAMMMXXMAMSSMAAAXXAMMXMXXMSMSMSMAMAMXAMXMMAAXAMXMXMASXSMSMMAXAMSMXSXMASMMMMXMAXMSSXAASAASAMXSASASASXMAMXMAMXAAAMMSSMMXMASMMSAMXXMAXMXX
SASAMMSAAMSASMXMAXMXSSMMASMXMSAMXAAAAAMSSXMXSASMXSSXSAXXSXXMXMXXAXMSSXMMSAMXMXXSXMMMSAMAMSMMMXSXMXMAMAMAMAMASMMXSSSMSXXAAXMSMMSAASAMAMMASXMM
SAMXSXSMAMMASXAMSSMXAMXSAMXAAXAAMSMSMSXAAAMAMAXXAMXXXMSMMMMMMAAAXSXXAAAASMMASASAMXAXMAMXMMMASXMASAMXMAMXXXMASXAXXXMAMXMSAMSAAXSMMSAMSXMASASX
MAMMSAXAAXMXMXMAXMMAAXAMXSMSMSMSMXAXXXMMSMMAMXMMSSMSXAAMAAAAMMMMXXMAXMMMSASXSXSMMMSSSSMAXXXAAMAAXASXMXXMSSMASMXMXAMXMAMMAMSSSMSXMMAMMAMXXAMM
SXSAMMMMMSAMXAMMSMSSMMSXMXAAAXAAAMXMMXSXXXSXSMAAAAAMMSMSMSSXSAMAXMMMSMXXSXMASAXXXAMAAAXMASMMSMMMSXMMMMSMAXMASAMMSXMASAXMAMMMMMMAASXMXAMAMSMM
SAMXMXAMSXXMSXSAAMXAMXMAMMSMMMSMSMAXAAXXSAMAMXMMXSMSAAMXAMXXSAXSMSAAAXMASAMAMMMMMMSMSMXAAXXXAXAMAXSAMMAMMXAMXAMAAASASXMSAMXXAAXAMAASMSMSMMAS
MAMMMMAMSASMSMMXSSSMMMSXMAXAMAXMAMAAMMSMMXMAMXXSAAAMMSXSASMMMSMAASMSSSSXMXSXMXMXAAMXAXXMSMMMSSXSSMSAXSAMXXSSSXMMSXMMSXMAMXXMMMSSMSXMAXAXMSAM
SMMAMMMMMAMAMXAAMXAAMAMAMAXAMSMMMMMXSXAXMSSSMSASMMMMAMXAXSMSAXMMMMAXAAMMMASXMAXXMSXSMSXMAAAAASAMXAMAMSMMSMMAMMMXMMMMMMSSSSSSXMAXAMXMAMMMXMAS
SMMMSAASMMMXSXMSSXSMMAXXMSSMMMASXAXAMXMSMXAMAMMXMAMMXSMMXXAMASMXSMMMMMMAMASMSSXSAMMSXMMSSSMSSMMMASMMMXAAAAMAMAXAMASAAMAXAAAASMSMAMMMMSSMMSAM
MAAAMMXMAXSMSAAAMXXMSXMAXXAXAMMAXAMXMAMMMMAMXMXASMSMMAAXSMXMSMAAMAMSAAMSMAMAXAAMXMASAMXAMXXXAAXSAXASXSMSSSSSMMXAXASXSSMMMMMMMMXSMAAAMMAAXMAX
SSMSSSXSAMXASMMMSASMAMSMMSAMXSSMASXMXAMAAXAMXXMXXAAAAXMMXMAMAMMMSAMASMMAMXSSMMMMAXAXAMXMAXAMMMXMASAMAMAMMMXMAXSSMASAMXXAAMAXXSAMXSSXMSSMMSSS
MXMXAAAMXMMMMMAMXMMMXMAXMMSMXAAXSAAASXMSSSSSMAMMMSMXMSXSASAXASXAXMSMXSSSSMMMAAAMSXSMAMSASMMSAAXMAMMMXMAMXXMAMMAAMMMMMXXMMXAAMSASAMMMXMASMXAA
MAMMMMMMASMMSSMMSXXAMSMSMAAMXSMXAMMMAAAXAAAAMXSAAXXAXSASASAMAMMAMXAXAAMASAAASMSMMAXSAMXAXAXSAMSXMMSSXSASXMAAXMXMMASASXSASMXMASAMXAAMXSAMXMSM
SASAMXXSAXAMAAAASMMMMAAAMSMMXAXXMXSMSMMMMMSMMASMSMMSSMAMMMMAMXSASAMMMMSASMMMXAMAMSMSXSMAMMMMSMSAXSAAAXXSAXSMXSMAMMMAAAMAMAMSAMXMXSASXMMMAAAX
XAMXMXMMXMAMSMMMMAAMMMXMMMASAMXSXAXMXMXAXXMMMMSMMMAMXMXMSAMXXMMASMXAAXMASMMAMSMAMAAXASMAMSMAAXSAMMMMMMMSAMXMAAAAMXMMMAMXMXAXXXMXMMAMXAASXSMX
SSSSMASAMSMMMMSXSXMSASAMXSAMAXAMMMSMAMMMSAXAAXXXAMXSXSAMMASXMMMMMXSSSSMXXMAMXMMMXMXMXMXMXAMXXXMXMAXAXSAMXAAMXSXMSXXSAMXMASXSMAXMXMXMSSMSXMXM
AAAXSAMXXAMAAMSASAASAXMSXMMSMMMSSMAMAXAAXMSSSSMMMSMXAXAASXMXMAAAMMMAMAMSMAMMMSASASAMMMSMSMSMSMAASXSMMMMSXSXSMMXSXMASMMAMXSAAMMMSAMAMXMASMMAA
MMMMMSSXXMSSSSMAMMMMSMAAMMMAMSAXAMAMASMSMXAAXXAAAAMMXMMMAMMASASMSAMAMAMAAAMAASASASMSMAAXAXAAAASXSASMSMASXMXSAMMSAMXXASXSAMXMMMAMASXXAMASAXAS
SAMXAMXMXMAAXAMAMXXAMMSMSASAXMASMSMSMAAAAMMSMMSMSMSAMMMMAMSASAMAXMSAXXSSSMSXXMMMMMXAMXXSMSMXMXAMXAXAAMXXAXAXSMASXMMMAMXMXSXMAMMXMMXMXMASMMMM
SMSMASASMMMSMMSSSXMXSAAASASXXSAMXAAAAMSMSXAAAAMAXAXXMAAXAXSASAMSMMSAMXAMAAXMXMAMASMXMSAMAAAASXMMMMMSMSMMSMSMXMASAMAXSMSXMAASMSSXSASMAMXSXASM
MAAXXSASAAAAAXAAMMSAMXMXMAMAXMASMMSMSXXXMMSMMMSMSMMMSSSMSXMAMMAMXMSAMXASMMMSASASASXMAAMMSMSMSASXAAAMAMXMAAXAXXAMMMSAMAXSAMAMAAAAMAMMAMXXMXXX
MSMSXMASMMMSSMMAMAMSASXXMXMXMASMAMXMAXXAMAXAAMAAAAXXAAAMMAMXMMXMMMMMMSMMAAMSASAXXXAXXMXMXMAMSAMMMMMMSAMXMSMMSSSMSAMAMAMMMXSMMMMMMAMSSSSSMMSS
MMAMXSAMXAXMAXXXMXXXXMAXMASMXMMMASASMSMSMASASMMSMMMSAMXMSAMMSXSMAMXSAXXMMMMMAMAMSXSMSXAMASAXMMMXSXMAMMMSXMASAAAAMXSXMAXSAMXAXXXXMMMAAMASAAAA
AMAMXMAXSASXASXSMSMSMXMMSASAMXSSXMASXSAMXMXAMXAMAMXASXMXSAMMSAAXAMSMMSXSASXMMMMMSAAAXMMMAMXMXASAMAMXSAAMASXMMXMMMXMXASASASMXMSMSSSMMSAASMMSS
MMAMAMXMSAMXMMAMAAMAMAXAXXXXAMMASMSMAMMMSAMSMXMSMMASMXMAXAXAMXMSMXAAMAAMMMAAMAXAMMMXMXSMSSSMXXMAMMMXSMMSAMXMXXASAMXMXMASXMMMAAAAAXXMAMXXAXAX
XSSSSSSXXXMASMAMXMXASMSSMSMXSASAMMAMXMAAAAXAAAAMXSXMMXMMMSMSMSXAXSSXMMSMAMMMMSMMSXSXMMXAAAAXMMXMASMMXMXMASAASXMAXAXMXMXMASAXSMMMSMXSXMMSSMMM
MMAAMAMAMXSAMSAMXSXMSAXXASAAAMMASXMSASMSXSMSAMXMAMAMXMASAXXMASMMMXMASXMXASMMMXAAMASAMAMMMSMSXMXXSAAXSXSMAMMSAAMAMMAMXSASXMAMMAAAXMAAAAAAMASA
MMMMMASMMXMSXXMAXSAAMXMMXMAXSMSMMAXMAMAXXMAMXMAMASAMAMMMXSAMXSAMXAXXMASMXMAAXSMMMAXAMXSXMAAXMASXXMSMMSAXAXXMXSMAXSAMMMASAMXMSAMSAMXXXMXMMAMS
XASAMASXXXAMXMXSASMMMMSXXXSAMAAXMXMMSMXMASMMSMXXXMMMASXSASXMAXAMMMMSSMMSMMSMMXMAMMSSMMMMSMSMXAXXXAXAXSMMMSAMAMXAXMMMSMMMMXMMXXSMXSSSMMXSMMMX
SASASXMXMMMSSMAMXSXMAAAMXAXMMSMSSXAAMAXXAMAAXASASMSMAMAMASXXMSSMAAAXAAAXSAMXAASMSMAAAXXAAMAMMMXMMMMSMXXXAMXMAMXSSXSAMAXSAASXXXXAMXAASMASASXS
AAXAMAMAAAASAMXSAMXMSSMMMAMAAMXMAXMASAMXSMMMMSMAXAAMAMAMMMAMMXMASMMSSMMAMXSAMMAXAMXSMMMSXSASASAMAASMMMXMXSASMSAAMAMXSMMSSXMAXSSMSMXMMMASAMAX
MXSAMXSSSMXSAMXMASXMAMXAAAXMMMAXMMMAMMSXMASXMAMXMXMSXMMSXMMSAASMXAMMXAAMMASAMXMSXSMMMSMMASASASAXXXMAAAAXASMSAMMMMAMMAMAMXMMSMMAAAAXSMMASMMMM
XMAMXMXAAXASXSXMMMMAMXXMSMXMMSSXXSXMSAMXSAMASMMXAMXAMMMSAAAXAXSXSAMXSXMASMMMMMXMAMMXAAAMAMAMXXXMSMMXXSXMASMMAMASXXSSMMXSAMAAAXMSMSMAAMAMAAXA
MMMSAAMSMMMXXMASAASXSSXMAMAAMAMMAMAMSASAMASMMXSMSXSASXASXMMSMMSMSASASASMMMAMAXAMMMMMSMSMXMXMSMSMSAASMMMXXMAXSMXAXAXAXAXSAMXMXMXXAAMMMMSSSMSS
AAAAXMAXAAXMSMASMXMSAAXSASXSMAMMAMXMSAMMMAMMMMAAXAMAMMMSXMASAAXASAMASAMMAXAMMSMSAAAAAAAASMMAXAAAMMMMAAAMXSMMAMXMMSXSMSMSAMXMSXSMSMSSXXAAXAXA
XMXSSMMSMMMAAMASMAXMMMMMASXXMASXMMMXMMMSMMXAAAMSMMMXMAXMASASMMSXMXMXMASXMSMSAAASMSMSMMMMAAXMMSMSMMSSSMMSAAXSXMAXAAAXAXASXMAMAASAMXAAMAMSMXMX
MSAMXMAAAXSSMMXSAMMSMAMMAMMXSAMAMXXMASASAMSSXXAXAAAASXXSAMMXMASXXMXMXAMXMAMMMMXMAXAMXMAMXAMXMMXMAAAXAAAMMSMMASMSMMXMAMMMMMSSMSMSSMXXMAXAAAMM
AXXSAMMSSMAAXSAMASAAXXMAMSAAMMSMAXMASMASAMXMSAAMSMSMSXXMASXMMAXXAMASMMMXMAXSSMXMAMXMAXMSMSAMXXAMMMSSSXMMAXASAMMMXSMMAMAMAAAAXXMAXAXMSSSXSXSS
MSMMMSMAMMSMMMASASXMMXXMXMMXSAAXXSAMMMAMAMSASMMXAXXASAXSXMASMXSMASASASMSSSMAAMXXSXMSXMAAAASXMMMSMXMAMXMMSSMMASMMASXSAMASMMMSMSMASXMMAMAMXMAX
XMAAAMMAMMAXXSXMXMAXAMMMSXAMMMXSMMMXXSAXXMMAMXSSMSMAMMAMXMAMXAMMAMMXAMAAAAMXMMSMXAAAXSMMSMXXAAAAMMMMMSAAXMXSAMAMASASMSMSAAXXAXMMXMAMXXAAXMAM
ASMMSSSSSSXSMSAXXXSMXMAMXMMSASXMAAASXSAXSAMSMXMAMMMAMXASAMXSMSSXMSAMSMXMMMMASAXASMMMMSAAXXASXMSMSXAXAMMSSMMMSSXMMMMMXAMXMMSMAMXMASXMSSMSXMAS
MMXXXXAMXMAMASMMSXMAMSSMAMSMAXXSMMXSXMSMAAXXAMSSMASASMMSXSXXAXAAAMMSXAASXSSXSAMMMXXXAMAMMMMSAAAASMMMSXMMAMXAMXXAAMASXMSXXAAAAMASMSAAAAAAXMAS
AMMMMMMMAMAMXMMAXAXAMAXXSSMMSMXXSXXMAMMMSMMMAMAMMMSXMXASMSXMMMMXMXXMMSMSAAAAMXMXMXSMSSXSAMMXMMMMMASAXAMSAMMSMSMSASAMAAXMMSXSASXSAXMMMMSMXMAS
MSSXAAASXSSSMMMSSMSSMASMXAXSAXXAXMASAXAMXMASAMASAMMAMMMMASMMMAXAXMAXAAAMMMMMMSMXMAXAASMSMSMXSSSMXXMASAMXASAXXAXXAMMSMMMXAAAXXXXMMMMSAAAXXMAS
XAAXXMXMXMAXAAAXAXAXMAMXMAMSASMMMSMSSSMMAXASASASAXSAMASMMMAAMSSSSXMAMXXMASAAAMAAMMSMMSMMAAMMMAAMSMMMMXMSMMASXXMSAMXAAAXMMMSMMSMXXAMXXXMSXSAS
MMSSSMAMSMMSSMSSSMMSMASAMAMMAMAXMXAMAMMASMMXAMASAMMASASAASMMSMAMAMSXSMMSAMSMSSSMSAAXAXASXMMXMSMMAAAMXMMAMMSMMAAMAMSSSMSXXXAAAAAXSXSXSMXMXAAS
XXAAASMXXAXAASAMXAAAMASMSSSMASMMXMMMMXSAMAXMMMAMXMSXMMSXMSXSAMXMAMSASMAMMXMXMAMAMMSMMSAMASXAMXXSSSMMXXSASXMASMSAMXAAAXXAMSSMMSSMMAMAMMAMXMMM
MMMSMMXXSXMSSSXMSXMMMXXXAAXXMAMAXXXMMAMXSXMXXMSSMXAMSXXAMXMSAXXMASXMSMASXAXAXMMMMAXAMMASAMSAMXAMXMAMAMMMSXMAMXXAMMMSMMMAMXAMXMXAMAMAMMSXMXAS
XAAMAMMMSAAMAXAXMASXMSXMAMSSSMXSAMMSMMSASMAMMMMAMSAMAMSMMMAMXMSXMAXAMXASMMSSMXAAAMMSMMXMAXAMXMXMASMMASAXMXMAXMMMMSAMAXXAMMSXMASMMMSASXMAXMMM
SMMSAXSAMMXMASAMSMMAAAXSMMSXSXAMMXAAAXMXMAAAAASAMXAMMXAXAMSSSMMASAMMMMXMAXAAASXXXXAMXMMSXMSMSXXSXXXXXXXMXAMMMSASAXASXMMMSAMXSMXMAAMAMXSSMAAM
MAMSAMMASXXMASAMXAXXMMMXAXMAMMSSXMSSMMSSXSMSSMSASXXMXSMSXMAAAAAAMXSXXMMSSMSXMAAXSMSMAMAXAXMAMMXMMMSSSXMAMXSAASMMMXMMMSAXMASMSAASMMSAMAAASMMS
MAMMAMSMMMSMASAMSSMMAXSMXMMAMMAXMXXXXSAMXXAXXAMAMXMAXAXXXMSSSMMXSASASXAAAAASXMXMXAASAMXSMMMAMXAAAXMASMSSMAAMMMMSMXAAASXMSSXAMSMMAMXAMMSMMXMX
SSSSMXMAMSMMASAMAMAMSMSXMXMAXMSSXXAMMMMSMMMMMSMMAXAMMXXMAXAAAASMMMSAMMMXMMXXXMASXSMSMSMSAAXXMMXMSMMMMMAAMMMXSAMAXSSMXMAMSMMMMXXXAMXXXMAXAXSM
XMAXXAMAMXXXMMAMXSAMAAXXAMMSSXMAMMAMAMXAXAAAAXAMASXSAMXMSAMXMASAAAMXMXSSSMMSXMAXMMMSAAASMSMSMXSMMASXSMSSMAXXMAMXXXAXAMSMMAAAASMSASAMXMSMXMAS
XMSMMSSSSSSMMSXSMSXSMSMMSMAXMMSASMSMSSSSSMSMSSXMAMAAMAMAAAXASXXXMXMSSXXAAMASMMSSMSAMSMMXAXAXAASAAMAAMAAMXMMMSXMMMSSMSXXAMSMMXXAAAXMAXMAMXAMX
SMASXAAAAAXAXAAMASMSAMAAMMMMAXMASAMXMAMXAAXMAMXMASXMASMXXMMMSMSMSXMAMSMSMMAXAXXAAMAXXXMAMMAMMMSAMSMMMMMXMAAASAMXASAAMASAMMSXSMSMSMMSASASMSAM
XSAMXMMMMMMSSMSMAMAMAMMMSAXSSMMAMXMXMMMSMMMMASASMSMXMXSSXMAMXAAAMMMAMSMMAMASMMMMMMMMSASMMMXSXXMMASXSAMXASMSXXAMMSXMMMAMXXMAMSAMAXAAXMSASMXAA
XMXSXXAXAXAMAAXXAMXMXMAMXMXMMAMASMSMSXMMMMASASXSXXAXSAMXASMSMMMAMXSSXSASXMAXXAAMMAMXSAMXSXMAXXSXXMAXXXMXSMXXSMMXMMMXMASMSMMSMAMAMMMSXMXXMXAM
MAMAMSMSSSMMMMMSMSMMXMXSAMAMMAMAMAXSAMXAAXMMAMAXXMSMMMSMMMMAXMMAMXSMAMXMAMXXMSSSSMSAMSMAMMSAMMSMAMAMSSMMSAMXAXSAMAAXSXSASAXAMXMAMXAMXMSAMXSM
ASMSXAAAXXAAMAXAMMAMXMASAXAMMSSXMSMSMMSSMSMMSMMMSMAMAAAAMSSMMMSASMSMSMASMMSSMAXXAXMXSAMXSAMASAMSMMMMAAMAXMAMXXMASXMMMAMAMASXSSSMSMMMAXSAXMAA
SXAAAMMMSMSMSMSMXSASAMXSSMMSMAAXMXAMXXMMMXMAAAAAASXXMSSSMASAAAMXMASAASMMSAAAMMSSXMMMXXSAMMSMMMMAMAMMSSMASXXSMASXMMSXMAMAMMXMXMAXAASMXMSXMAXM
XMMMXXAAMXMXAAAMASMMAXAMXSAAMSMMXMAMSMMAMAASMXMXXXMAXXMAMASMMMXSMMMSMSMXMMSMMMAMXMSMSXMASASAMXSAMXXXAAMASASAAXMASXMXMASAMXMAMSSMSSMASAMXASMM
SASMXMMXSAMSMSMSXSMSSMXSAMSSMXAAXSXMAMXAMXXAMMSMSMSXMASXMAMMSXXSAMXXXXAAMMXASMASMMAASMMXMASMMXSMSMMSSSMSSMSAXMSAMXAXXAXAMMASMAXAMAMAMAMXSAAA
MASAMXAAMMMAAAXMASMAAAMMXXMXXXMMAMASMSSMSMMAMXAAXAAMMAMXMMSAMMASAMASASXMSASAMSASAMMSMAMAMXMAMAMMAAAXAAXXXAMAMMXAAXASXMXSAMAXMASMSXMMXSMMMMSS
MMMMXMMSMXSMSMSSMSAMXSMMSMSAXXAXXSAMXMASAAXAMMMMMMMSMAMXXAAAXXAMAMASAMSXXAMAMMMSMMXMAXXAXXMSMASXSSMMSMMSMMMSMXSMSMMAAAAXAMASMXSAXXXAAXMSSMAA
MASXAAAAMMSMAMXMXMXXAXAXAAMAMSSMMMMSASXSSSMSSXAXXXAXASMSMMSMMMMSSMMSASXXMASAMAASASMMMSSSSSMAMXMXAXXAASAMAXAXXXMAXAMSMMMSSMAXMAMMMSMMXSAAXMAX
SASMMMXSXMSAMXAMAMMMASXMASMAMMASAAMSASAXAMAAAXMSAMXSMXMXAMXAXMXAAAXSXMXXXASAMMMSMMAAAMAMAASXSMMSMMMSXMXSXMXSXSMMXXMAAAAAXMSMMASAAXAAMMMMSSSM
MXSAAMMXAMXXXSXXAMAMXSAAXXXXMAASXSXSAMXMMMMMSAMSASAXMASXSMSAMSMSMMMXMMMMMMMMMXXSASMMMMAMSMMSMAAXAAMMASMMMSXMXSAMSSSXMMMMXXXASASMXSMMSMMMAAAX
SXSMMSASAMMSMMMSSSMSASMSSMMMMMMMAMXSXSASXAMMMAXSAMAMSASXAXMAMSAXXSAMAAAASASMSXAXASAMXSMMAXXAMMMSMXXMAMXXAMAXAMAMSAAASMMSAAMAMASMASAMAMAMMSMM
SAMXXMXSXMXAAAAAAMMMASMMAMAASASXAAXXAXAMXAMASMMMSMMMMAXXAMXMXMAMAMMXSMSXXASAAMSMMMMMAAXSASMSSSMMMASMAMMMSSMSMSSMMMMMMAAAMMMAMXMXAXAMASXSMAAA
MAMMXSXMAMSSSMMMMSAMXMASMMSMSASXXMSXMMSMMMMAXAAAAMXXMSMSMAAMMMXMXMMXMAMAMSMXMXMXSAXAMMXSAMAXXMAAMASAMXMAXAAMAAXXAAAAMMMMMASXSXMMMSSMXSXAMXSS
SAMXAMASAMAAMAXSAXAXSSMSXXMASXMASXMASAXASAASMSMSSSMSAMASASXXAMSASMSAMAMMXMAXSXMASXMXMXAMAMXMAXMMMAXAAAMXXSAMMMSSSSSSSSMMSMMXSMSSXAMMASXMMMMM
SMSAAXMASXSSMASXMSSMAMAMMAMMMAMXSASAMXSAMXMXAXAMAAAMAMAMAMMSSSMASXMASAMSAMXMSAMASXASXMMSSMSSSMSSMMSASMMSAMXXMXMAMAAAMMAAMAMAXMAMMMMMXSAMXSAX
MAXMAMXXAXMAMXSAMAMMAMAMAXMAMAMXMAMXSAMXSXMMSMMMMMMMMMMMMMXAMAMAMASAMXSMSSXASAMASXMXAXAAAXAAAAXXAAAAAASMAMAXXAXAMMMMMXMMSXMMSMASXSASXSAMXMMM
SAMXXMASMMSXMASXMAMXAXMSSMSAMXSSMSMMMXSMSAMSAMXMXMXMSAXAXXMSSSMASXMAMSAMXMAXSAMAMAMMMMMXXAMSMMMMXMMMMXMSXMMMSMSMMSMMAAXMSAAAMXMSASASASAMXAAA
MASXSXMASAMAMXSXASXSSXMXXAMMSMAMAAXXMAXASAMAAAMXSAMXSXSMSMAMAASAXAMXXASMSXMMSXMASAMASXMAMSMXAXMASMXMMMAMXAAAAMMAASAMMMSAMXMMSMXMAMAMMXASXMAS
XXAXSAMXMMSAMMMMSXAXAASMMMMAAMAMAMMXMASXSAMXSXMAMAMAMXMAAMMMSMMSSMMAXMASMAMXMASMSASXSAMMSAASMMSSMSMASXMXMXMSSSMMMSAMAAMAMMSAAMAMMMXMAMSAAASX
MXMMSSMSAASXSASXAMMMSMMASAMSSSMSXAAXMASXSXMXXMMMSAMXSAMXMSMAAXAAMXMXMXMMSMMAMXXASXMMSMMSSXXMXAMAMXMASAMXSAAAAXXAAMAMMMSXMAMXAMXSAXASXMMSMMMS
AMXAMMMMMMSXSMSXMASAXAMMSAXAMXAMMMSMMXXMMMSXMASASMSXAXSAAAMXMMMSSXMAAXXXAMXMMXMXMXMASXMMXMSMMMSAMXMASAMASMSMXMSMSSSMSXMMMMSSSMASMMXMAXMASAXX
MXMMSAXXSXSAMAXMXMMMSAMASMMSSMXMASAMXMXAAAXMAMXMXAMXMASMSMXAXXAAMASXXSXSXSAMSMMMXAAMMXMAAAAAAAXAMXMXSXMASAMXAAAAXAAASMSXMSAAAMAMXASAMMMAMMSS
SXSXSMXMMAMAMSMSSSSXMAMMMSAMMAMSMXXXAXMSMMXMSMMSMMMAXAXMMXSSMMMASAMXAMMMAMMXAAXAXSSMAAMXSSSMMSSSSSSMMAMXXAAMMMMSMSMMMAAAXMMSMMAXAAMASXXXSXAX
AASMMXSAMXMMMXAXAAXSMASXAMMMMAMAMSSSMSAMAMSAXXAAXASAMMSMAMMAAASAMXSMMMAMMMSSSSMSAXAMSMSAXXAMXAAXAMAASXMSMMMSAMSMMAAAMSMMMXMXAMXXAXSAMMSMMMMS
MSMAAAXXMMSXMMSMMMMXSASMSMXAMAMXXAAAXMMMAMMAMMSSSXAAAAAMASXSMMMMSMAAASMMXMAAAMAMXSAMAAMMMSMMMMSMMSSMMMAXAAAMAMXASMMSAMAAXAXSSMSMSXMASAAMAAMM
MAMMMSMMMXMASXMAXXSAMXSAAASXMMSSMMSMMSSMSMMMMAXMMMSSMSSXMMXAMXXXAAMSMMAMXXMMMMSMMSXMMSMMAAAMXMMMXXXXAMMMMMMSAMSMMMAMASMMXMMMAMAAXMSXMMMXSXSS
SMAXXMAMSASXMAMSSXMASAMXMMMAASAMAMXXAAXMASAAMXMAAAMAAXAASXSXMAMXSSMAXXAXSMXAAMAAMMMSAAAMSSMMAMAAAMMSMSAAXMAXAXXMASXSAMMAASASMSMSMAAXMASAMMAA
AXMMSSSXAMMXMXMAMXMMMXMAXXMSMMASMMMAMMXSAXXXSXSMMSSMMMMMMAMMMXXAMAMASMSXAMSMSSSXMAAMXSAMXMASXSXSXAAAAMXSMMSSMMSMAMMAAMMXXMASMAXAASMXSAMASMAM
SASXAAMAMXMXSAMXSAXAAASMMXMAXSAMMAXAAXXMAXSMMXSXAAXAAMSMMXMAXMMXMAMXMAAMMMAAXAXASMMSAAMMAMXMAMMXMMSXSMXMMAXAAAXMASXMMMXSAMSMMMSXMAXAMMSSMASX
MXAMMSMSXMSASASASXSMSMMSSXSSMMASMXSMMXSMSMSAAAXMMMSSMMAXMAMMAXAMMSMSMAMMXSMSMASMMASAXMSSXMAMXMSAMMXAMXASMSSSMMSSXMAMAXAAAXMASXMMSMMXSMMASXMX
SXMXXMAMAXMASAMASAXAXAAAXMAXSMXMMXMASMXAAAMAMSXXSAAMAXXXSASMSMMSAAAXAAMMXMSXMXMAXSMSXXMAASXSMXSASAMAXMXSAXAMAXMASXSMAMMSMMMAMXSASASAAASAMXSX
XAXXAMAMAMMAMXMAMXMXMMMMSAXXXXSMSMSAMAMSMSMSMXAAMMXSXMSMMASAAAMMXMSXSXSXAMMMMMSASAAXMAMMMMAAXAMAMXSSMSMMXMAMSXSASXAMXSAXAXSSMAMMSAMSSMMMSAXM
SMMSMSXMMSMSSMMASMMMSSSMMXAMSXSAAAMMSSMAAAAAAMMMMAXMMMAAMXMMMMMSXXMMMAMMSSMAAAMSAMXMASMMXMSMMSSSXMXMMSAASMAMMASAMMSMAXXSMMMAMMSAMAMXXXAAMASA
MAAMXAAAMAMXAXSASAXAAMAASAMXAAMXMMMMXMMXXMSMSMMSXSASASMSMSAMXAAAMMMAMXMSMAMMMMSAMXAAXMAMSAMXAAAAXXAMASMMMMMSMAMAMAXMXSMXMASAMSMXSSMMASMMSASX
SMMXMMMMXAMSSMMASXMMSSSMMXMAMMMAAXXSASMSSXXXAAMMAMXMAMAAXXMASMSXSAMMMAMASAMSMXMAXSMSASAMMAMXMMSMXMXMASASAXSXMMSMMASAMXAXSMSASMAMMXAMXMAXMASX
AXMASXSMSSXMMAMXMAMXMAXMMAMASMSMSAASXMXAAXXXSSMMAMMMSMSMMMXMAMAASMSASASMMXXXAASAMAXAXMAXMAMAMMXXSMAMASAMMSMAXMAMMASMMMMXAXSMMMMMASXMAMXMMAMA
MSSMSAXAAXAASXMSMMSAMAMXSXSAMAAAAMAMXMMXMMSAAAMMASMAXAXXAXAMAMMAMAXAXMMXMMMSSMSAMXXSMSSXSASMXSAMAXMSMMAMXAMSMMSXMASASAMSSMMSMXAMMMSMMSMMMSSM
XAAAMXMMXSMMMMASAASAMSSMMMMMSSMSMMMMAMSMXAXMAMSSMSMXSMMMSXMMAMXMMAMSMSSSMAAMAXXXMAMXAXAXSAMXXXASAAXAMSSMSSSMAAXMMMSASAMXAAAAXMXMAAAMXAASAMXX
AMMMMXXSASASXMAMMMXXMXAAMASAMXAAAXAXAMAXMASXMXMAASAAMAAAMASMSSSXMXSXAXAASMMSSMSSMSMMSMMMMXMSXSXMMXSAXAMXXMAMMMMMSAMXSAMSSMSMSAMSMSMSMSXMASXM
SXSXSAAAAXAMXMASXMSSSXSMMMSASMSMSSMSSMMXSASAMASMMMMSSMMMSAMAXMAASMXMXMSMMSMAXAXMXAAMMMAAMMMAAXMAAASMMASMASXMMSAASASXXAMAMXMAMMMAMAMXXMASAMXA
AMAAMASMSMSMMXAMAAAMXAXXSMXAMAAXXAAAAASAMXXASASXSAMXAMSMMMMMMMSMMAASAXXXAAMMMMMSMSSMAXXMMAAMXMSMMXSASAMMAMXMASAXMASASXMMSAMXMSSXSMMXMSMMMSSS
ASMXMXMXAMMAAMXSMMMSMSMAXAMSMSSMMMMMSMMAMASXMASXSSSXSMMAAXAMAMXMASASMSSMSXSXMXASAAAMXSASXSMXMXAAMAXXMXXMAMASXMSMMXMASAASMMXAMAAXSMSAMXMAMAAA
XXMMSMMSMSMMMSMAXMXAAMMSMSMMAAAMSMMXXXSAMAAAMXMMMMSXMASXMSMSMSAMXMASAAMMAAXASMASMMMMMAAAAXMASMMSMXSMMMSSMSAMAAAXXXMXMMSMAMSMSMMMMASXSAMXMMSS
SASAMXAAXXAAAAMMMSAMXMAAAAAMMMSMAAXASXSAMASXMAAAAASMSAMAAAXAMXMXXMMMMMSMMSMAMMAMAAXXXMMMXMASMXXAXXAAAAMAXAASMMMSAMXXAXXMAXAAAASAMXMMSAMXSXAX
SMMSSMSSSSSMSSXSAMXSSMAMSMSMXMAXSSMXSMSXMMAMSMSSMXSAMXSAASXMASMXAXSAMXXXAXMAMMASXMXSASMXMSXXMAXMSMSSMMSAMSXMASXAMMXMASXSMSMSSSMMXMAMSMMAAMMS    """.strip().splitlines()


   # Strip data
   input_data = [line.strip() for line in input_data]


   result = count_intersecting_mas(input_data)
   print(f"Total intersecting diagonal occurrences of 'MAS': {result}")