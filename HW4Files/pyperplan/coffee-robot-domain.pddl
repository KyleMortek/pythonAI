
(define (domain coffee-robot)
   (:requirements :typing)
   (:types room door robot)
   (:predicates	
		(adj ?r1 ?r2 - room)
		(connects ?d - door ?r1 ?r2 - room)
		(isOpen ?d - door)
		(isClosed ?d - door)
		(coffeeInRoom ?r - room)
		(holdCoffee ?r - robot)
		(emptyHand ?rob - robot)
		(at ?rob - robot ?r - room)
		)		

;; Notice how the opening a door that connects two rooms 
;; adds the adjacency predicats in the effect	
(:action open
	:parameters (?d - door ?r1 ?r2 - room ?rob - robot)
	:precondition (and (isClosed ?d) (connects ?d ?r1 ?r2) (at ?rob ?r1) (emptyHand ?rob))
	:effect (and (isOpen ?d) (adj ?r1 ?r2) (adj ?r2 ?r1)  (not (isClosed ?d))) 
)

(:action close
	:parameters (?d - door ?r1 ?r2 - room ?rob - robot)
	:precondition (and (adj ?r1 ?r2) (isOpen ?d)(emptyHand ?rob)(at ?rob ?r1)); (connects ?d ?r1 ?r2) (at ?rob ?r1) (emptyHand ?rob))
	:effect (and (isClosed ?d) (not (isOpen ?d)))
)
(:action move
	:parameters (?r1 ?r2 - room ?rob - robot); ?d - door)
	:precondition (and (at ?rob ?r1)(adj ?r1 ?r2) );(and (isOpen ?d) (at ?rob ?r1) (connects ?d ?r1 ?r2) (adj ?r1 ?r2))
	:effect (and (at ?rob ?r2) (not (at ?rob ?r1))); (adj ?r2 ?r1))
)

(:action grabCoffe
	:parameters (?r - room ?rob - robot)
	:precondition (and (coffeeInRoom ?r) (emptyHand ?rob) (at ?rob ?r) )
	:effect (and (holdCoffee ?rob) (at ?rob ?r)(not(coffeeInRoom ?r)) 
	(not(emptyHand ?rob)))
)

(:action dropOffCoffee;needs to open door. 
	:parameters (?r - room ?rob - robot); ?d - door)
	:precondition (and (holdCoffee ?rob) (at ?rob ?r))
	:effect (and (emptyHand ?rob) (coffeeInRoom ?r)(not(holdCoffee ?rob))(at ?rob ?r))
)


)

