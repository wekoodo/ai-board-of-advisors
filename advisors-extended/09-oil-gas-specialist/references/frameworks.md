# Oil & Gas Frameworks

> Durable-figures rule (see `../../_config/shared/conventions.md`): the formulas and ratios below
> are durable. Any year-specific or market-specific figure is labeled "illustrative — verify
> current-year value." Confirm the live number before relying on it.

---

## 1. Upstream E&P Project Economics

**When to use:** Evaluating the economics of a producing or proposed exploration & production asset
or program.

**Decline curve:** Production from a well or field declines over time. The Arps hyperbolic model is
the durable workhorse:
```
q(t) = qi / (1 + b · Di · t)^(1/b)
```
where `qi` = initial rate, `Di` = initial decline rate, `b` = decline exponent (0 = exponential,
1 = harmonic). Estimated ultimate recovery (EUR) is the integral of the curve. Unconventional
(shale) wells decline steeply early — often 60–70% in year one *(illustrative — verify current-year
value)* — then flatten.

**Breakeven price:** the commodity price at which project NPV = 0. Build from full-cycle costs:
```
Breakeven = (Capex per unit + Opex per unit + Transport + Royalties + Taxes) / Recoverable units
            (adjusted to the relevant price benchmark)
```
Compare breakeven to the forward strip, not to spot. Recent North American shale half-cycle
breakevens have clustered roughly in the high-$30s to $50s per barrel WTI *(illustrative — verify
current-year value)*; quote the live figure for the specific basin.

**Netback:** realized price at the wellhead after deductions:
```
Netback = Realized Price − Royalties − Transportation − Processing − Production/Severance Taxes − Opex
```
Netback isolates per-unit profitability and lets you compare assets across basins with different
differentials.

**Payback:** time for cumulative undiscounted (or discounted) cash flow to recover invested capital.
Pair with a discounted measure (NPV, IRR, and the PV-10 standard used in reserve reporting) — payback
alone ignores the long decline tail.

**Output:** a per-unit economic picture (breakeven vs. strip, netback, EUR, payback / NPV) and a
clear statement of price sensitivity.

---

## 2. Midstream / MLP Evaluation

**When to use:** Evaluating a midstream operator or an MLP / energy-infrastructure vehicle for
cash-flow quality and distribution durability.

**Cash-flow quality first.** Distinguish **fee-based, take-or-pay** contract revenue (durable) from
**commodity-sensitive** margins (volatile). Volume risk, recontracting risk, and counterparty credit
all sit underneath the headline yield.

**Distribution Coverage Ratio (DCR):**
```
DCR = Distributable Cash Flow (DCF) / Distributions Paid
```
where DCF ≈ Adjusted EBITDA − cash interest − maintenance capex − taxes. A ratio above 1.0 means the
distribution is covered; conservative operators target meaningful cushion, often around 1.2x or
higher *(illustrative — verify current-year value)*. A ratio persistently below 1.0 signals a
distribution funded by debt or equity issuance — a red flag.

**Leverage:**
```
Net Debt / Adjusted EBITDA
```
Investment-grade midstream balance sheets have generally been managed toward roughly the
3x–4.5x range *(illustrative — verify current-year value)*; confirm the current target and covenant
limits. Also check the interest-coverage ratio and the maturity ladder.

**Growth vs. return of capital.** Identify how much of the distribution is return *of* capital vs.
return *on* capital, and whether growth depends on accretive projects, drop-downs, or simply new
debt/equity. Watch the distribution growth rate against DCF growth.

**Output:** an assessment of distribution durability (coverage, leverage, contract mix) separated
from the question of price/valuation.

---

## 3. Energy Investment Due-Diligence Checklist

**When to use:** Before forming a view on any energy investment category or vehicle.

**Asset & operations:**
- [ ] What segment(s) — upstream, midstream, downstream — and what is the commodity exposure?
- [ ] Reserve quality and life (for E&P): proved (1P) vs. proved+probable (2P), decline profile, basin?
- [ ] For midstream: contract mix (fee-based % vs. commodity), volume vs. recontracting risk, counterparties?
- [ ] Operating cost position relative to peers; basin differentials and takeaway capacity?

**Financial:**
- [ ] Breakeven economics vs. the forward strip (E&P); distribution coverage and leverage (midstream)?
- [ ] Balance sheet: net debt/EBITDA, maturity ladder, liquidity, hedge book?
- [ ] Capital allocation: maintenance vs. growth capex, buybacks/distributions, reinvestment discipline?

**Risk:**
- [ ] Commodity-price sensitivity (what oil/gas price assumption is baked in?)
- [ ] Regulatory, environmental, and energy-transition exposure; abandonment/reclamation liabilities?
- [ ] Concentration in the client's overall portfolio (refer to Investment Advisor 05)?

**Tax & structure:**
- [ ] Structure (C-corp, MLP/partnership, royalty trust) and its tax consequences — K-1 vs. 1099,
      UBTI in retirement accounts, return-of-capital, depletion, IDCs (refer to Tax Strategist 02)?

**Output:** a structured go/no-go-to-deeper-analysis summary with the open questions flagged.

---

## 4. Commodity Price-Risk & Hedging Framework

**When to use:** Assessing commodity-price exposure and the durable tools for managing it.

**Step 1 — Identify the exposure.** Long exposure (producer, E&P investor) is hurt by falling prices;
short exposure (refiner buying crude, consumer) is hurt by rising prices. Size it: how much cash flow
or portfolio value moves per dollar of price change?

**Step 2 — Choose the durable tool and understand its trade-off:**

| Instrument | Protects against | Cost / trade-off |
|------------|------------------|------------------|
| **Swap** (fix the price) | Both directions of move | Gives up upside; no premium |
| **Put option / floor** | Downside only | Pay premium; keep upside |
| **Collar** (buy put, sell call) | Downside, within a band | Low/zero premium; caps upside |
| **Costless collar** | Downside, within a band | No premium; tighter upside cap |

**Step 3 — Match the hedge to the purpose.** Operational hedging locks in project economics and
protects coverage/leverage covenants; it is risk-*reduction*. Taking on price exposure without an
offsetting position is speculation — name it as such.

**Step 4 — Size and term.** Hedge a portion (rarely 100%) over a defined horizon; over-hedging
creates its own risk if volumes fall short. Note basis risk (the hedged benchmark vs. the realized
price differ) and roll risk.

**Step 5 — Read a company's hedge book.** Percentage of volumes hedged, instruments used, strike
levels vs. the strip, and tenor tell you how protected near-term cash flows are and how much upside
has been sold.

**Output:** a plain-language statement of the exposure, the candidate hedging tools and their
trade-offs, and a flag where speculation is being mistaken for hedging.
