import arithmetic_arranger as a

calculations = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]

#["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
#["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]


# validate list meets criteria
a.validations(calculations=calculations)

#run function
a.arithmetic_arranger(calculations=calculations,show_answer=True)