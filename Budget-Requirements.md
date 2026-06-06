# Newsite.html — Requirements instruction 
**Purpose:** Reference document for rebuilding the personal finance dashboard as a component-based frontend application from scratch.

---

## 1. Page Overview

The Budget page is a personal financial reporting dashboard for Seun Gwak. 
It aggregates NAB credit card statements uploaded by user and salary data uploaded by user into interactive charts, advisory analysis, and a rolling forecast engine. All logic runs client-side — no backend, no auth.

**Entry point:** `Newsite.html` linked from `index.html` as the "Budget1" nav item under the Finance category. create "Budget1" nav item  if it doesn't exist under Finance category

---

## 2. Design System

### 2.1 Color Palette

| Token | Hex | Usage |
|---|---|---|
| `--bg` | `#F0F4FF` | Page background |
| `--surface` | `#FFFFFF` | Card/panel backgrounds |
| `--surface2` | `#F8FAFF` | Subtle table row / header fills |
| `--nav` | `#060E1F` | (defined but unused — nav uses `#075985`) |
| `--ink` | `#0F172A` | Primary text |
| `--ink2` | `#334155` | Secondary text |
| `--ink3` | `#64748B` | Muted/label text |
| `--ink4` | `#94A3B8` | Placeholder / column headings |
| `--border` | `rgba(15,23,42,.07)` | Card borders |
| `--blue` | `#2563EB` | Primary accent (links, active states) |
| `--blue-s` | `#EFF6FF` | Blue tint backgrounds |
| `--green` | `#059669` | Positive/income |
| `--green-s` | `#ECFDF5` | Green tint |
| `--amber` | `#D97706` | Warning |
| `--amber-s` | `#FFFBEB` | Amber tint |
| `--red` | `#DC2626` | Negative/expense/danger |
| `--red-s` | `#FEF2F2` | Red tint |
| `--purple` | `#7C3AED` | Retail / misc accent |
| `--purple-s` | `#F5F3FF` | Purple tint |
| `--indigo` | `#4F46E5` | Education category |
| `--teal` | `#0D9488` | Fitness category |
| `--orange` | `#EA580C` | (defined, used via inline) |

**Header gradient:** `linear-gradient(160deg, #0369A1 0%, #0EA5E9 55%, #38BDF8 100%)` — ocean blue.
**Budget nav bar:** `#075985` (dark blue, below site nav).

### 2.2 Typography

| Font | Weight(s) | Usage |
|---|---|---|
| Plus Jakarta Sans | 300, 400, 500, 600, 700, 800 | All body text, headings, nav |
| JetBrains Mono | 400, 500, 600 | All numbers, data labels, mono tags, column headers |

Both loaded from Google Fonts CDN.

### 2.3 Spacing & Radius

| Token | Value |
|---|---|
| `--r` | `14px` — standard card radius |
| `--rs` | `8px` — small elements (buttons, pills) |
| `--rl` | `20px` — hero chart radius |
| Max content width | `1240px` |
| Main padding | `40px 48px` (desktop), `24px 20px` (mobile) |
| Nav padding | `0 48px` (desktop), `0 20px` (mobile) |

### 2.4 Shadows & Borders

- Default card: `border: 1px solid var(--border)` — no shadow unless hovered
- Hover shadow: `0 4px 20px rgba(0,0,0,.06), 0 1px 3px rgba(0,0,0,.04)` + `translateY(-2px)`
- Hero chart: 3px top gradient bar `linear-gradient(90deg, #3B82F6, #8B5CF6, #0D9488)`
- Stat cards: 3px top bar in card's accent color

### 2.5 Category Color Map

Used consistently across all charts and dot indicators:

| Category | Hex |
|---|---|
| education | `#6366F1` (indigo) |
| groceries | `#3B82F6` (blue) |
| dining | `#F97316` (orange) |
| fitness | `#0D9488` (teal) |
| transport | `#F59E0B` (amber) |
| retail | `#8B5CF6` (purple) |
| utilities | `#10B981` (green) |
| subscriptions | `#EF4444` (red) |
| fees | `#6B7280` (grey) |
| health | `#EC4899` (pink) |
| income | `#059669` (dark green) |
| mortgage | `#DC2626` (red) |
| other | `#94A3B8` (muted) |

---

## 3. Layout Architecture

### 3.1 Page Structure (top to bottom)

