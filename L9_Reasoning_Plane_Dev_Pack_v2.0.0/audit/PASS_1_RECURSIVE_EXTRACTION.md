# Recursive Extraction Pass 1 — Conversation Reconstruction

Goal: recover every material architecture decision introduced after the v1.2 pack, especially the game-theory / signal / strategic-value branch.

## Recovered concern families

1. **Dynamic state/time** — state is a trajectory, not snapshot; material actions/observations force bounded re-evaluation.
2. **Hidden state** — uncertain actor/world variables live as distributions, not Boolean heuristics.
3. **Signal interpretation** — signal meaning is context-conditioned and can invert as later evidence arrives.
4. **Signal correlation** — more observations can be redundant; duplicate/correlated evidence must not inflate confidence.
5. **Strategic signal generation** — another actor may choose an action partly to alter our behavior, making the evidence-generation process incentive-sensitive.
6. **Higher-order beliefs** — explicit bounded models of what others believe about us and vice versa.
7. **Strategic interaction** — coupled action/belief/value recursion across multiple actors through time.
8. **Game theory** — method family, not node; zero-sum/positive-sum distinction; best response/equilibrium/repeated-game/signaling/commitment/exploitability/mechanism-design questions.
9. **Bounded lookahead** — action/reaction trajectory search stops by horizon/budget/convergence/VOC.
10. **ActorModel** — dense context-scoped derived hypothesis state with observations, response tendencies and higher-order beliefs.
11. **Graph Memory** — natural home for derived actor patterns; remains context not truth.
12. **Odoo projection** — Odoo retains authoritative business facts plus one concise human-facing Negotiating Style projection, not dense hidden cognitive state.
13. **Bilateral brokerage** — both supplier floor and buyer WTP are latent; buy/sell prices may be strategic outcomes.
14. **Strategic influence** — truthful signaling/incentive design distinguished from deception.
15. **Agent reuse** — Mack/Emma/L-CTO/future agents need the same strategic projection machinery; adapter earned, new node not earned.
16. **Strategic Value** — replaces vague machine leverage score.
17. **Systemic Future Value** — counterfactual future-state improvement, including future work elimination.
18. **Propagation topology** — one-way/bilateral/closed-loop/mesh valued by unrolling cycles through time.
19. **Causal attribution** — mesh paths cannot double count shared downstream value.
20. **Signal value** — decision improvement + future reusable value - capture/processing/propagation/misleading cost.
21. **Rational attention** — cheap relevance filter before expensive reasoning.

Result: no material concern from the branch is intentionally omitted from v2 design surfaces.
