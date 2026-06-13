# Autonomous Alpha Research Engine

> **Alpha mining.** An autonomous Python pipeline that generates, backtests and selects systematic trading signals using institutional-grade robustness filters — Deflated Sharpe Ratio (DSR) and Probability of Backtest Overfitting (PBO).

Currently being extended toward a **Long/Short equity framework** by expanding the alpha universe across individual equities and integrating fundamental, sentiment and alternative data sources.

---

## What It Does

The system runs a fully closed-loop alpha research process without human intervention:

1. **Alpha Generation** — combines financial operators (`ts_mean`, `zscore`, `rank`, `delta`, `ts_std`) across price, volume, returns and volatility to produce candidate signal expressions
2. **Backtesting** — computes PnL, Sharpe ratio and equity curve for each candidate
3. **Robustness Validation** — filters alphas using DSR, PBO, regime stability and walk-forward consistency
4. **Evolutionary Selection** — top survivors are recombined to generate new alpha children for the next generation
5. **Portfolio Construction** — surviving alphas are aggregated into an inverse-volatility weighted portfolio with normalized signal scaling

---

## Architecture

```
quant-alpha-engine/
│
├── master/              # Entry points (research + portfolio runs)
├── engine/              # Alpha generation, backtesting, evolution, validation
├── core/                # Portfolio construction, risk, optimisation
├── validation/          # DSR, PBO, regime validation, bootstrap, stress tests
├── pipelines/           # End-to-end research and portfolio pipelines
├── strategies/          # Standalone strategy implementations
├── execution/           # Paper trading, order management, slippage
├── monitoring/          # Live risk and performance monitoring
├── dashboard/           # Streamlit dashboards (research + investor + PM terminal)
└── outputs/             # CSV exports (alpha book, portfolio, IC results)
```

---

## Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/vdswmart-beep/quant-alpha-engine.git
cd quant-alpha-engine
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install pandas numpy yfinance streamlit plotly
pip install scipy scikit-learn statsmodels
```

### 4. Run the full pipeline
```bash
python3 -m master.master_run
```

This executes two sequential phases:

- **RESEARCH** — generates 200 alpha candidates, backtests each one, filters by robustness (DSR, PBO, regime stability), selects the top 20 survivors and evolves ~40 children for the next generation
- **PORTFOLIO** — loads the best 10 alphas from the library, normalizes their signals, and builds an inverse-volatility weighted portfolio with live performance metrics

**Expected output:**
```
========== RESEARCH ==========
Generating 200 alphas...
Top 20 survivors selected.
Accepted : 199  |  Rejected : 1  |  Survivors : 20  |  Children : 39

========== PORTFOLIO ==========
Selected 10 alphas — Building portfolio...
Portfolio weights:  alpha_0: 10.3%  |  alpha_1: 9.2%  |  ...
Sharpe : 0.78  (annualised)

DONE
```

### 5. Launch the Research Dashboard
```bash
streamlit run dashboard/research/app.py
```

Open [http://localhost:8501](http://localhost:8501) and navigate across:

| Page | Description |
|------|-------------|
| Alpha Factory | Live alpha generation and scoring |
| IC Analysis | Information Coefficient by alpha |
| Walk-Forward | Out-of-sample robustness validation |
| Feature Lab | Signal decomposition and statistics |
| Crowding | Overlap and correlation heatmaps |
| Portfolio Construction | Weights, equity curve and attribution |

Press `Ctrl + C` to stop.

### 6. Launch the Investor Dashboard
```bash
streamlit run dashboard/Investor/app.py
```

---

## Key Modules

| Module | Description |
|--------|-------------|
| `engine/alpha_expression_engine.py` | Evaluates alpha expressions against market data |
| `engine/alpha_research_loop.py` | Orchestrates the full generation → validation → selection loop |
| `engine/mythos_validator.py` | Institutional robustness scoring (DSR, PBO, stability) |
| `engine/alpha_evolution.py` | Evolutionary recombination of winner alphas |
| `core/portfolio.py` | Inverse-volatility portfolio construction |
| `validation/deflated_sharpe.py` | Deflated Sharpe Ratio implementation |
| `validation/pbo.py` | Probability of Backtest Overfitting (CSCV method) |

---

## Outputs

All results are saved automatically in `outputs/`:

| File | Description |
|------|-------------|
| `alpha_book.csv` | Full alpha library with robustness scores |
| `portfolio.csv` | Weights and portfolio equity curve |
| `ic_results.csv` | Information Coefficient by alpha and period |
| `walkforward_results.csv` | Out-of-sample validation metrics |
| `rankings.csv` | Alpha rankings by DSR and PBO |

---

## Stack

- **Python 3.9** — pandas, numpy, scipy, scikit-learn, statsmodels
- **Data** — yfinance (market data)
- **Validation** — custom DSR, PBO, bootstrap, regime detection
- **Visualisation** — Streamlit multi-page dashboards + Plotly
- **Execution** — paper trading engine with order management and slippage modelling

---

## Background

Built during a Global Markets trainee program at a tier-1 investment bank, alongside live exposure to equity derivatives, structured products and fixed income trading desks. Designed to reflect institutional alpha research workflows (WorldQuant / Two Sigma style expression-based alpha mining) with rigorous out-of-sample validation.

---

*For questions or collaboration: [github.com/vdswmart-beep](https://github.com/vdswmart-beep)*