```
[Site Nav]          ← sticky, z-index 200, shared across all pages
[Header]            ← ocean blue gradient, full-width, not sticky
[Budget Tab Nav]    ← sticky at top:56px (below site nav), z-index 100
[Sub-nav]           ← visible only on Expenses tab
[Main Content]      ← tab-switched sections, max-width 1240px
[Footer]            ← account info + back link
```

### 3.2 Dual Navigation System

**Site Nav (`.site-nav`):**
- Sticky, `height: 56px`
- Brand: "Seun Gwak" + blue dot
- Links: EL1 · Brain Dump · Budget (active) · Property · RBA Rate
- Frosted glass: `backdrop-filter: blur(10px)`
- Active link: `font-weight: 600`, `color: #0a0a0a`

**Budget Tab Nav (`nav`):**
- Sticky at `top: 56px`
- Background: `#075985`
- Tabs: Advisory · Income · Expenses · Forecast · + Upload
- Active tab: white text + white bottom border
- Font size: 25px, font-weight: 700

**Sub-nav (`#sub-nav`):**
- Visible only when Expenses tab is active
- White surface, mono labels, blue active indicator
- Sub-tabs: Overview · Jan Statement · Feb Statement · Mar Statement · Apr Forecast · Insights
- Dynamically extended when new statements are uploaded

### 3.3 Responsive Breakpoints

| Breakpoint | Changes |
|---|---|
| `≤ 768px` | Side padding drops to 20px; chart-grid becomes single column; h1 → 26px; balance-card in header hidden; budget table collapses to 3 columns |
| `≤ 540px` | Site nav links gap shrinks |
| `≤ 380px` | Site nav links hidden entirely |

---

## 4. Component Inventory

### 4.1 Stat Card (`.stat-card`)
- White background, 1px border, 14px radius
- 3px top bar in accent color
- Labels in JetBrains Mono, value in large font with accent color
- Optional sub-text and delta indicator (`.d-up` red / `.d-dn` green — counterintuitively, up=bad for expenses)
- Hover: `translateY(-2px)` + shadow
- Responsive grid: `auto-fit, minmax(185px, 1fr)`
- Variants: `sc-blue`, `sc-green`, `sc-red`, `sc-amber`, `sc-purple`, `sc-indigo`, `sc-teal`, `sc-ink`

### 4.2 Chart Box (`.chart-box`)
- White surface, 1px border, 14px radius, 24px padding
- Title (17px, 700) + subtitle in JetBrains Mono (14px, ink3)
- `canvas` inside `.chart-wrap` with explicit height
- Full-width variant: `.chart-box.full` spans both columns
- Grid: `grid-template-columns: 1fr 1fr` with 20px gap

### 4.3 Hero Chart (`.hero-chart`)
- White surface, 20px radius, 30px 32px padding
- 3px top gradient bar (blue → purple → teal)
- Used for the primary/featured chart in each section
- Canvas height: 280px standard

### 4.4 Data Table (`.data-table`)
- Full-width, collapse borders
- Header: JetBrains Mono, 12px, uppercase, ink4
- Last column right-aligned with JetBrains Mono + bold
- Row hover: surface2 background
- Category dot indicator: 8px square, 3px radius

### 4.5 Alert (`.alert`)
- Three variants: `alert-red`, `alert-green`, `alert-blue`
- Icon-less — just colored left-border-style border + tinted background
- `strong` tag for the prefix label in accent color

### 4.6 Forecast Block (`.forecast-block`)
- Container with header row (category dot + label + total) on surface2
- Body rows: 4-column grid (merchant | prev actual | last actual | forecast)
- Columns: `1fr 90px 90px 100px`
- Row hover state

### 4.7 Budget Analysis Block (`.budget-block`)
- Header: 5-column grid (category | current | % income | recommended | status)
- Columns: `1fr 100px 90px 110px 120px`

### 4.8 Status Pill (`.status-pill`)
- Inline-flex, 100px radius, JetBrains Mono, 12px, uppercase, bold
- Variants: `sp-green` (On target), `sp-red` (Over limit / Critical), `sp-amber` (Watch / Review)

### 4.9 Insight Card (`.insight-card`)
- White surface, 1px border, 14px radius, 22px padding
- Colored `border-top: 3px solid` for priority indication
- Tag (mono, uppercase), title (700, 17px), body text (ink3, 14px), amount (mono, 19px, bold)
- Hover: same translateY + shadow effect
- Grid: `auto-fit, minmax(280px, 1fr)`

### 4.10 Grand Total Bar (`.grand-total`)
- Dark gradient background: `linear-gradient(135deg, #0F172A, #1E3A5F)`
- White text, large value on right
- Stacks vertically (label + sub-label on left, value on right)

