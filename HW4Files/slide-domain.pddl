
(define (domain slide-domain)
   (:predicates 
   		(location ?l)
		(tile ?t)
		(adj ?l ?l)
		(empty ?l)
		(at ?t ?l))		
		
(:action move
       :parameters  (?t ?from ?to)
       :precondition (and (tile ?t) (location ?to) (location ?from) (adj ?from ?to) (empty ?to) (at ?t ?from) ) 
       :effect (and  (empty ?from) (at ?t ?to)
		     (not (empty ?to)) (not (at ?t ?from)) ) ))

