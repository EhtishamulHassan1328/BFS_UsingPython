import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

#80000+ nodes
#node_adjlist = nx.read_adjlist('Slashdot0902.txt',create_using=nx.Graph(),nodetype=int)    #reading file in adjecency list


node_adjlist = nx.read_adjlist('facebook_combined.txt',create_using=nx.Graph(),nodetype=int)    #reading file in adjecency list

#if nx.is_weighted(node_adjlist):
    #print("BFS does not work on weigted graphs\n")
    #exit()

#else:
 #   print("\nBFS would work for this Data Set:\n")


visited_nodes = []  #visited nodes list initialized
BFS_queue = []      #BFS queue initialized

file1 = open('BFS_file.txt', 'w')   #writing the output
file2 = open('BFS_queues.txt','w')  #Progress of queues

def BFS(visited_nodes, graph, node): 
  visited_nodes.append(node)        #starting node is added before going into loop
  BFS_queue.append(node)

  while BFS_queue:
    n = BFS_queue.pop(0)
    file2.write("\nNode is poped from BFS queue : ")
    file2.write(str(n))         
    print (n, end = " ")        #output on terminal

    for neighbour_node in graph[n]:
      if neighbour_node not in visited_nodes: #to only add the nodes which are not visited
        file1.write(str(neighbour_node))
        file1.write(" ")

        visited_nodes.append(neighbour_node)    #visited nodes are not checked again (marked)
        BFS_queue.append(neighbour_node)

        file2.write("\nNode is added to visited and BFS queue : ")
        file2.write(str(neighbour_node))
        file2.write(" ")


#main (driver code)
print("Output after running BFS")
BFS(visited_nodes, node_adjlist, 0)
file1.close()       #files are closed           
file2.close()