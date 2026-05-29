#### Dropped


- `Event distance/length` 
    - missing or invalid unit (`None`, `m`, `x`, empty, `6:40`, `07:35`, `71.5`): ~1,100 rows total
    -  d (days): 12 190 rows - dropped per instructions

- `Event number of finishers`: drop 10 rows for "Ultra trail Dinarides - King's Race (CRO)" — all rows show 0 finishers, likely cancelled or incorrectly registered event.

- `Athlete age validation`
    - Rows where `year_of_event - year_of_birth` < 10 or > 100: 284 rows.

- `Athlete gender`
    -  7 null rows → drop
    -  46 rows with value `X` → drop (possibly non-binary registration, but cannot be confirmed).

- `Athlete country & performance`
    - `Athlete country`: 3 nulls
    - `Athlete performance`: 2 nulls


