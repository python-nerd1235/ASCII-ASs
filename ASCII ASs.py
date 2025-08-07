code=[]
while 'Q' not in code:
    code.insert(-1,input())
code.remove('Q')
cellpont=0
codepont=0
op=''
cells = [False]*10
for i in cells:
    for b in code:
        b=int(b)
        b-=codepont+len(cells)
        if b==65:
            if i:
                cells[cellpont]=False
            else:
                cells[cellpont]=True
        elif b==83:
            if not i and cells[cellpont-1]:
                cells[cellpont]=False
        elif b==115:
               if i or cells[cellpont-1]:
                    cells[cellpont]=True
        codepont+=1     
    codepont=0
    cellpont+=1
for i in cells:
    print(i)