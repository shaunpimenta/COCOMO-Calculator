# A Effort coefficient that can be calibrated, currently set to 2.94
# Version 2.1 72
# © 1995 – 2000 Center for Software Engineering, USC
# AT Percentage of the code that is re-engineered by automatic translation
# ATPROD Automatic translation productivity
# B Scaling base-exponent that can be calibrated, currently set to 0.91
# E Scaling exponent described in Section 3.1
# EM 17 Effort Multipliers discussed in Section 3.2.1
# PM Person-Months effort from developing new and adapted code
# PMAuto Person-Months effort from automatic translation activities discussed in Section 2.6.
# SF 5 Scale Factors discussed in Section 3.1
# Post Architecture Model
B=0.91
A=2.94
def postarchitecture(Sf,Adapted_SLOC,At,ATPROD,size,em,A=2.94,B=0.91,):
    E=B+(0.01*Sf)
    pm_auto=(Adapted_SLOC*(At/100))/ATPROD
    pm = A*((size)**E)*em+pm_auto
    return [E,pm]

def earlydesign(size,Sf,em,Adapted_SLOC,At,ATPROD,A=2.94,B=0.91):
    E = B + (0.01 * Sf)
    pm_auto = (Adapted_SLOC * (At / 100)) / ATPROD
    pm = A * ((size) ** E) * em + pm_auto
    return [E,pm]