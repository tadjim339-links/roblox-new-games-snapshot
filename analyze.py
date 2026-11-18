#!/usr/bin/env python3
"""Summarise a snapshot of new Roblox games (CSV in data/). Standard library only.
Usage: python3 analyze.py data/new_games_2026-11-18.csv"""
import csv, sys, statistics as st
from collections import defaultdict

rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
for r in rows:
    for k in ("playing_now", "days_old", "visits"):
        r[k] = int(r[k])

print(f"{len(rows)} games, {sum(r['playing_now'] for r in rows):,} concurrent players in total")
print(f"median age: {st.median(r['days_old'] for r in rows)} days")
print(f"median concurrent players: {st.median(r['playing_now'] for r in rows):,.0f}\n")

by = defaultdict(list)
for r in rows:
    by[r["genre"]].append(r)
print(f"{'genre':<22}{'games':>6}{'players':>10}{'median':>9}")
for g, rs in sorted(by.items(), key=lambda kv: -sum(x["playing_now"] for x in kv[1])):
    print(f"{g:<22}{len(rs):>6}{sum(x['playing_now'] for x in rs):>10,}{st.median(x['playing_now'] for x in rs):>9,.0f}")

top5 = sorted(rows, key=lambda r: -r["playing_now"])[:5]
share = sum(r["playing_now"] for r in top5) / sum(r["playing_now"] for r in rows)
print(f"\ntop 5 games hold {share:.0%} of all players in this list")

with_codes = [r for r in rows if r["codes_in_description"]]
print(f"{len(with_codes)} of {len(rows)} games ({len(with_codes)/len(rows):.0%}) mention a code in the official description")

young = [r for r in rows if r["days_old"] <= 14]
print(f"{len(young)} games are 14 days old or less; biggest: "
      + (max(young, key=lambda r: r['playing_now'])['name'] if young else "n/a"))
