# Edge, robotics & games

Latency is the point here. A decision every few milliseconds is only possible with a small, non-generative model. Descriptions are in original wording, based on each project's own GitHub description (as of 04 Oct 2026). Projects were discovered through several lists and searches (see [REFERENCES.md](../REFERENCES.md)). The tools have not been run. The License column is what GitHub reports for each repo, not legal advice.

## Edge and embedded

| Tool | What it does | License |
|---|---|---|
| [jevlike-esp32](https://github.com/david-cermak/jevlike-esp32) | Decision-model-style edge router running on an ESP32 | MIT |
| [robo-harness](https://github.com/grmkris/robo-harness) | Workbench for a SO-101 robot arm (Bun/Effect coordinator, React UI, LeRobot motors) | none stated |
| [jev-drone](https://github.com/RomanSlack/jev-drone) | Camera-only drone in MuJoCo with a small decision model in the loop at 2.5 Hz | MIT |
| [typesafe-jev-drone-demo](https://github.com/kxzk/typesafe-jev-drone-demo) | Three.js drone simulator with a Python backend and live decision-model navigation | none stated |
| [Edge service orchestration paper](https://arxiv.org/abs/2609.22753) | LLM replacement for latency-sensitive orchestration | n/a |
| [Laya in the browser](https://dev.to/vishalmysore/a-421m-encoder-beat-a-15b-llm-at-running-my-agent-inside-a-browser-tab-kc2) | 421M encoder running an agent in a browser tab (blog; a 1.5B LLM used alongside) | n/a |

## Games

| Tool | What it does | License |
|---|---|---|
| [typesafe-mario](https://github.com/fhshaik/typesafe-mario) | Agent that plays Super Mario Bros. from structured emulator state | none stated |
| [tsai-sc](https://github.com/phyous/tsai-sc) | Plays the StarCraft shareware version through keyboard and mouse, recording action probabilities | MIT |
| [jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon) | Plays Pokémon Red with a decision model | unclear |
| [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) | Pokémon Red on PyBoy: code handles routing and arithmetic, the model chooses at branches | MIT |
| [PlayJev](https://github.com/OmniJev/PlayJev) | 0.8B multimodal decision-style model that plays GUI games from raw pixels | Apache-2.0 |
| [Jev Pong](https://github.com/ably-labs/jev-pong) | Pong where the ball moves one step per model decision, comparing Jev and LLMs | Apache-2.0 |
| [typesafe-playground](https://github.com/kavehmz/typesafe-playground) | Interactive experiments from support routing to 3D driving simulations | none stated |
| [jev-experiments](https://github.com/dabit3/jev-experiments) | Collection of 22 latency-focused applications (repo has no description) | none stated |