### 4.11 Credit Block (`.credit-block`)
- Green-tinted header with total credited
- 4-column rows: date | description | type pill | amount
- Payment pill (blue) and Refund pill (purple)
- Summary bar at bottom

### 4.12 Upload Zone (`.upload-zone`)
- Dashed border, centered content, emoji icon + title + hint
- Invisible `<input type="file">` covers entire zone (click + drag both work)
- Hover / drag-over state: blue border + blue tint background

### 4.13 Upload Stats Cards (`.us-card`)
- Smaller stat cards (`.upload-stats` grid, `minmax(150px, 1fr)`)
- Show: total charges, credits received, largest charge, top category

### 4.14 Preview Table (`.preview-tbl`)
- Sticky headers, `max-height: 420px`, overflow scroll
- Category column has inline `<select>` dropdown for manual override
- Source badge indicator (hist/auto/AI/new?)
- Credit rows highlighted green

### 4.15 Category Source Badge (`.cat-src`)
| Badge | Color | Meaning |
|---|---|---|
| `hist` | Green | Matched from merchant history cache |
| `auto` | Blue | Matched by keyword rule |
| `AI ✦` | Purple | Categorised by Gemini API |
| `new?` | Amber | Unknown — needs user review |

### 4.16 Header (`.header-inner`)
- Left side: eyebrow label + H1 + metadata line + hpills row
- Right side: balance card (hidden on mobile)
- Eyebrow: JetBrains Mono with left-line decorator (`::before`)
- Hpills: glassmorphism pill buttons on the blue gradient

---

## 5. Functional Requirements

### 5.1 Tab Navigation System
- Five primary tabs: Advisory, Income, Expenses, Forecast, Upload
- `showSection(id, event)` JS function: toggles `.tab-section.active`, updates `.nav-tab.active`
- Sub-nav only visible when Expenses is active
- `showSub(id, event)` JS function: toggles `.sub-section.active`, updates `.sub-tab.active`
- Tabs and sub-tabs support click events on `<button>` elements
- New sub-tabs are injected dynamically when statements are uploaded

### 5.2 Advisory Tab (update it everytime user uploaded file with newest analysis on the file)

**Purpose:** Financial health summary and personalised recommendations.

**Components:**
- 2 alert banners at top (critical red + positive green)
- 6 stat cards: monthly take-home , after-mortgage, housing+education % , NAB balance , savings rate , super 
- 2-column chart grid:
  - Reality donut: current budget breakdown as % of monthly take-home
  - Recommended vs actual: grouped bar chart (actual % vs recommended %)
- Budget analysis table: 10 rows (mortgage through savings), with 5 columns and status pills
- 6 insight/action cards ordered by priority, color-coded by urgency
- Target budget allocation bar chart 
- 2 grand total bars: income after mortgage + estimated monthly overspend
- 2 advisory alerts at bottom

**Data (NOT HARD-CODED), You will need to analyse data from uploaded file by user and update it everytime user uploaded a file:**
- Monthly income:
- Mortgage: 
- Education: 
- Detailed category vs recommended thresholds

### 5.3 Income Tab (update it everytime user uploaded file with newest analysis on the file)

**Purpose:** Payroll history and income trend analysis.

**Components:**
- Hero line chart:analyse x number of pay in pay periods by user uploaded data , coloured points at pay-rise dates
- 6 stat cards: current FN pay, current monthly, annual gross, total YTD, total pay rise, mortgage % of income
- Monthly income bar chart 
- Income vs mortgage dual-line chart
- Pay rise stepped line chart
- Data table: x pay periods with amounts and percentage changes

**Data (NOT HARD-CODED), You will need to analyse data from uploaded file by user and update it everytime user uploaded a file:**
- pay periods: 
- salary tiers: 


### 5.4 Expenses Tab — Overview (update it everytime user uploaded file with newest analysis on the file)

**Purpose:** expense summary across period of time from uploaded file by user.

**Components:**
- Hero line chart: monthly totals for period of time from uploaded file by user.
- x stat cards: months spend, interest+fees total, balance drop, total payments
- x-month combined donut chart with legend
- Month-on-month grouped bar chart (x categories × x months)
- Balance trend line chart (4 data points)
- Payments received vs spending grouped bar chart

**Data (NOT HARD-CODED), You will need to analyse data from uploaded file by user and update it everytime user uploaded a file:**

