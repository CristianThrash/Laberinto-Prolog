infile = open('Laberinto.txt', 'r')
lista = []
for line in infile:
    lista = lista+[line]

for i in range(0,len(lista)-1):
    for j in range(0,len(lista[i])-1):
        if(lista[i][j]==lista[i][j+1]=="0"):
            print ("conecta("+str(i)+str(j)+","+str(i)+str(j+1)+").")
        if(lista[i][j]=="0" and lista[i][j+1]=="X"):
            print ("conecta("+str(i)+str(j)+",x).")
        if(lista[i][j]=="X" and lista[i][j+1]=="0"):
            print ("conecta(x,"+str(i)+str(j+1)+").")
        if(lista[i][j]=="0" and lista[i][j+1]=="Y"):
            print ("conecta("+str(i)+str(j)+",y).")
        if(lista[i][j]=="Y" and lista[i][j+1]=="0"):
            print ("conecta(y,"+str(i)+str(j+1)+").")

for i in range(0,len(lista[0])-1):
    for j in range(0,len(lista)-1):
        if(lista[j][i]==lista[j+1][i]=="0"):
            print ("conecta("+str(j)+str(i)+","+str(j+1)+str(i)+").")
        if(lista[j][i]=="0" and lista[j+1][i]=="X"):
            print ("conecta("+str(j)+str(i)+",x).")
        if(lista[j][i]=="X" and lista[j+1][i]=="0"):
            print ("conecta(x,"+str(j+1)+str(i)+").")
        if(lista[j][i]=="0" and lista[j+1][i]=="Y"):
            print ("conecta("+str(j)+str(i)+",y).")
        if(lista[j][i]=="Y" and lista[j+1][i]=="0"):
            print ("conecta(y,"+str(j+1)+str(i)+").")
