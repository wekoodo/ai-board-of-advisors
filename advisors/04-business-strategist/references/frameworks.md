# Business Strategy Frameworks

> Durable-figures rule (see `../../_config/shared/conventions.md`): the formulas and ratios below
> are durable. Any year-specific dollar figure is labeled "illustrative — verify current-year value."
> Confirm the live number before relying on it.

---

## 1. SWOT Analysis Template

**When to use:** Strategic situation assessment — especially for business transitions, new market entry, or competitive review.

```
## SWOT Analysis: [Business Name]
Date: [YYYY-MM-DD]

### Strengths (Internal — positive)
- [What does the business do better than competitors?]
- [What unique resources, capabilities, or assets does it have?]
- [What do customers consistently praise?]

### Weaknesses (Internal — negative)
- [Where does performance lag?]
- [What resources are missing?]
- [What do customers complain about?]

### Opportunities (External — positive)
- [What market trends create openings?]
- [What unmet needs exist in the customer base?]
- [What are competitors failing to do well?]

### Threats (External — negative)
- [What competitive, regulatory, or market forces could hurt the business?]
- [What substitutes or disruptors are emerging?]
- [What economic or macro risks are present?]

### Strategic Implications
- SO (Strengths + Opportunities): Use these strengths to capture these opportunities
- WO (Weaknesses + Opportunities): Address these weaknesses to unlock these opportunities
- ST (Strengths + Threats): Use these strengths to mitigate these threats
- WT (Weaknesses + Threats): Reduce these weaknesses to minimize these threats
```

---

## 2. Porter's Five Forces

**When to use:** Assessing competitive dynamics and industry attractiveness.

**The Five Forces:**

1. **Competitive rivalry** (high/medium/low)
   - How many competitors? How differentiated are offerings?
   - Price competition intensity? Industry growth rate (declining = more rivalry)?
   - Switching costs for customers?

2. **Threat of new entrants** (high/medium/low)
   - How high are barriers to entry? (capital, regulation, brand, IP, network effects)
   - Can a competitor enter easily and undercut on price?

3. **Threat of substitutes** (high/medium/low)
   - Are there alternative products/services that meet the same need differently?
   - Do substitutes offer a better price-performance trade-off?

4. **Bargaining power of buyers** (high/medium/low)
   - How many buyers? Are they concentrated (few large customers)?
   - Can buyers easily switch to competitors? Do they have price transparency?

5. **Bargaining power of suppliers** (high/medium/low)
   - How many suppliers for key inputs? Are they concentrated?
   - Is the business dependent on a single supplier?

**Interpretation:** Industries where all five forces are weak = highly attractive (high profitability potential). Industries where multiple forces are strong = commoditized, low-margin.

---

## 3. Business Model Canvas

**When to use:** Clarifying or redesigning the business model; stress-testing assumptions.

```
┌─────────────────┬──────────────────┬─────────────────┬──────────────────────────┐
│ Key Partners    │ Key Activities   │ Value           │ Customer Relationships    │
│                 │                  │ Propositions    │                          │
│ Who helps us    │ What do we do    │                 │ How do we interact with  │
│ deliver value?  │ every day to     │ What problem    │ customers? (self-serve,  │
│                 │ deliver value?   │ do we solve?    │ dedicated, community)    │
│                 │                  │ Why do          │                          │
│                 ├──────────────────┤ customers       ├──────────────────────────┤
│                 │ Key Resources    │ choose us?      │ Customer Segments        │
│                 │                  │                 │                          │
│                 │ What assets do   │                 │ Who are we serving?      │
│                 │ we need?         │                 │ Mass market, niche,      │
│                 │                  │                 │ segmented, B2B, B2C?     │
├─────────────────┴──────────────────┴─────────────────┴──────────────────────────┤
│ Cost Structure                             │ Revenue Streams                    │
│                                            │                                    │
│ What are the major costs in this model?   │ How do we make money? One-time     │
│ Which resources and activities are        │ sales, subscriptions, licensing,   │
│ most expensive?                           │ commissions, usage fees?           │
│                                            │ What is each customer willing      │
│                                            │ to pay?                            │
└────────────────────────────────────────────┴────────────────────────────────────┘
```

---

## 4. OKR Framework

**When to use:** Setting and tracking strategic goals across a quarter or year.

**OKR structure:**
```
Objective: [Qualitative, ambitious, inspiring goal — what we want to achieve]
  Key Result 1: [Measurable outcome that indicates the objective is being achieved]
  Key Result 2: [Measurable outcome]
  Key Result 3: [Measurable outcome — 3 KRs per objective is the norm]
```

**Rules:**
- Objectives: inspiring and qualitative ("become the go-to provider for X")
- Key Results: specific, measurable, time-bound, and outcomes (not activities)
  - Bad KR: "Launch the new website" (activity)
  - Good KR: "Increase website conversion rate from 2% to 4% by Q4"
- 3–5 OKRs per quarter maximum — focus is the point
- Score KRs at end of quarter: 0.7 is a success; 1.0 consistently = not ambitious enough

**Annual OKR → Quarterly cascade:**
1. Set 2–4 annual company OKRs
2. Derive quarterly OKRs that contribute to annual goals
3. Review and score quarterly; adjust as conditions change

---

## 5. Growth Lever Analysis

**When to use:** Client wants to grow revenue but isn't sure which lever to pull first.

**The five levers:**
1. **New customers** — Acquire net-new customers who have never bought before
2. **Higher price** — Increase average transaction value through premium positioning, bundles, or tiered pricing
3. **More purchases per customer** — Increase purchase frequency through subscription models, re-engagement campaigns, or habit formation
4. **Expand into new segments** — Sell existing offerings to adjacent customer segments or verticals
5. **New products/services** — Launch additional offerings for existing or new customers

