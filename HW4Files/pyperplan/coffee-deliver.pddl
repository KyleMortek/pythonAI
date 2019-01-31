(define 
   (problem fetch-coffee)
   (:domain coffee-robot)
   (:objects robotRoom livingRoom kitchen bedroom hall - room
	     d1 d2 d3 d4 - door
	     rob - robot
         
  )	

   (:init 

    (at rob robotRoom)
    (emptyHand rob)
    (coffeeInRoom kitchen)
	(connects d1 robotRoom hall)
	(connects d1 hall robotRoom)
	(isClosed d1)
    (connects d3 hall bedroom)
    (connects d3 bedroom hall)
    (isClosed d3)
    (connects d2 hall livingRoom)
    (connects d2 livingRoom hall)
    (isClosed d2)
    (connects d4 livingRoom kitchen)
    (connects d4 kitchen livingRoom)
    (isClosed d4)
    
    
   ;; Rest of inital condition  
   ;;

   ) 
(:goal 
       (and 
       (at rob robotRoom)
       (coffeeInRoom bedroom)
       (emptyHand rob)
       (isClosed d1)
       (isClosed d2)
       (isClosed d3)
       (isClosed d4)
       ;; The goal state goes here
       )

)
)
