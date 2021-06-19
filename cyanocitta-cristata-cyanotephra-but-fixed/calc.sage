enc = [(26, 66, 70314326037540683861066), (175, 242, 1467209789992686137450970), (216, 202, 1514632596049937965560228), (13, 227, 485439858137512552888191), (1, 114, 112952835698501736253972), (190, 122, 874047085530701865939630), (135, 12, 230058131262420942645110), (229, 220, 1743661951353629717753164), (193, 81, 704858158272534244116883)]
A = Matrix([[enc[0][0]^2,enc[0][1]^2,enc[0][0]*enc[0][1],enc[0][0],enc[0][1],1], [enc[1][0]^2,enc[1][1]^2,enc[1][0]*enc[1][1],enc[1][0],enc[1][1],1], [enc[2][0]^2,enc[2][1]^2,enc[2][0]*enc[2][1],enc[2][0],enc[2][1],1],[enc[3][0]^2,enc[3][1]^2,enc[3][0]*enc[3][1],enc[3][0],enc[3][1],1],[enc[4][0]^2,enc[4][1]^2,enc[4][0]*enc[4][1],enc[4][0],enc[4][1],1],[enc[5][0]^2,enc[5][1]^2,enc[5][0]*enc[5][1],enc[5][0],enc[5][1],1]])
E = Matrix([[enc[0][2]],[enc[1][2]],[enc[2][2]],[enc[3][2]],[enc[4][2]],[enc[5][2]]])
print((A^-1)*E)