| Month | Total Spend | Credits |
|---|---|---|


### 5.5 Expenses Tab — Per-Month Statements (update it everytime user uploaded file with newest analysis on the file)

**Purpose:** Detailed breakdown of each monthly credit card statement.

**month:**
- Hero horizontal bar chart (categories sorted by size)
- Alert: large one-offs 
- 5 stat cards
- Weekly bar chart (full width)
- Category summary table 
- Credit block (recieved payments or any refund by rows)


### 5.6 Expenses Tab — Insights

**Purpose:** Cross-statement pattern analysis.

**Components:**
- 
1 green milestone alert
- 6 insight cards colour-coded by theme (green, indigo, amber, blue, red, teal)

### 5.7 Forecast Tab (Dynamic)

**Purpose:** Auto-generated rolling forecast based on all committed historical months.

**Forecast logic:**
- **Fixed recurring categories** (education, utilities, fitness, subscriptions): forecast = last committed month's actual for each named merchant
- **Variable categories** (groceries, dining, transport, health): forecast = rolling 2-month average across `HISTORICAL_MONTHS`
- **Retail/one-off**: explicitly excluded from forecast
- Forecast rebuilds automatically each time `commitUpload()` is called

**Components:**
- Info alert explaining forecast methodology
- Dynamic column headers with month labels
- Forecast blocks per category (rebuilt from `RECURRING_ITEMS` + `HISTORICAL_MONTHS`)
- Dynamic grand total bar
- 2-column chart grid:
  - Forecast by category (bar)
  - Monthly trend + forecast (line, dashed amber for forecast point)

**Data sources:**
- `HISTORICAL_MONTHS[]` — pre-seeded with Jan/Feb/Mar, grows with uploads
- `RECURRING_ITEMS{}` — named merchant actuals for fixed-cost categories

### 5.9 Upload Tab

**Purpose:** Import new bank statements to extend the report.

**Supported formats:**
- NAB PDF statements (via PDF.js)
- Any CSV export from internet banking

**Upload flow:**

1. **File selection:** drag-and-drop or click on upload zone
2. **Format detection:** `.pdf` → PDF path; otherwise → CSV path
3. **PDF parsing (NAB-specific):**
   - PDF.js extracts text per page
   - Groups text items by Y coordinate (rounded to nearest 2px) to reconstruct visual rows
   - Sorts rows top-to-bottom (PDF Y is bottom-up → sort descending)
   - Regex extracts statement period: `Statement Period DD MMM YY-DD MMM YY`
   - Transaction regex: `DD/MM/YY DD/MM/YY VNNNNN <description> <amount> [CR]`
   - `CR` suffix indicates a credit
4. **CSV parsing:**
   - Header row auto-detected
   - Column mapper UI shown (date, amount, description dropdowns)
   - Headers auto-mapped by keyword matching (`/date|time/`, `/amount|debit|credit/`, `/desc|narr|merchant/`)
5. **Auto-categorization (4-tier pipeline):**
   - Tier 1: Exact match against `merchantCache` (normalised key)
   - Tier 2: Substring match — each cache key checked against full description (longest key wins)
   - Tier 3: Keyword rules (`CAT_KW` object, 11 categories with keyword arrays)
   - Tier 4: Gemini API (`gemini-2.5-flash`) for unknowns — sends unique uncategorised descriptions, returns JSON mapping
6. **Preview:** table shows all transactions with editable category dropdowns and source badges
7. **Upload stats:** 4 mini-cards (total charges, credits, largest charge, top category)
8. **Commit:**
   - Learns merchant→category mappings to `merchantCache` + `localStorage`
   - Updates monthly expense line chart (new data point)
   - Updates month-on-month compare chart (new dataset)
   - Injects new statement sub-tab + full analysis view (mirroring historical months statment style)
   - Pushes month into `HISTORICAL_MONTHS[]`
   - Rebuilds dynamic Forecast tab
   - Rebuild dynamic advirory tab
   - rebuild dydnamic income tab
   - Shows upload history card

### 5.9 Merchant Categorization Engine

**Normalization function (`normMerchant`):**
- Lowercase, replace `*` with space
- Remove non-alphanumeric except spaces
- Strip common stop-words: `pty, ltd, the, and, of, au, com, www, online, store, australia, vic, nsw, qld, wa, sa`
- Collapse whitespace, filter words shorter than 3 chars, take first 3 words

