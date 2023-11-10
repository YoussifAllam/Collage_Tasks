import networkx as nx
import matplotlib.pyplot as plt

class labeling : 
    labels = {}
    
    def draw_graph(self, graph:nx.graph , labels , pos):
        if pos == None:
            pos = nx.spring_layout(graph)
        nx.draw(graph, node_size=1000  ,node_shape='8',labels=labels ,pos = pos )
        plt.show()
        
        
    def get_longest_path_length_or_Diameter (self , Graph , start_node , target ):
        all_paths = nx.all_simple_paths(Graph, start_node , 'D')
        return len(min(all_paths , key=len))


    def check_if_label_is_Valid(self ,  U_Label , V_Label ,  diameter , destance_between_U_V ):
        First_Term  = abs(V_Label - U_Label )
        Second_Term = (diameter + 1) - destance_between_U_V
        if First_Term >= Second_Term and V_Label not in labeling.labels.values() :
            return True
        else: return False
        
        
    def get_correct_label(self ,  node_list , node_index , V_Label , diameter , labels) :
        V_Label+=1
        for  i in range (node_index , 0 , -1  ):
            cur_node_letter = node_list[node_index]
            last_node_letter = node_list[node_index-1]
            V_Label = labels[cur_node_letter]
            U_Label = labels[last_node_letter]
            destance_between_U_V = len(nx.shortest_path(G ,cur_node_letter , last_node_letter ))
            
            while not self.check_if_label_is_Valid(U_Label , V_Label ,diameter , destance_between_U_V):
                V_Label+=1
                pass
            return V_Label


    def radio_labeling(self , G : nx.Graph ): 
        for v in G.nodes():
            labeling.labels[v] = 0 
            
        diameter  = self.get_longest_path_length_or_Diameter(G2 , start_node = 'A', target = 'D')
        print(diameter)
        node_list = list(G.nodes()) 
        
        for i in range(1 ,  len(node_list) ):
            node_letter = node_list[i]
            correct_V_Label = self.get_correct_label( node_list , node_index = i , V_Label = labeling.labels[node_letter] , diameter= diameter, labels = labeling.labels )
            labeling.labels[node_letter] = correct_V_Label
        return labeling.labels
    
  
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')])

G2 = nx.Graph()
G2.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])

all_paths = nx.all_simple_paths(G, 'A' , 'D')
# print(max(all_paths , key=len))
# for path in all_paths:
#     print(path , len(path))

obj = labeling()
if obj.radio_labeling is None:
   print("No radio labeling exists for the given graph.")
else:
   labels = obj.radio_labeling(G2)
   for key , value in labels.items():
       labels[key]=f'{key} {value}'
   pos  = {'A': (0, 0), 'B': (0, 1), 'C': (1, 1), 'D': (1, 0)} 
   # pos = None
   obj.draw_graph(G2,labels ,pos)