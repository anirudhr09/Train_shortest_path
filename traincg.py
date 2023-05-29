import turtle
V = 47
label=[]
def adj_mat(a):

    # STRAIGHT LINES

    for i in range(17):  # green line Cental to ekatuthangal
        a[i][i + 1] = 2
        a[i + 1][i] = 2
    for i in range(17, 33):  # Red line from egmore to tambaram
        a[i][i + 1] = 3
        a[i + 1][i] = 3
    for i in range(33,46):  # Blue line from central to airport
        a[i][i + 1] = 2
        a[i + 1][i] = 2

    # INTER CONNECTIONS

    a[0][17] = 4  # Park to central -G
    a[17][0] = 4

    a[0][33] = 3  # Central G to Cental Blue
    a[33][0] = 3

    a[17][33] = 4  # Park to Central Blue
    a[33][17] = 4

    a[1][18] = 4  # Egmore metro to Egmore
    a[18][1] = 4

    a[24][42] = 4  # Guindy station to Guindy metro
    a[42][24] = 4

    a[16][25] = 4  # St thomas Station to St thomas metro
    a[25][16] = 4
    
    a[28][46] = 4  # Airport metro to Tirusulum 
    a[46][28] = 4

    a[15][43] = 3  # Alandur -B to Alandur -G
    a[43][15] = 3

    # UPDATION OF EDGES

    a[20][21] = 2  # Nungambakkam to Kodambakkam
    a[21][20] = 2
    a[21][22] = 2  # kodambakkam to mambalam
    a[22][21] = 2
    a[44][45] = 3  # Nanganallur to Meenambakkam
    a[45][45] = 3
    a[34][35] = 1  # Govt Estate to LIC
    a[35][34] = 1
    a[35][36] = 1  # LIC to 1000 lights
    a[36][35] = 1
    a[3][4] =1     # Pachaiappas to Kilpauk
    a[4][3] =1
    return a

def print_matrix(a):
    for i in range(47):
        for j in range(47):
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

def printpath(parent, i, mp , src,des):
    if parent[i] == -1:
        return

    printpath(parent, parent[i], mp , src , des)
    #print(i)
    #label.append(src)
    label.append(i+1)
    #label.append(des)
    print(mp[i])

def printSolution(dist, parent, des, mp, src):
    for i in range(V):
        if i == des:
            print("\nTime Taken:", dist[i], "Minutes")
            print("\nPath taken:\n")
            print(mp[src])
            #print()
            printpath(parent, i, mp , src , des)

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
    mp[0] = "Chennai Central metro - G"   #green starts
    mp[1] = "Chennai egmore metro - G"
    mp[2] = "Nehru Park metro"
    mp[3] = "Kilpauk metro"
    mp[4] = "Pachaiappas College metro"
    mp[5] = "Shenoy Nagar metro"
    mp[6] = "Anna Nagar East metro"
    mp[7] = "Anna Nagar Tower metro"
    mp[8] = "Thirumangalam metro"
    mp[9] = "Koyambedu metro"
    mp[10] = "CMBT metro"
    mp[11] = "Arumbakkam metro"
    mp[12] = "Vadapalani metro"
    mp[13] = "Ashok Nagar metro"
    mp[14] = "Ekatuthangal metro"
    mp[15] = "Alandur metro - G"
    mp[16] = "St.Thomas mount metro"
    mp[17] = "Chennai Park"             #Red Starts
    mp[18] = "Chennai Egmore"
    mp[19] = "Chetpet"
    mp[20] = "Nungambakkam"
    mp[21] = "Kodambakkam"
    mp[22] = "Mambalam"
    mp[23] = "Saidapet"
    mp[24] = "Guindy"
    mp[25] = "St.Thomas mount"
    mp[26] = "Palavandhangal"
    mp[27] = "Meenambakkam"
    mp[28] = "Tirusulam"
    mp[29] = "Pallavaram"
    mp[30] = "Chrompet"
    mp[31] = "Tambaram Sanitorium"
    mp[32] = "Tambaram"
    mp[33] = "Chennai central metro - B"  #Blue Starts
    mp[34] = "Government Estate metro"
    mp[35] = "LIC metro"
    mp[36] = "Thousand lights metro"
    mp[37] = "AG-DMS metro"
    mp[38] = "Teynampet metro"
    mp[39] = "Nandanam metro"
    mp[40] = "Saidapet metro"
    mp[41] = "Little mount metro"
    mp[42] = "Guindy metro"
    mp[43] = "Alandur metro - B"
    mp[44] = "Nanganallur metro"
    mp[45] = "Meenambakkam metro"
    mp[46] = "Airport metro"
    
    for i in range(47):
        print(i + 1, ".", mp[i])