**Category keyword rules (13 categories, ~120 keywords):**
- `mortgage`, `education`, `groceries`, `dining`, `fitness`, `transport`, `utilities`, `subscriptions`, `health`, `retail`, `fees`
- Pre-seeded with ~50 known merchant→category mappings covering Jan/Feb/Mar merchants

**Persistence:** `localStorage` key `nabBudget_mc` — JSON array of `[key, category]` pairs

---

## 6. Data Model

### 6.1 Transaction Object
```
{
  date:      string,    // "DD/MM/YY"
  desc:      string,    // raw merchant description
  amount:    number,    // always positive
  isCredit:  boolean,   // true = payment/refund
  category:  string,    // one of ALL_CATS
  catSource: string     // 'history' | 'auto' | 'ai' | 'new' | 'manual'
}
```

### 6.2 Historical Month Object
```
{
  label:    string,           // "January"
  short:    string,           // "Jan"
  total:    number,           // total charges
  credits:  number,           // total credits received
  cats:     { [cat]: number } // spend per category
  merchants?: { [key]: number } // (added at upload time, normalised merchant totals)
}
```

### 6.3 Recurring Item Object
```
{
  name:    string,              // display name
  actuals: { [month]: number }  // e.g. { Feb: 829.73, Mar: 859.73 }
}
```

### 6.4 Category Constants
```
ALL_CATS = ['education','groceries','dining','fitness','transport',
            'utilities','subscriptions','health','retail','fees',
            'mortgage','income','other']
```

### 6.5 Chart Data (Pre-seeded)

**Fortnightly pay (17 periods):**
Sep 2025–Apr 2026. Three tiers: $2,715.33, $2,902.13, $2,989.64.

**Monthly income (8 months):**
Sep 2025–Apr 2026. Dec 2025 ($8,146) and Apr 2026 ($6,215.49) elevated due to extra pays/back-pay.

**Monthly expenses (Jan–Mar 2026):**
Jan: $10,154 · Feb: $3,598 · Mar: $3,915

**NAB balance timeline:**
Jan 13 open: $14,825 → Feb 12: $15,383 → Mar 12: $15,102 → Apr 13: $6,336

---

## 7. Charts Inventory

| Chart ID | Tab / Sub-tab | Type | Data |
|---|---|---|---|
| `fortnightlyChart` | Income | Line | x FN pays |
| `monthlyIncomeChart` | Income | Bar | x-month income |
| `incomeVsMortgageChart` | Income | Line (dual) | Income vs mortgage |
| `payRiseStepsChart` | Income | Stepped line | FN pay tiers |
| `monthlyExpenseChart` | Expenses - Overview | Line | Monthly totals (dynamic) |
| `donutChart` | Expenses - Overview | Doughnut | x-month category split |
| `compareChart` | Expenses - Overview | Bar (grouped) | Month vs month (dynamic) |
| `trendChart` | Expenses - Overview | Line | NAB balance trend |
| `pmtsChart` | Expenses - Overview | Bar (grouped) | Payments vs charges |
| `febDonut` | Expenses - Feb | Doughnut | Feb category split |
| `weekChart` | Expenses - Feb | Bar | Feb weekly spend |
| `marChart` | Expenses - Mar | Bar (horizontal) | Mar by category |
| `marWeekChart` | Expenses - Mar | Bar | Mar weekly spend |
| `forecastChart` | Expenses - Apr Forecast | Bar | Static recurring forecast |
| `realityDonut` | Advisory | Doughnut | Current budget % of income |
| `recommendedChart` | Advisory | Bar (grouped) | Actual vs recommended % |
| `targetBudgetChart` | Advisory | Bar | Target allocation |
| `fcBreakdownChart` | Forecast | Bar | Dynamic forecast by category |
| `fcTrendChart` | Forecast | Line | Actuals + dashed forecast |

**Chart.js global config:**
- Font: Plus Jakarta Sans
- Tooltip: dark `#0F172A` background, custom title + body fonts
- Tooltip border: `rgba(255,255,255,0.06)`, 10px corner radius

---

## 8. External Dependencies

| Dependency | Version | Purpose | Load method |
|---|---|---|---|
| Chart.js | 4.4.1 | All charts | CDN UMD bundle |
| PDF.js | 3.11.174 | NAB PDF parsing | CDN (main + worker) |
| Google Fonts | — | Plus Jakarta Sans + JetBrains Mono | CSS import |
| Gemini API | gemini-2.5-flash | AI merchant categorization | Fetch (API key hardcoded) |

