def audit_blocklists(list_a, list_b, list_c):
    universal = list_a & list_b & list_c
    redundant = (list_a & list_b) | (list_c & list_b) | (list_a & list_c)
    Unique_A = list_a  - (list_c | list_b) 
    return (universal, redundant, Unique_A)