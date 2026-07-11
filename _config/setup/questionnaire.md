# Onboarding Questionnaire

This is the question bank for the Board of Advisors onboarding interview. Work through each
domain in order. Ask questions conversationally — do not read this file verbatim. Follow up
naturally on the user's answers.

---

## Domain 1: Personal

- What is your first name? (And preferred name if different?)
- How old are you, and what year were you born?
- Where are you located? (City, state/province, country)
- What is your marital or relationship status?
  - If married or partnered: Is your spouse/partner employed? Approximate income?
- Do you have any dependents? (Children, parents, others)
  - If yes: How many, and what ages? Any special needs or circumstances?
- How would you describe your current health? (General — relevant for insurance and estate planning)

> **[Agent instruction]:** When the Personal domain is answered, write `_config/profile/personal.md`
> with a clean summary before proceeding to Employment.

---

## Domain 2: Employment

- What is your current role and who do you work for? (Or are you self-employed?)
- Employment type? (W-2 employee, 1099 contractor, both, or business owner only?)
- Approximate annual gross income from employment?
- Employer benefits: 401(k)/403(b) match (rate?), health insurance, HSA/FSA, equity (RSUs/options/ESPP), other?
- How stable and predictable is your income? Growing, flat, or variable?
- Secondary income sources? (Freelance, rental, side business, dividends) Approximate amounts?

> **[Agent instruction]:** Include Employment as an "Income & Employment" section within
> `_config/profile/financial.md`. Do not create a separate file.

---

## Domain 3: Business

> **[Agent instruction]:** Ask whether the user owns any businesses first. If not, write
> `_config/profile/businesses.md` noting the user owns no businesses, then skip to Domain 4.

- What businesses do you own? (Name, industry, your role — sole owner, partner, shareholder?)
- For each business:
  - Legal entity type? (Sole prop, LLC, S-Corp, C-Corp, partnership?)
  - Approximate annual gross revenue and net profit (after owner comp)?
  - Stage? (Startup, growth, mature, considering exit?)
  - Employees or contractors? Roughly how many?
  - Significant business liabilities? Personal guarantees on business debt?
  - Co-owners? Any buy-sell agreement in place?

> **[Agent instruction]:** Write `_config/profile/businesses.md` with a structured summary of
> each business after this domain.

---

## Domain 4: Financial

- Liquid assets (approximate): checking/savings combined; money market/short-term?
- Tax-advantaged balances (approximate): 401(k)/403(b), Traditional IRA, Roth IRA, HSA, other (529/ABLE)?
- Non-retirement investment accounts (taxable brokerage) — approximate value?
- Real estate: primary residence (value and mortgage balance?); rentals/investment property (values and balances?)
- Other significant assets: vehicles, collectibles, business equity not captured above?
- Liabilities: mortgage(s) and rate(s); student loans; auto loans; credit card (balance and rate); other; business debt with personal guarantee?
- Insurance in place: life (term/permanent, amount, who?), disability (ST/LT, employer/private?), health, homeowner's/renter's, auto, umbrella, business?
- Approximate monthly cash flow — saving, breaking even, or spending more than you earn?

> **[Agent instruction]:** Write `_config/profile/financial.md` including the Income & Employment
> section from Domain 2 and all financial information from Domain 4.

---

## Domain 5: Investments

- What investment account types do you hold? (401k, IRA, Roth IRA, taxable brokerage, other?)
- Approximate current allocation: stocks/equities, bonds/fixed income, real estate/REITs, cash, alternatives (percentages)?
- Risk tolerance — conservative / moderate / aggressive — and what drives it?
- Primary investment time horizon — when will you draw on these assets?
- Any investment restrictions or preferences? (ESG, sector exclusions, concentration limits?)
- Working with an advisor/manager, or self-directed?

> **[Agent instruction]:** Write `_config/profile/investments.md` with a structured summary.

---

## Domain 6: Goals

- **Short-term (1–3 years):** specific goals, approximate cost/target, timeline.
- **Medium-term (3–10 years):** major milestones (home purchase, business expansion, education, career change).
- **Long-term (10+ years):** target retirement age; desired retirement income (today's dollars); legacy goals and target; other major long-term goals.
- **Education funding:** saving for children's or your own education? Ages and target funding level?

> **[Agent instruction]:** Write `_config/profile/goals.md` with Short-Term, Medium-Term,
> Long-Term, and Education sections.

---

## Domain 7: Concerns

- Biggest current financial worries or pain points?
- Major financial decisions/transitions in the next 12–24 months? (Business sale, real estate purchase, inheritance, job change, divorce, retirement?)
- Areas where you feel uncertain or undereducated that advisors should address?
- Anything else — financial, legal, personal, or business — the board should know?

> **[Agent instruction]:** Append a "Current Concerns" section to `_config/profile/goals.md`
> with the user's concerns, upcoming decisions, and areas of uncertainty.

---

## Interview Complete

> **[Agent instruction]:** When all domains are complete, verify all five profile files and their
> required headers/sections using the completion gate in `_config/setup/CONTEXT.md`. Only after the
> gate passes, tell the user:
>
> "Your profile is saved to `_config/profile/`. All profile files are gitignored and stay on your
> machine only. You can update any section any time by editing the file directly or asking an
> advisor to update it during a session.
>
> To begin using the Board of Advisors, return to the root `CONTEXT.md` and tell your agent what
> you'd like to discuss."