def draw_nodes_and_connect(labels):
    turtle.title("Chennai Railway Network")
    turtle.setup(800, 600)
    turtle.bgcolor("black")
    # Set the font and font color
    font = ("Arial", 16, "bold")  # Specify the font type, size, and style

    # Move the turtle to the desired position
    turtle.penup()
    turtle.goto(0, 200)  # Adjust the coordinates as needed
    turtle.pendown()
    turtle.color("white")
    # Write the text
    turtle.write("Chennai Railway Network", align="center", font=font)

    # Function to create a node with number label
    def create_node(color, number):
        turtle.penup()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
        turtle.color("white")
        turtle.goto(turtle.xcor(), turtle.ycor() )
        turtle.write(number, align="center", font=("Arial", 10, "bold"))
        turtle.goto(turtle.xcor(), turtle.ycor() )

    # Function to move turtle to the next position
    def move_to_next_position():
        turtle.penup()
        turtle.goto(turtle.xcor() + 50, turtle.ycor())

    # Function to connect nodes based on labels
    def connect_nodes(labels):
        turtle.speed(1)
        turtle.pensize(3)
        turtle.color("white")
        turtle.penup()

        for i in range(len(labels) - 1):
            turtle.goto(node_positions[labels[i]])
            turtle.pendown()
            turtle.goto(node_positions[labels[i+1]])
            turtle.penup()

    # Set up the turtle
    turtle.speed(0)
    turtle.penup()
    
    # Calculate starting position for green nodes
    num_green_nodes = 17
    start_x_green = -(num_green_nodes * 50) / 2
    start_y_green = 0
    turtle.goto(start_x_green, start_y_green)

    # Create green nodes and store their positions
    turtle.color("green")
    node_positions = {}
    for i in range(1, num_green_nodes + 1):
        node_positions[i] = turtle.position()
        create_node("green", i)
        move_to_next_position()

    # Calculate starting position for red nodes
    num_red_nodes = 16
    start_x_red = -(num_red_nodes * 50) / 2
    start_y_red = -100
    turtle.goto(start_x_red, start_y_red)

    # Create red nodes and store their positions
    turtle.color("red")

    for i in range(1, num_red_nodes + 1):
        node_positions[i + num_green_nodes] = turtle.position()
        create_node("red", i+num_green_nodes)
        move_to_next_position()


    # Calculate starting position for blue nodes
    num_blue_nodes = 14
    start_x_blue = -(num_blue_nodes * 50) / 2
    start_y_blue = -200
    turtle.goto(start_x_blue, start_y_blue)

    # Create blue nodes and store their positions
    turtle.color("blue")
    for i in range(1, num_blue_nodes + 1):
        node_positions[i + num_red_nodes + num_green_nodes] = turtle.position()
        create_node("blue", i + num_red_nodes + num_green_nodes)
        move_to_next_position()

    # Define the array input of labels
    #labels = [1, 4, 7, 11, 15, 16, 18, 21, 24, 27, 29, 32, 35, 38, 40]

    # Connect the nodes based on the array input
    connect_nodes(labels)

    # Exit on click
    turtle.exitonclick()

if __name__ == '__main__':
    area = {}
    src = 0
    des = 0

    print("\n\nFINDING THE FASTEST ROUTE THROUGH METRO/RAILWAYS\n")
    print("------------------------------------------------------------\n\n")

    graph = [[0] * 47 for _ in range(47)]
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
    label.append(src+1)
    dijkstra(graph, src, des, area)
    label.append(des+1)
    draw_nodes_and_connect(label)