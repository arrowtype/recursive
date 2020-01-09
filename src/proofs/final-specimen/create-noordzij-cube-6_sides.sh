#/bin/bash

src venv/bin/activate

#   CUBE CONSTRUCTION                                         
#                                                             
#                 |––––––-----|                               
#                 |           |                               
#                 |  5. top   |                               
#                 |           |                               
#                 |––––––-----|                               
#   |––––––-----| |––––––-----| |––––––-----| |––––––-----|   
#   |           | |           | |           | |           |   
#   |  4. left  | |  1. frnt  | |  2. rght  | |  3. back  |   
#   |           | |           | |           | |           |   
#   |––––––-----| |––––––-----| |––––––-----| |––––––-----|   
#                 |––––––-----|                               
#                 |           |                               
#                 |  6. bttm  |                               
#                 |           |                               
#                 |––––––-----|                               
#                                                             


# define basic vars here, so you don't repeat yourself
mono=0
rows=6
cols=4
lttr="rw"

# do not edit; this calls the drawbot script
cube="python src/proofs/final-specimen/create-flattened-noordzij-cube_side.py"

echo "                                                                          "
echo "                                                                          "
echo "                                                                          "
echo "                                                                          "
echo "                                                                          "
echo "               – – –  C A S L  – – –                                      "
echo "             T |                 T |    M                                 "
echo "           H   |               H   |           O                          "
echo "         G     |             G     S                   N                  "
echo "       W       |           W       L                           O          "
echo "     – – –  C A S L  – – –         N           – – –  C A S L  – – –      "
echo "     |         |         |         T         T |                 T |      "
echo "     |         |         |         |       H   |               H   |      "
echo "     S         |         S         |     G     |             G     S      "
echo "     L         – – – –   L   – – – –   W       |           W       L      "
echo "     N       T           N        T  – – –  C A S L  – – –         N      "
echo "     T     H             T      H    |         |         |         T      "
echo "     |   G               |    G      |         |         |         |      "
echo "     | W                 |  W        S         |         S         |      "
echo "     – – –  C A S L  – – –           L         – – – –   L   – – – –      "
echo "         M                           N       T           N        T       "
echo "                O                    T     H             T      H         "
echo "                        N            |   G               |    G           "
echo "                                O    | W                 |  W             "
echo "                                     – – –  C A S L  – – –                "
echo "                                                                          "
echo "                                                                          "
echo "                                                                          "
echo "                                                                          "


# # side 1, "front": 
# $cube --fileTag 01_front --rows 6 --cols 4 -l rw --xVar slnt --yVar CASL --aXasc True  --bYasc True  --MONOVal    0 --wghtVal 1000
# # side 2, "right": 
# $cube --fileTag 02_right --rows 6 --cols 4 -l rw --xVar wght --yVar CASL --aXasc False --bYasc True  --MONOVal    0 --slntVal -15
# # side 3, "back": 
# $cube --fileTag 03_back --rows 6 --cols 4 -l rw --xVar slnt --yVar CASL --aXasc False --bYasc True  --MONOVal    0
# # side 4, "left": 
# $cube --fileTag 04_left --rows 6 --cols 4 -l rw --xVar wght --yVar CASL --aXasc True  --bYasc True  --MONOVal    0
# # side 5, "top": 
# $cube --fileTag 05_top --rows 6 --cols 4 -l rw --xVar slnt --yVar wght --aXasc True  --bYasc False --MONOVal    0 --CASLVal 1
# # side 6, "bottom": 
# $cube --fileTag 06_bottom --rows 6 --cols 4 -l rw --xVar slnt --yVar wght --aXasc True  --bYasc True  --MONOVal    0


# -------------------------------------------------------------------------------------------------------------------------------------------
# 

#                         | * 1 - C A S L - 0 * |                                                 
#                         | 0                 0 |                                                 
#                         | |                 | |                                                 
#                         | sl               sl |                                                 
#                         | nt               nt |                                                 
#                         | |                 | |                                                 
#                         | 1                 1 |                                                 
#                         | * 1 - C A S L - 0 * |                                                 
#     * 0 - w g h t - 1 * | * 1 - C A S L - 0 * | * 1 - w g h t - 0 * | * 0 - C A S L - 1 * |     
#     0                 0 | 0                 0 | 0                 0 | 0                 0 |     
#     |                 | | |                 | | |                 | | |                 | |     
#     sl               sl | sl               sl | sl               sl | sl               sl |     
#     nt               nt | nt               nt | nt               nt | nt               nt |     
#     |                 | | |                 | | |                 | | |                 | |     
#     1                 1 | 1                 1 | 1                 1 | 1                 1 |     
#     * 0 - w g h t - 1 * | * 1 - C A S L - 0 * | * 1 - w g h t - 0 * | * 0 - C A S L - 1 * |     
#                         | * 1 - C A S L - 0 * |                                                 
#                         | 0                 0 |                                                 
#                         | |                 | |                                                 
#                         | sl               sl |                                                 
#                         | nt               nt |                                                 
#                         | |                 | |                                                 
#                         | 1                 1 |                                                 
#                         | * 1 - C A S L - 0 * |                                                 



