(define (problem 3x3test)
 (:domain slide-domain-grid)
 (:objects 1 2 3 - idx
 tile1 tile2 tile3 tile4 tile5 tile6 tile7 tile8 - tile)
 (:init
 ;; inc and dec
 (inc 1 2) (inc 2 3) (dec 3 2) (dec 2 1)
 ;; board after applying 100 random moves solution length=27
 ;; a difficult state
 ;; [4, 7, 1]
 ;; [0, 8, 6]
 ;; [2, 5, 3]
 	;; [3, 1, 5]
	;; [6, 7, 2]
	;; [4, 0, 8]
 (at tile3 1 1) (at tile1 1 2) (at tile5 1 3)
 (at tile6 2 1) (at tile7 2 2) (at tile2 2 3)
 (at tile4 3 1) (empty 3 2) (at tile8 3 3))

 (:goal (and (empty 1 1) (at tile1 1 2) (at tile2 1 3)
 (at tile3 2 1) (at tile4 2 2) (at tile5 2 3)
 (at tile6 3 1) (at tile7 3 2) (at tile8 3 3) ))
 
 )



; (define (problem 3x3test)
;    (:domain slide-domain-grid)
;    (:objects 1 2 3 - idx
; 	tile1 tile2 tile3 tile4 tile5 tile6 tile7 tile8 - tile)
;    (:init 



	;; inc and dec predicates !!
	;; you need to define these operations in logic




	;; (SUBMIT THIS ONE) board after applying 35 random moves solution length=15 ... a medium difficulty state
	;; [3, 1, 5]
	;; [6, 7, 2]
	;; [4, 0, 8]



	;; board after applying 100 random moves solution as length=27 ... a difficult state
	;; [4, 7, 1]
	;; [0, 8, 6]
	;; [2, 5, 3]

; )
;    (:goal (and 
	
; 	   )
; ))
