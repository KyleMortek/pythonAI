''' 
Nils Napp
Sliding Probelm for AI-Class
'''

from slideproblem import * 
import time
## you likely need to inport some more modules to do the serach


class Searches:
    
                
    def h_1(self,s0: State,sf: State ) -> numbers.Real:
        return "something"
        
    def h_2(self,s0: State,sf: State ) -> numbers.Real:
        return "somethign"
        
    def a_star_tree(self,problem : Problem) -> tuple:
        return "Totally fake return value"
        
    def a_star_graph(self,problem : Problem) -> tuple:
        return "Not really the right format for Solution"


if __name__ == '__main__':

    import time
    
    p=Problem()
    s=State()
    n=Node(None,None, 0, s)
    n2=Node(n,None, 0, s)
    
    searches = Searches()
    
    
    si=State()
    
    
    # change the number of random moves appropriately
    # The longes solution is 31 moves, see if you can find a solution >=30 moves. 
    # Pleaes post them if you find them!
    print(si)
    apply_rnd_moves(15,si,p)
    p.initialState=si
    
    print(si)
    
    
    startTime=time.clock()
    
        
    print('\n\n=== A*-Tree ===\n')
    startTime=time.clock()
    res=searches.a_star_tree(p)
    print(time.clock()-startTime)
    print(Node.nodeCount)
    print(res)
    
    print('\n\n=== A*-Graph ===\n')
    startTime=time.clock()
    res=searches.a_star_graph(p)
    print(time.clock()-startTime)
    print(Node.nodeCount)
    print(res)

