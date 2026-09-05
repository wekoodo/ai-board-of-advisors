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
> with a clean summary before proceeding to Employment. If that named path is already a shim, write
> the resolved owning sections and do not copy facts into the shim.

---

## Domain 2: Employment

- What is your current role and who do you work for? (Or are you self-employed?)
- Employment type? (W-2 employee, 1099 contractor, both, or business owner only?)
- Approximate annual gross income from employment?
- Employer benefits: 401(k)/403(b) match (rate?), health insurance, HSA/FSA, equity (RSUs/options/ESPP), other?
- How stable and predictable is your income? Growing, flat, or variable?
- Secondary income sources? (Freelance, rental, side business, dividends) Approximate amounts?

> **[Agent instruction]:** Include Employment as an "Income & Employment" section within
> `_config/profile/financial.md` when that path is still a single file. If it is already a shim,
> write the resolved `Income & Employment` owning section and do not copy facts into the shim
> (`_config/shared/icm-conventions.md` **Resolve a named profile path**). Do not create a
> separate file during a first-write interview. A later focused write may split that named path;
> follow `_config/shared/icm-conventions.md` **Keep files load-scoped**.

---

## Domain 3: Business

> **[Agent instruction]:** This domain has two optional branches. Neither is required to finish
> general onboarding. Ask the entity gate first, then the living-trust gate.

### Entities

Ask whether the user owns, controls, manages, benefits from, or operates through any businesses,
holding companies, land trusts, disregarded entities, or joint ventures.

- If **no**: write `_config/profile/businesses.md` noting that none are owned. Do not create
  `_config/profile/entities/index.md`. Continue to the living-trust gate.
- If **yes**, for each entity:
  - What is its legal name and a stable short name?
  - Is it an LLC, corporation, land trust, sole proprietorship, or another structure?
  - Where was it formed, and where else is it registered?
  - What is its known federal tax classification or election?
  - Who owns, controls, manages, or benefits from it?
  - What parent, subsidiary, trust, property, or partner relationships matter?
  - What does it do, and what stage is it in?
  - Which facts are uncertain or need confirmation?

> **[Agent instruction]:** When entities exist, write `_config/profile/businesses.md` as the
> high-level map only. Write `_config/profile/entities/index.md`, then create one
> `_config/profile/entities/<entity-slug>/overview.md` per known entity from
> `entities/_template/overview.md`. Choose each slug by following
> `_config/profile/entities/CONTEXT.md` **Slugs** before creating a folder. Mark each entity
> `basic` with freshness `current`. Do not start in-depth entity onboarding during this domain.
> Do not require the user to pick a next entity to deepen. After this interview, adding another
> entity uses `_config/setup/entity-registration.md`.

### Living trust

Ask whether the user has a revocable living trust or similar estate vehicle. Do not count land
trusts already listed as entities.

- If **no**: do not create `_config/profile/trust.md`. Continue to Domain 4.
- If **yes**:
  - What is the trust's legal name and general purpose?
  - Who are the current trustees, and how do they share decision authority?
  - Which family members or beneficiaries are relevant to board planning?
  - Which major assets or entities connect to the trust?
  - Are any funding, titling, amendment, or succession questions pending?

> **[Agent instruction]:** Write `_config/profile/trust.md` with identity, trustees, beneficiaries,
> connected assets, and open questions. If that named path is already a shim, write the resolved
> owning sections and do not copy facts into the shim. Keep detailed operating-entity facts in the
> entity registry. Do not start `_config/setup/trust-onboarding.md` during this domain.

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
> section from Domain 2 and all financial information from Domain 4 when that path is still a
> single file. If it is already a shim, write only Domain 4 facts into the owning section for each
> heading being written (`_config/shared/icm-conventions.md` **Resolve a named profile path**).
> Do not rewrite Income & Employment; Domain 2 already owns that section. Do not copy facts into
> the shim.

---

## Domain 5: Investments

- What investment account types do you hold? (401k, IRA, Roth IRA, taxable brokerage, other?)
- Approximate current allocation: stocks/equities, bonds/fixed income, real estate/REITs, cash, alternatives (percentages)?
- Risk tolerance — conservative / moderate / aggressive — and what drives it?
- Primary investment time horizon — when will you draw on these assets?
- Any investment restrictions or preferences? (ESG, sector exclusions, concentration limits?)
- Working with an advisor/manager, or self-directed?

> **[Agent instruction]:** Write `_config/profile/investments.md` with a structured summary. If
> that named path is already a shim, write the resolved owning sections and do not copy facts into
> the shim.

---

## Domain 6: Goals

- **Short-term (1–3 years):** specific goals, approximate cost/target, timeline.
- **Medium-term (3–10 years):** major milestones (home purchase, business expansion, education, career change).
- **Long-term (10+ years):** target retirement age; desired retirement income (today's dollars); legacy goals and target; other major long-term goals.
- **Education funding:** saving for children's or your own education? Ages and target funding level?

> **[Agent instruction]:** Write `_config/profile/goals.md` with Short-Term, Medium-Term,
> Long-Term, and Education sections. If that named path is already a shim, write each of those
> headings only to the section the folder router maps for that heading. Do not write them into
> the Current Concerns or action-register files. Do not copy facts into the shim.

---

## Domain 7: Concerns

- Biggest current financial worries or pain points?
- Major financial decisions/transitions in the next 12–24 months? (Business sale, real estate purchase, inheritance, job change, divorce, retirement?)
- Areas where you feel uncertain or undereducated that advisors should address?
- Anything else — financial, legal, personal, or business — the board should know?

> **[Agent instruction]:** Append a "Current Concerns" section to `_config/profile/goals.md`
> with the user's concerns, upcoming decisions, and areas of uncertainty. If that named path is
> already a shim, write the resolved owning section.

---

## Interview Complete

> **[Agent instruction]:** When all domains are complete, verify the five required profile files
> and their required headers/sections using the completion gate in `_config/setup/CONTEXT.md`.
> Confirm optional `trust.md` / `entities/` files only when this interview created them. Only
> after the gate passes, tell the user:
>
> "Your profile is saved to `_config/profile/`. Real profile files are excluded from Git by
> default. Cloning this repo does not restore them. Content you send to a cloud model follows
> that provider's policies. You can update any section any time by editing the file directly or
> asking an advisor to update it during a session.
>
> If you registered entities, you can deepen one later by asking — that is not required to use
> the board. You can also add another entity later without repeating this interview. Same for a
> living-trust profile.
>
> To begin using the Board of Advisors, return to the root `CONTEXT.md` and tell your agent what
> you'd like to discuss."
