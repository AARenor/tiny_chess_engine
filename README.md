# tiny_chess_engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/AARenor/tiny_chess_engine/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/AARenor/tiny_chess_engine/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in one Python file of 4,091 bytes: its own 0x88 move generator (castling, en passant, promotion, and a legality filter that makes each move and asks whether the opponent can take the king) that walks a list of the occupied squares instead of the whole board, an ordered alpha-beta search with a capture-only quiescence and a killer move per ply, a material and piece-square evaluation with the bishop pair, mate and stalemate scoring, and iterative deepening under a fixed node budget of 65,000 nodes a move. No clock and no randomness: the killer table is emptied at the start of every move, so the move is a function of the position and the legal move list alone, and a trial replays move for move. It plays the house gauntlet over HTTP at MAKEFUN_ENV_URL and exits when the trial is done.

Benchmarked on this machine over five positions (the opening, two middlegames, a king-and-pawn endgame, a tactical position): 74,000 to 206,000 nodes a second, the slowest position 0.87 s for its 65,000 nodes, and a completed depth of 4 to 7 plies (5 in the opening, 4 in both middlegames and in the tactical position, 7 in the endgame). Twenty plies of self-play from the start position stayed legal, every move checked against an independent attack scan. The previous 150,000-node build rated Elo 1,099 on the kit's practice trial (one win, two draws, three losses). This build, graded here against the kit's own env on the practice draw's first instance, scored one win, one draw and four losses (Elo 997): a draw by threefold repetition against depth-2, a checkmate win over depth-3, and losses to depth-4 and to the 100k, 250k and 500k node engines.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