**Security concern:** The Gemini API key is hardcoded in the HTML source (`GEMINI_KEY`). In a rebuilt component-based app this must be moved to an environment variable or proxied through a backend.

---

## 9. Non-Functional Requirements

### 9.1 Current State
- **Fully client-side:** No server, no database, no authentication
- **Data persistence:** `localStorage` only (merchant cache). All financial data and chart data lost on page refresh after uploads
- **Privacy:** No login, no data leaves browser (except Gemini API calls with merchant descriptions)
- **Performance:** All charts render synchronously at page load (~20 Chart.js instances). PDF parsing is async
- **Accessibility:** No ARIA labels, no keyboard navigation for tabs, no focus management

### 9.2 Known Limitations (to address in rebuild)

| Issue | Description |
|---|---|
| No data persistence | Uploaded statements lost on page refresh — stored only in Chart.js dataset objects |
| Single file | ~1,950 lines of HTML/CSS/JS in one file — unmaintainable at scale |
| Hardcoded API key | Gemini key visible in browser source |
| No state management | Tab state not reflected in URL — refreshing always lands on Advisory |
| No theming | Colors defined in CSS but not linked to any system-wide token file |
| Missing error states | Charts render with stale/empty data if uploads fail partway |

---

## 10. Page Navigation Context

The Budget1 page sits within the broader personal site:

```
index.html
├── EL1.HTML            (Resume vault)
├── BrainDump.html      (AI brain dump / Eisenhower matrix)
├── Budget1.html         ← this page
├── Property_sale_calculator.html
└── rba_cash_rate_history_3.html
```

Budget1.html includes both the shared site nav and its own page-specific nav. A rebuilt version should pull the site nav from a shared layout component.

---

## 11. Rebuild Considerations for Component-Based Architecture

### Recommended component breakdown:

```
/components
  /layout
    SiteNav.tsx           ← shared across all pages
    Footer.tsx
  /budget
    BudgetHeader.tsx      ← gradient header with hpills + balance card
    BudgetNav.tsx         ← tab nav bar (Advisory/Income/Expenses/Forecast/Upload)
    BudgetSubNav.tsx      ← sub-tabs for Expenses section
  /charts
    HeroChart.tsx         ← wrapper with gradient top bar
    StatCard.tsx          ← reusable colored stat card
    ChartBox.tsx          ← standard chart container
    ChartGrid.tsx         ← 2-col responsive grid
  /advisory
    AdvisoryTab.tsx
    BudgetAnalysisTable.tsx
    InsightCard.tsx
    ActionPlan.tsx
  /income
    IncomeTab.tsx
  /expenses
    ExpensesTab.tsx
    StatementView.tsx     ← reusable per-month view (Jan/Feb/Mar/uploaded)
    CreditBlock.tsx
    ForecastBlock.tsx     ← static Apr forecast view
    InsightsView.tsx
  /forecast
    ForecastTab.tsx       ← dynamic forecast
    ForecastBlock.tsx     ← category block (shared with Apr view)
  /upload
    UploadTab.tsx
    UploadZone.tsx
    ColumnMapper.tsx
    TransactionPreview.tsx
    UploadStats.tsx
  /shared
    Alert.tsx
    DataTable.tsx
    StatusPill.tsx
    GrandTotal.tsx
    CategoryDot.tsx

/lib
  categorize.ts           ← merchant normalizer + 4-tier pipeline
  forecast.ts             ← forecast algorithm
  parseNAB.ts             ← NAB PDF transaction parser (PDF.js)
  parseCSV.ts             ← generic CSV parser
  gemini.ts               ← Gemini API client

/data
  categories.ts           ← ALL_CATS, CAT_COLORS_MAP, CAT_KW
  historicalMonths.ts     ← Jan/Feb/Mar seed data
  recurringItems.ts       ← named merchant recurring data
  incomeSeries.ts         ← fortnightly + monthly income arrays
  advisory.ts             ← advisory analysis data (budget table rows, action items)
```

### State management needs:
- Currently active tab + sub-tab (URL hash or router)
- `HISTORICAL_MONTHS[]` — grows with uploads (needs sessionStorage or IndexedDB for persistence)
- Merchant cache — already uses `localStorage`
- Chart references — needed for dynamic updates on upload
- Upload pipeline state — current file, parsed transactions, preview mode

### Chart library:
Chart.js 4.x is the current implementation. In a component-based rebuild, consider wrapping in `react-chartjs-2` or switching to Recharts/Victory if using React, or Chart.js directly via `ref` with cleanup on unmount.
