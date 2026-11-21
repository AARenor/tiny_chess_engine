# tiny_chess_engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/AARenor/tiny_chess_engine/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/AARenor/tiny_chess_engine/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in one Python file of 4,091 bytes: its own 0x88 move generator (castling, en passant, promotion, and a legality filter that makes each move and asks whether the opponent can take the king), an ordered alpha-beta search with a capture-only quiescence, a material and piece-square evaluation with the bishop pair, mate and stalemate scoring, and iterative deepening under a fixed node budget of 150,000 nodes a move. No clock and no randomness: the same position always gets the same move, so a trial replays move for move. It plays the house gauntlet over HTTP at MAKEFUN_ENV_URL and exits when the trial is done.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
