# FFWTT Ligue Confinement MEGA SUIVI GENERATOR

## Quick Start

- This script requires `python` (it has been tested on 3.7.5)

- `python build.py > tableau.html`

It uses input.txt to produce as an output a table with every game played in the
[FFWTT Wiki's](http://www.ffwtt.net/wiki/index.php?title=Accueil) syntax.

The table is read by line : the players are in line and their opponents are
in column.


## input.txt format

- Lines starting with`//` are comments
- `PlayerName (Job)` declares a player with the given job. Jobs are additional
information that are basically only for display purpose
- `P1 P2 HP1 HP2` declares a game. The loser is the player with 0 hp or less.
If the two players has less than 0 hp, it's a draw. W/D/L = 3/1/0
- `P1 P2 HP1 HP2 Link` is the same as above except it displays a clickable
link for score.


## Licence

Distributed by SquonK under the [WTFPL](https://fr.wikipedia.org/wiki/WTFPL)