V = 40

def adj_mat(a):
    for i in range(13):  # Blue line from central to airport
        a[i][i + 1] = 2
        a[i + 1][i] = 2

    a[0][14] = 3  # Red line from central to egmore
    a[14][0] = 3

    for i in range(14, 26):  # Red line from egmore to tambaram
        a[i][i + 1] = 3
        a[i + 1][i] = 3

    a[19][20] = 0  # Removing saidapet and st.thomas mount edge
    a[20][19] = 0
    a[19][9] = 3  # saidapet to guindy
    a[9][19] = 3
    a[9][20] = 3  # guindy to st.thomas mount
    a[20][9] = 3
    a[22][23] = 0  # remove meenambakam to pallavaram
    a[23][22] = 0
    a[22][13] = 2  # meenambakam to airport (tirusulam)
    a[13][22] = 2
    a[13][23] = 3  # airport to pallavaram
    a[23][13] = 3

    a[14][27] = 2  # green line egmore to nehru park metro
    a[27][14] = 2

    for i in range(27, 38):  # green line nehru park to ekatuthangal
        a[i][i + 1] = 2
        a[i + 1][i] = 2

    a[33][34] = 3  # Thirumangalam to Koyambedu
    a[34][33] = 3
    a[38][39] = 3  # Ashoknagar to ekkatuthangal - 3 mins
    a[39][38] = 3
    a[39][10] = 2  # ekatuthangal to alandur
    a[10][39] = 2
    a[10][20] = 2  # alandur to St.Thomas mount
    a[20][10] = 2

    return a

def print_matrix(a):
    for i in range(40):
        for j in range(40):
            print(a[i][j], end=' ')
        print()

def minDistance(dist, sptSet):
    min1 = float('inf')
    min_index = 0

    for v in range(V):
        if not sptSet[v] and dist[v] < min1:
            min1 = dist[v]
            min_index = v

    return min_index

def printpath(parent, i, mp):
    if parent[i] == -1:
        return

    printpath(parent, parent[i], mp)
    print(i)

def printSolution(dist, parent, des, mp, src):
    for i in range(V):
        if i == des:
            print("\nTime Taken:", dist[i], "Minutes")
            print("\nPath taken:\n")
            print(mp[src])
            print()
            printpath(parent, i, mp)

def dijkstra(a, src, des, mp):
    dist = [float('inf')] * V
    sptSet = [False] * V
    parent = [-1] * V

    dist[src] = 0

    for count in range(V - 1):
        u = minDistance(dist, sptSet)
        sptSet[u] = True

        for v in range(V):
            if not sptSet[v] and a[u][v] > 0 and dist[u] != float('inf') and dist[u] + a[u][v] < dist[v]:
                dist[v] = dist[u] + a[u][v]
                parent[v] = u

    printSolution(dist, parent, des, mp, src)

def mapped(mp):
    mp[0] = "Chennai Central"
    mp[1] = "Government Estate metro"
    mp[2] = "LIC metro"
    mp[3] = "Thousand lights metro"
    mp[4] = "AG-DMS metro"
    mp[5] = "Teynampet metro"
    mp[6] = "Nandanam metro"
    mp[7] = "Saidapet metro"
    mp[8] = "Little mount metro"
    mp[9] = "Guindy"
    mp[10] = "Alandur metro"
    mp[11] = "Nanganallur metro"
    mp[12] = "Meenambakkam metro"
    mp[13] = "Airport"
    mp[14] = "Egmore"
    mp[15] = "Chetpet"
    mp[16] = "Nungambakkam"
    mp[17] = "Kodambakkam"
    mp[18] = "Mambalam"
    mp[19] = "Saidapet"
    mp[20] = "St.Thomas mount"
    mp[21] = "Palavandhangal"
    mp[22] = "Meenambakkam"
    mp[23] = "Pallavaram"
    mp[24] = "Chrompet"
    mp[25] = "Tambaram Sanitorium"
    mp[26] = "Tambaram"
    mp[27] = "Nehru Park metro"
    mp[28] = "Kilpauk metro"
    mp[29] = "Pachaiappas College metro"
    mp[30] = "Shenoy Nagar metro"
    mp[31] = "Anna Nagar East metro"
    mp[32] = "Anna Nagar Tower metro"
    mp[33] = "Thirumangalam metro"
    mp[34] = "Koyambedu metro"
    mp[35] = "CMBT metro"
    mp[36] = "Arumbakkam metro"
    mp[37] = "Vadapalani metro"
    mp[38] = "Ashok Nagar metro"
    mp[39] = "Ekatuthangal metro"

    for i in range(40):
        print(i + 1, ".", mp[i])

if __name__ == '__main__':
    area = {}
    src = 0
    des = 0

    print("\n\nFINDING THE FASTEST ROUTE THROUGH METRO/RAILWAYS\n")
    print("------------------------------------------------------------\n\n")

    graph = [[0] * 40 for _ in range(40)]
    adj_mat(graph)
    # print_matrix(graph)
    
    mapped(area)

    print("------------------------------------------------------------\n")
    src = int(input("Enter the boarding station number:")) - 1
    des = int(input("Enter the destination station number:")) - 1

    print("------------------------------------------------------------\n\n")
    
    if area.get(src) is None:
        print("Oops! invalid Source")
        exit()
    
    if area.get(des) is None:
        print("Oops! invalid Destination")
        exit()
    
    dijkstra(graph, src, des, area)
