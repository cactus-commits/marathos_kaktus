### Dropped columns and rows

#### Rows

- `Event distance/length` 
    - missing or invalid unit (`None`, `x`, empty, `6:40`, `07:35`, `71.5`): ~ 1,100 rows total
    -  d (days): 12 190 rows - dropped per instructions

- `Event number of finishers`: drop 10 rows for "Ultra trail Dinarides - King's Race (CRO)" — all rows show 0 finishers, likely cancelled or incorrectly registered event.

- `Athlete age validation`
    - Remove all athletes that were under 10 or over 100 years at the time of the marathon - 284 rows.

- `Athlete gender`
    -  7 null rows 
    -  46 rows with value `X` (possibly non-binary registration, but cannot be confirmed).

- `Athlete country & performance`
    - Remove null rows - 7 rows

#### Columns
- Event distance/length since we split it in to two new kolumns


### Null rows we keep

- **Athlete club**
    - Over 2 miljon rows. No data at all here for races before 2021 which menas they didnt collect it befor then. Another reason for nulls after 2021 can be that all athletes don't belong to a club
    - replaced with "Unknown" since these. rows still hold valuebale info. 

- **Athlete year of birth / Athlete age category**
    - Over half a miljon rows (the null rows for both columns match)
    - We leave these rows as is

#### Split and transform columns

- **Event distance/length** (`"50km"`, `"24h"`)
    - Split in to two new columns 
        - `event_distance_value` → number (ex. `50`)
        - `event_distance_unit` → unit (ex. `km`)



#### Standardisation 

Replaces typos and missing info in the columns below.  This affected a total of ~ 2000 rows

- **Athlete country**
    - `SVE` → `SWE`
    - `GRB` → `GBR`
    - `IRE` → `IRL`
    - `XXX` → `"Unknown" ~ 1700 rows

- **Athlete age category**
    - `F35` → `W35`

Changed text in Athlete country to uppercase to prevent missatch in the future since we had a few rows wheer the country names were with lower cas e(ex. swe etc)


