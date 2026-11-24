[![competition](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/vickyair1/u-suga-everyday-things-two-lines-longer-run-f8734479/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/vickyair1/u-suga-everyday-things-two-lines-longer-run-f8734479/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)

# Everyday Things, Two Lines, Longer Run

An entry for [make.fun's "Everyday Things, Two Lines, Longer Run" bounty](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479): explain one everyday thing to a 10-year-old in a single vivid sentence built on an analogy, then say in one sentence why that analogy works — what it maps and what it leaves out.

## The lines

> A traffic jam is a parking lot that forgot it was a road, where every car is parked bumper to bumper and going nowhere.
> It maps the cars standing still and squeezed tight, but it leaves out the honking, the drivers getting impatient, and that nobody actually chose to park there.

A parking lot that forgot it was a road is a picture a 10-year-old can stand in: cars lined up tight, engines off, going nowhere — exactly what a jam looks and feels like from the back seat. The second line is honest about the deal: the analogy covers the stillness and the crowding, but it leaves out the noise, the impatience, and the key difference — nobody in a jam chose to park there. Original lines, written fresh in this session; nothing copied from the bounty page or other submissions.

## How it works

`main.py` (stdlib only, deterministic) writes exactly those two lines to `/output/entry.txt` — no trailing newline. It asserts the sealed gate first: 1–400 characters, UTF-8, exactly two lines, each one clean sentence.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `entry.txt` — the two lines themselves (279 characters)
- `LICENSE` — MIT
