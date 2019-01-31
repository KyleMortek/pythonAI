
(define (domain slide-domain-grid)
   (:requirements :typing)
   (:types idx tile)
   (:predicates	
		(empty ?r ?c - idx)
		(at ?t - tile ?r ?c - idx)
		(inc ?i  ?j - idx)
		(dec ?i  ?j - idx)
		)		
	
(:action Up
       :parameters  (?t - tile ?rowFrom - idx ?col - idx ?rowTo - idx)
       :precondition (and   (at ?t ?rowFrom ?col) (empty ?rowTo ?col) (dec ?rowFrom ?rowTo)) 
       :effect (and  (empty ?rowFrom ?col) (at ?t ?rowTo ?col)
		     (not (empty ?rowTo ?col)) (not (at ?t ?rowFrom ?col)) ) )

(:action Down
       :parameters  (?t - tile ?rowFrom - idx ?col - idx ?rowTo - idx)
       :precondition (and   (at ?t ?rowFrom ?col) (empty ?rowTo ?col) (inc ?rowFrom ?rowTo)) 
       :effect (and  (empty ?rowFrom ?col) (at ?t ?rowTo ?col)
		     (not (empty ?rowTo ?col)) (not (at ?t ?rowFrom ?col)) ) )

(:action Right ; down pretty sure that parameters is just naming your variables 
       :parameters  (?t - tile ?row - idx ?colFrom - idx ?colTo - idx)
       :precondition (and   (at ?t ?row ?colFrom) (empty ?row ?colTo) (inc ?colFrom ?colTo));(inc ?rowFrom ?rowTo)) 
       :effect (and  (empty ?row ?colFrom) (at ?t ?row ?colTo)
		     (not (empty ?row ?colTo)) (not (at ?t ?row ?colFrom)) ) )

(:action Left ; up similar 
       :parameters  (?t - tile ?row - idx ?colFrom - idx ?colTo - idx)
       :precondition (and   (at ?t ?row ?colFrom) (empty ?row ?colTo) (dec ?colFrom ?colTo)) 
       :effect (and  (empty ?row ?colFrom) (at ?t ?row ?colTo)
		     (not (empty ?row ?colTo)) (not (at ?t ?row ?colFrom)) ) )
)

