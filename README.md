# fold-it-solver: a backtracking approach
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

This repository contains a backtracking-based algorithm to solve the Fold-It board game. The game description can be found on [thinkfun.com](https://www.thinkfun.com/wp-content/uploads/2017/07/FoldIt-3550-Instructions.pdf). 

<img src="https://i.ytimg.com/vi/v6c1sovcTPU/maxresdefault.jpg" alt="Screenshot" width="560" height="315">

Check out a [Python app demo]() using PyInstaller to see the game in action (available for Windows).

<video width="560" height="315" controls>
  <source src="https://github.com/ianchaulh/fold-it-solver/blob/main/gui_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Table Of Contents:

- [Game Overview](#game-overview)
  - [Main](#main)
  - [Example](#example)
- [Installation](#installation)
- [Representation](#representation)
  - [Representing folding outcome by 3d array](#representing-folding-outcome-by-3d-array)
  - [Perfoming folding operation](#performing-folding-operation)
- [Usage](#usage)
- [Contributing](#contributing)
  - [Improving runtime](#improving-runtime)
  - [Writing cleaner code](#writing-cleaner-code)
  - [Pull requests](#pull-requests)

## Game Overview
### Main
The core premise of this game is for players to manipulate a $4 \times 4$ square cloth with distinct items in each grid (identical sides). The player's goal is to find a sequence of folds along the clear vertical and horizontal lines that will result in only the selected items being present in the final "plan view" of the folded cloth.

While some combinations of target items may have straightforward folding solutions, others can be more challenging, requiring the player to apply extra spatial awareness, logical reasoning, and keen observation skills.

This project proposes a brute force solution and can be extended to tackle $m \times n$ cloth configurations.
### Example
[Fold-it — game overview at SPIEL 2016 by Happy Baobab](https://www.youtube.com/watch?v=Yx72yootYJg) provides a detailed demonstration of the game mechanics and player experience.

## Installation
```bash
git clone https://github.com/ianchaulh/fold-it-solver.git
cd fold-it-solver
pip install -r requirements.txt
```

## Representation


## Usage


## Contributing
Contributions are welcome 👋.
### Improving runtime
### Writing cleaner code
### Pull requests
