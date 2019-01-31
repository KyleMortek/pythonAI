(define (problem 3x3test)
   (:domain slide-domain)
   (:objects loc1 loc2 loc3 loc4 loc5 loc6 loc7 loc8 loc9
	tile1 tile2 tile3 tile4 tile5 tile6 tile7 tile8)
   (:init (location loc1)
	(location loc2)
	(location loc3)
	(location loc4)
	(location loc5)
	(location loc6)
	(location loc7)
	(location loc8)
	(location loc9)

	(tile tile1)
	(tile tile2)
	(tile tile3)
	(tile tile4)
	(tile tile5)
	(tile tile6)
	(tile tile7)
	(tile tile8)
	

;;  Predicates for following board confiburaiton
;;  adj is not symmetric, so both need to be added 
;;
;;  loc1  | loc2 | loc3
;;  --------------------
;;  loc2  | loc5 | loc6
;;  -------------------
;;  loc7 | loc 8 |loc9


	(adj loc1 loc2)        
	(adj loc2 loc1)        

	(adj loc2 loc3)        
	(adj loc3 loc2)

	(adj loc1 loc4)        
	(adj loc4 loc1)

	(adj loc2 loc5)        
	(adj loc5 loc2)        
        
	(adj loc3 loc6)        
	(adj loc6 loc3)        

	(adj loc5 loc4)        
	(adj loc4 loc5)

       	(adj loc5 loc6)        
	(adj loc6 loc5)        

	(adj loc4 loc7)        
	(adj loc7 loc4)        

	(adj loc5 loc8)        
	(adj loc8 loc5)        

	(adj loc6 loc9)        
	(adj loc9 loc6)

	(adj loc7 loc8)        
	(adj loc8 loc7) 

	(adj loc8 loc9)        
	(adj loc9 loc8) 

	
	;; board after applying 100 random moves solution length=27 ... a difficult state
	;; [4, 7, 1]
	;; [0, 8, 6]
	;; [2, 5, 3]

;;	(at tile4 loc1)
;;	(at tile7 loc2)
;;	(at tile1 loc3)
;;	(empty loc4)
;;	(at tile8 loc5)
;;	(at tile6 loc6)
;;	(at tile2 loc7)
;;	(at tile5 loc8)
;;	(at tile3 loc9)

	;; board after applying 35 random moves solution length=15 ... a medium difficulty state
	;; [3, 1, 5]
	;; [6, 7, 2]
	;; [4, 0, 8]


	(at tile3 loc1)
	(at tile1 loc2)
	(at tile5 loc3)
	(at tile6 loc4)
	(at tile7 loc5)
	(at tile2 loc6)
	(at tile4 loc7)
	(empty loc8)
	(at tile8 loc9)


)
   (:goal (and 
	(empty loc1)
	(at tile1 loc2)
	(at tile2 loc3)
	(at tile3 loc4)
	(at tile4 loc5)
	(at tile5 loc6)
	(at tile6 loc7)
	(at tile7 loc8)
	(at tile8 loc9)
	
)))