echo "                                                                          "
echo "                                                                          "
echo "                                                                          "
echo "                                                                          "
echo "                                                                          "
echo "               – – –  C A S L  – – –                                      "
echo "             T |                 T |    M                                 "
echo "           H   |               H   |           O                          "
echo "         G     |             G     S                   N                  "
echo "       W       |           W       L                           O          "
echo "     – – –  C A S L  – – –         N           – – –  C A S L  – – –      "
echo "     |         |         |         T         T |                 T |      "
echo "     |         |         |         |       H   |               H   |      "
echo "     S         |         S         |     G     |             G     S      "
echo "     L         – – – –   L   – – – –   W       |           W       L      "
echo "     N       T           N        T  – – –  C A S L  – – –         N      "
echo "     T     H             T      H    |         |         |         T      "
echo "     |   G               |    G      |         |         |         |      "
echo "     | W                 |  W        S         |         S         |      "
echo "     – – –  C A S L  – – –           L         – – – –   L   – – – –      "
echo "         M                           N       T           N        T       "
echo "                O                    T     H             T      H         "
echo "                        N            |   G               |    G           "
echo "                                O    | W                 |  W             "
echo "                                     – – –  C A S L  – – –                "
echo "                                                                          "
echo "                                                                          "
echo "                                                                          "
echo "                                                                          "

# TODO: consider if there were just XYZ axes. 

# -x CASL -y wght -z slnt --Xasc True --Xasc True --Zasc True

# then, python would just run through each of the 6 sequences needed and piece the final flat box together

# probably also useful: labels on/off

#      –––––––    
#     /     / |   
#  ↑ –––––––  |   
#  z |     | /  ↗ 
#    –––––––  y   
#      x →        


#   CUBE CONSTRUCTION                                         
#                                                             
#   |––––––-----|                                             
#   |           |                                             
#   |  5. top   |                                             
#   |           |                                             
#   |––––––-----|                                             
#   |––––––-----| |––––––-----| |––––––-----| |––––––-----|   
#   |           | |           | |           | |           |   
#   |  1. frnt  | |  2. rght  | |  3. back  | |  4. left  |   
#   |           | |           | |           | |           |   
#   |––––––-----| |––––––-----| |––––––-----| |––––––-----|   
#   |––––––-----|                                             
#   |           |                               _______    
#   |  0. bttm  |                              /  5  / |      
#   |           |                           ↑ ––––––/ 2|      
#   |––––––-----|                           z |  1  | /  ↗    
#                                             _______/ y      
#                                               x →           
#                                                             





# side 1, "front": 
$cube --MONOVal $mono --rows $rows --cols $cols -l $lttr --fileTag 01_front  --xVar CASL --aXasc False --yVar slnt --bYasc False --wghtVal 1000
# side 2, "right": 
$cube --MONOVal $mono --rows $rows --cols $cols -l $lttr --fileTag 02_right  --xVar wght --aXasc False --yVar slnt --bYasc False
# side 3, "back": 
$cube --MONOVal $mono --rows $rows --cols $cols -l $lttr --fileTag 03_back   --xVar casl --aXasc False --yVar slnt --bYasc False
# side 4, "left": 
$cube --MONOVal $mono --rows $rows --cols $cols -l $lttr --fileTag 04_left   --xVar wght --aXasc True  --yVar slnt --bYasc False
# side 5, "top": 
$cube --MONOVal $mono --rows $rows --cols $cols -l $lttr --fileTag 05_top    --xVar CASL --aXasc False --yVar wght --bYasc False 
# side 6, "bottom": 
$cube --MONOVal $mono --rows $rows --cols $cols -l $lttr --fileTag 06_bottom --xVar CASL --aXasc False --yVar wght --bYasc True  --slntVal -15