**Evaluation criteria for each lever:**
- Cost to activate (low / medium / high)
- Speed to revenue (weeks / months / quarters)
- Risk (low / medium / high)
- Scalability (limited / moderate / high)

**Starting point heuristic:**
- If retention rate is below 70%: fix retention before acquiring new customers — leaky bucket problem
- If net promoter score is high: prioritize referral/word-of-mouth for new customer acquisition (lowest CAC)
- If average transaction value is low vs. competitors: test pricing before adding products
- If customer lifetime value is high: invest heavily in acquisition (math supports it)

---

## 6. Unit Economics

**When to use:** Deciding whether to spend on growth, or whether the model can support scale.

**Contribution margin:**
```
Contribution margin $ = Price − Variable cost per unit
Contribution margin % = Contribution margin $ ÷ Price
```
Include true variable costs (COGS, delivery, payment fees, usage). Overhead is not a unit cost.

**CAC vs LTV as a decision rule:**
```
LTV          = Contribution per customer × expected purchases (or retained periods)
Payback      = CAC ÷ contribution per period
LTV:CAC      = LTV ÷ CAC
```

**Decision rules:**
- Negative contribution: do not buy more of that unit. Fix price, mix, or cost first.
- LTV below ~3× CAC (durable heuristic; channel-dependent): acquisition spend is not the growth lever yet.
- Payback longer than cash/runway: freeze growth spend. Tag 01 if household cash is the constraint.
- Unit economics work in one segment and fail in another: grow only the working segment.

**When unit economics forbid growth spend:**
- Contribution is negative or too thin after true variable costs
- CAC is rising while retention or repeat is falling
- Discounting is the only way units move (see Pricing)
- Cash cannot survive the payback period

---

## 7. Pricing

**When to use:** Revenue growth is the goal and the question is raise price vs add volume.

**Raise price vs add volume:**
- **Raise price** when demand hits capacity, willingness-to-pay is untested, contribution is thin, or discounting has trained buyers.
- **Add volume** when contribution is healthy, capacity is idle, CAC is efficient, and price already matches willingness-to-pay.

**Willingness-to-pay tests (cheap first):**
1. Ask recent buyers what they would have paid; note the gap vs list.
2. Quote a higher package to a slice of *new* demand — do not surprise existing contracts.
3. Win/loss: lost on price vs lost on fit. Rarely losing on price usually means underpriced.
4. Price to the outcome (hours saved, revenue enabled), not cost-plus.

**When not to discount:**
- To close a buyer who would have paid list
- To fill capacity if the discount becomes the new reference price
- When fulfillment is the constraint (discounting adds load you cannot deliver)
- When contribution after discount misses the floor needed for CAC payback

---

## 8. Constraint / Bottleneck

**When to use:** Growth stalls, or several "priorities" compete.

**Name the one constraint:**
1. **Sales** — demand is below capacity; pipeline or conversion is the limiter.
2. **Fulfillment** — demand exceeds delivery; quality, lead time, or ops break when you sell more.
3. **Talent / people** — a role or skill is the limiter (see Hiring vs contractor).
4. **Capital / cash / runway** — the plan is sound but cash cannot fund the next step; tag 01 if household cash is the constraint.
5. **Systems** — people and demand exist, but process, tooling, or data cannot handle the load.

**Rules:**
- One constraint at a time. A second "priority" is inventory, not work.
- Exploit the constraint before spending to elevate it (use idle time, drop low-margin work, sequence jobs).
- Do not grow a non-constraint. More sales while fulfillment is binding makes the queue worse.
- Re-diagnose after each 90-day cycle — the constraint moves.

---

## 9. Hiring vs Contractor

**When to use:** A role looks like the constraint, or headcount is the proposed fix.

| | Hire | Contractor |
|---|------|------------|
| Cost | Loaded salary + benefits + ramp waste | Rate × hours; no benefits; management time |
| Ramp | Weeks to months before full output | Faster if the skill is a known package |
| Reversibility | Hard (severance, morale, knowledge) | Easier (end of term) |
| Control / IP | Higher if the role is core | Weaker unless the contract is tight — tag 03 |

**When a role is the constraint:**
- Work queues behind one person and no system change removes the queue
- Quality or sales fail in a way extra hours from current people cannot fix
- The skill is needed every week for 12+ months (bias hire) vs a bounded project (bias contractor)

**Decision rules:**
- If cash/runway is the constraint, do not hire to "feel fully staffed." Contractor or no seat.
- Core, repeating work that *is* the value proposition: hire.
- Specialized, bursty, or reversible work: contractor first.
- A hire that does not attack the current constraint is overhead.

---

## 10. 90-Day Operating Cadence

**When to use:** The strategy is chosen and the operator needs a rhythm, not more analysis.

**Cadence:**
- **Weekly** — a short metrics list tied to the binding constraint (one primary metric, 2–4 supporting). No new strategy in the weekly.
- **Monthly** — did the constraint move? Kill or double the experiments. Cash/runway check.
- **Quarterly** — score OKRs per framework 4 (0.7 = success). Reset the next 90 days; do not add a second constraint.

**90-day plan shape:**
1. Named constraint
2. 1–3 OKRs (from framework 4)
3. Weekly metric and owner
4. What you will not do this quarter

**Rules:**
- If it is not on the weekly metric, it is not this quarter's work.
- Score KRs; do not rewrite the year mid-quarter unless the constraint diagnosis was wrong.
