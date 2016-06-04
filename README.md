# mobipy
## Purpose
Provide a visualizer for rentability over accomodations

## Requirements
- domain/accomodation/property/property.xlsx : list of properties
- domain/accomodation/rentable/rentable.xlsx : list of rentable (are usually a property, or a part of a property)
- domain/accountancy/lodger.xlsx : list of lodgers (identity, and contract information). If two persons are present in a rentable (whether it's on a single physical contract or not, ie whether they are roommates or a couple), they should be represented as two separate rows (as one can leave the other at any moment). If there are several persons in the same rentable, then each person must have a personal rent value (in the case they don't pay the same amount for different personal_surface).

