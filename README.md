# roblox-new-games-snapshot

A small, dated dataset of **new Roblox games that already have a real audience**, plus a 40-line script that summarises it.

- `data/new_games_2026-11-18.csv` - 120 games created in the last 45 days with at least 1,500 concurrent players, checked 18 November 2026 at about 12:38 UTC. Columns: name, creator, genre, playing_now, days_old, visits, codes_in_description, place_id.
- `analyze.py` - standard-library Python, no install needed.

```
python3 analyze.py data/new_games_2026-11-18.csv
```

## What this snapshot shows

| | |
|---|---|
| Games listed | 120 |
| Total concurrent players | 1,260,034 |
| Median game age | 29 days |
| Median concurrent players | 6,298 |
| Share of players held by the top 5 games | 18% |
| Games that mention a code in their official description | 20 (17%) |
| Games 14 days old or less | 9 |

By genre, Simulation dominates (55 games, about 632k players), followed by Survival (17 games, about 225k) and Action (13 games, about 132k). Median players per game are more even than the totals suggest: Obby and Platformer and Sports and Racing games have a higher median than Simulation, they just have far fewer entries.

The audience is also not concentrated in a handful of hits: the five biggest games hold under a fifth of all players in the list, so new games still have room to break through.

## Notes on the data

- Player counts are a moment in time and change by the minute; treat the file as a snapshot, not a ranking to quote next week.
- The "codes" column only contains text the developer wrote in the official game description. It is not a list of working codes; always check the game's own page.
- Each row has the Roblox place id, so you can open `https://www.roblox.com/games/<place_id>` for the official page.

## Live version

The numbers above come from the [new Roblox games tracker](https://fresh-game-tracker.dolphinstudio101.workers.dev/?utm_source=github&utm_medium=readme), which refreshes the list and links every game to its official page. If you want a different snapshot date, the same page is the place to start.

Data is factual public information. Licence: MIT for the script, CC0 for the CSV. Not affiliated with Roblox Corporation.
