# Web-Agents Usage Examples

This document provides practical examples of using the web-agents suite for various academic website development tasks.

## Example 1: Creating a Static Academic Site with Hugo

### Scenario

You want to create a simple academic personal website using Hugo with:

- Home page with research overview
- Publications page from BibTeX file
- Blog section for research updates
- CV page
- Responsive and accessible design

### Invocation

```text
@Web-Conductor

I need to create a static academic website using Hugo with the following features:
- Home page with a brief bio and research overview
- Publications page that pulls from a BibTeX file
- Blog section for research updates
- CV/resume page with downloadable PDF
- Clean, responsive design that works on mobile and desktop
- Accessible (WCAG 2.1 Level AA)
- Optimized for Google Scholar

The site should be deployable to GitHub Pages.
```

### Expected Workflow

1. **Planning Phase**: Web-Plan creates a multi-phase plan:
   - Phase 1: Hugo project setup and configuration
   - Phase 2: Layout and navigation structure
   - Phase 3: Home page implementation
   - Phase 4: Publications page with BibTeX parsing
   - Phase 5: Blog listing and post template
   - Phase 6: CV page with PDF generation
   - Phase 7: Responsive styling
   - Phase 8: Accessibility improvements
   - Phase 9: SEO and metadata
   - Phase 10: GitHub Pages deployment

2. **Implementation**: Web-Implement, Web-Content, and Web-Style execute phases with TDD

3. **Review**: Web-Review validates each phase for WCAG compliance, responsive design, SEO

4. **Preservation**: Each phase documented in `plans/hugo-site/phase-N-preserve.md`

### Key Deliverables

- Hugo site structure with layouts and content
- BibTeX integration with publication listing
- Markdown blog with frontmatter
- Responsive CSS with mobile-first design
- Accessibility attributes (ARIA, semantic HTML)
- Meta tags and Open Graph markup
- GitHub Actions workflow for deployment

---

## Example 2: Building a Next.js Portfolio with MDX Blog

### Scenario

You want a modern, dynamic portfolio using Next.js with:

- Static generation for performance
- MDX blog with code syntax highlighting
- Publication listing with filtering
- Dark mode support
- Tailwind CSS for styling
- Deployment to Vercel

### Invocation

```text
@Web-Conductor

Create a Next.js portfolio site with TypeScript and Tailwind CSS:
- Home page with projects showcase
- MDX-powered blog with syntax highlighting and tag filtering
- Publications page with search/filter capabilities (from JSON or BibTeX)
- Dark mode toggle (respect system preference by default)
- Fully responsive and accessible
- SEO-optimized with proper meta tags
- Deploy to Vercel

Use modern best practices: TypeScript, ESLint, Prettier, component tests.
```

### Expected Workflow

1. **Planning**: Web-Plan evaluates options:
   - **App Router vs Pages Router**: Recommends App Router for modern features
   - **MDX Integration**: next-mdx-remote vs contentlayer
   - **Styling**: Tailwind with CSS custom properties for theming
   - **Testing**: Vitest + React Testing Library + Playwright

2. **Implementation Phases**:
   - Phase 1: Next.js setup with TypeScript and Tailwind
   - Phase 2: Layout components and navigation
   - Phase 3: Home page with project cards
   - Phase 4: MDX blog integration with frontmatter
   - Phase 5: Publication data management and filtering
   - Phase 6: Dark mode implementation
   - Phase 7: Responsive design across breakpoints
   - Phase 8: Meta tags and Open Graph
   - Phase 9: Component tests and E2E tests
   - Phase 10: Vercel deployment configuration

3. **Specialists**:
   - **Web-Implement**: Core React components, routing
   - **Web-Content**: MDX processing, publication data, RSS feed
   - **Web-Style**: Tailwind config, dark mode, design system

### Key Deliverables

- Next.js app with SSG
- MDX blog with syntax highlighting
- Dark mode with system preference detection
- Tailwind-based design system
- Vitest component tests
- Playwright E2E tests
- Lighthouse scores: 90+ across all metrics
- Vercel deployment config

---

## Example 3: Adding Accessibility to Existing Site

### Scenario

You have an existing website that needs accessibility improvements to meet WCAG 2.1 Level AA standards.

### Invocation

```text
@Web-Conductor

Audit and improve accessibility of my existing website to meet WCAG 2.1 Level AA:
- Fix semantic HTML issues
- Add proper ARIA labels where needed
- Ensure keyboard navigation works throughout
- Fix color contrast issues
- Add skip links and focus management
- Test with screen readers (guidance for manual testing)
- Set up automated accessibility testing

The site is built with React and uses CSS Modules for styling.
```

### Expected Workflow

1. **Exploration**: Web-Explore maps component structure

2. **Research**: Web-Research reviews WCAG 2.1 Level AA requirements and React accessibility patterns

3. **Planning**: Web-Plan creates accessibility-focused phases:
   - Phase 1: Semantic HTML audit and fixes
   - Phase 2: ARIA labels and roles
   - Phase 3: Keyboard navigation improvements
   - Phase 4: Color contrast fixes
   - Phase 5: Focus indicators and management
   - Phase 6: Skip links and landmarks
   - Phase 7: Alternative text for images
   - Phase 8: Form accessibility (labels, errors)
   - Phase 9: Automated testing setup (axe-core)
   - Phase 10: Manual testing documentation

4. **Implementation**: Web-Implement fixes components with tests

5. **Review**: Web-Review validates WCAG compliance with axe-core

### Key Deliverables

- Semantic HTML throughout (`<nav>`, `<main>`, `<article>`)
- ARIA labels and roles where semantic HTML insufficient
- Keyboard-accessible navigation
- Focus indicators (visible focus states)
- Color contrast meeting 4.5:1 (normal) and 3:1 (large text)
- Skip to main content link
- Image alt text
- Form labels and error messages
- axe-core integration in Jest/Vitest tests
- Playwright accessibility test suite
- Manual testing checklist

---

## Example 4: Implementing Publication Listing from BibTeX

### Scenario

You have a BibTeX file with 50+ publications and want a filterable, sortable listing on your website.

### Invocation

```text
@Web-Content

I have a publications.bib file with 50+ publications. I need:
- Parse the BibTeX and convert to usable format
- Display as formatted citations (APA or similar style)
- Filter by type (journal, conference, preprint)
- Filter by year
- Sort by date (most recent first)
- Search by title or author
- Link to PDF, DOI, project pages when available
- Schema.org ScholarlyArticle markup for SEO
- Responsive card or list layout

The site uses Next.js with TypeScript. Prefer JSON data file for performance (parse BibTeX at build time).
```

### Expected Workflow

1. **Web-Content** implements:
   - BibTeX parsing script (build-time)
   - Type definitions for publication data
   - Publication data transformation
   - Filtering and sorting logic
   - Publication component with schema markup

2. **Web-Implement** adds:
   - Filter/search UI with tests
   - Responsive publication cards
   - Accessible interactions

3. **Web-Style** creates:
   - Publication card styling
   - Responsive grid layout
   - Filter UI styling

### Key Deliverables

- `scripts/parse-bibtex.js`: Parse BibTeX at build time → `data/publications.json`
- `lib/publications.ts`: Filter, sort, search utilities with tests
- `components/PublicationCard.tsx`: Publication display component
- `components/PublicationList.tsx`: List with filtering UI
- `components/schemas/PublicationSchema.tsx`: JSON-LD markup
- Component tests for filtering and sorting
- Visual regression tests for publication cards
- Responsive design (mobile list, desktop grid)

---

## Example 5: Creating a Responsive Navigation

### Scenario

You need a navigation bar that works well on mobile (hamburger menu) and desktop (horizontal menu) with accessibility.

### Invocation

```text
@Web-Implement

Create an accessible, responsive navigation component:
- Mobile: Hamburger menu that opens a drawer/dropdown
- Desktop: Horizontal menu with links
- Keyboard accessible (Tab navigation, Escape to close)
- ARIA labels for screen readers
- Focus management when opening/closing mobile menu
- Smooth transitions (with reduced motion support)
- Active link highlighting
- Skip to main content link

The site uses React with Tailwind CSS. Write tests for keyboard navigation and responsive behavior.
```

### Expected Workflow

1. **Tests First** (TDD):
   - Mobile menu toggle works
   - Keyboard navigation (Tab, Escape, Enter)
   - Active link styling
   - Focus management
   - Responsive breakpoint switching

2. **Implementation**:
   - Navigation component with mobile/desktop views
   - Hamburger toggle button
   - ARIA labels (`aria-expanded`, `aria-controls`)
   - Focus trap for mobile menu
   - Active link detection

3. **Styling** (Web-Style if needed):
   - Mobile drawer styling
   - Desktop horizontal menu
   - Transitions with `prefers-reduced-motion`
   - Focus states

### Key Deliverables

- `components/Navigation.tsx`: Responsive nav component
- `components/Navigation.test.tsx`: Keyboard and responsive tests
- Mobile hamburger menu (drawer style)
- Desktop horizontal navigation
- ARIA labels and roles
- Focus management (trap when open, restore when closed)
- Skip to main content link
- Smooth transitions (respecting motion preferences)
- Visual regression tests at mobile and desktop

---

## Example 6: Setting Up Visual Regression Testing

### Scenario

You want to catch unintended visual changes in your website with screenshot-based testing.

### Invocation

```text
@Web-Implement

Set up visual regression testing for my Next.js site:
- Use Playwright for screenshot capture
- Test key pages at mobile, tablet, desktop breakpoints
- Test component states (default, hover, focus)
- Test dark mode vs light mode
- Set up CI integration (GitHub Actions)
- Provide approval workflow for intentional changes

Key pages to test: home, publications, blog listing, blog post, CV
```

### Expected Workflow

1. **Setup**:
   - Playwright installation and configuration
   - Test structure for different breakpoints
   - GitHub Actions workflow

2. **Test Implementation**:
   - Page tests at breakpoints (375px, 768px, 1440px)
   - Component tests for states
   - Theme tests (light/dark)

3. **CI Integration**:
   - GitHub Actions to run tests
   - Artifact upload for screenshots
   - Fail on visual changes (require manual approval)

### Key Deliverables

- `playwright.config.ts`: Playwright configuration
- `tests/visual/pages.spec.ts`: Page screenshot tests
- `tests/visual/components.spec.ts`: Component state tests
- `.github/workflows/visual-tests.yml`: CI workflow
- Baseline screenshots in `tests/visual/__screenshots__/`
- Documentation for updating baselines
- PR comment bot with screenshot diffs (optional)

---

## Example 7: Optimizing Performance and Core Web Vitals

### Scenario

Your site is slow and you want to improve Core Web Vitals scores.

### Invocation

```text
@Web-Conductor

My Next.js site has poor Core Web Vitals. Help me optimize:
- LCP is 4+ seconds (target: < 2.5s)
- FID is good
- CLS has issues with layout shifts
- Large JavaScript bundle (500KB+)
- Images not optimized
- No code splitting

Need:
- Image optimization strategy
- Bundle size reduction (code splitting, tree shaking)
- Critical CSS implementation
- Lazy loading for below-fold content
- Fix layout shifts
- Set up Lighthouse CI
```

### Expected Workflow

1. **Audit Phase**: Web-Review audits current performance

2. **Planning**: Web-Plan creates optimization phases:
   - Phase 1: Image optimization (next/image, WebP)
   - Phase 2: Code splitting (dynamic imports)
   - Phase 3: Critical CSS and font loading
   - Phase 4: Layout shift fixes (size attributes)
   - Phase 5: Lazy loading implementation
   - Phase 6: Bundle analysis and tree shaking
   - Phase 7: Lighthouse CI setup

3. **Implementation**: Each phase with before/after measurements

### Key Deliverables

- Optimized images (WebP, proper sizing, lazy loading)
- Code-split bundles (< 200KB initial)
- Critical CSS inlined
- Size attributes on images/videos
- Font loading strategy (`font-display: swap`)
- Dynamic imports for heavy components
- Lighthouse CI in GitHub Actions
- Performance budgets configured
- Core Web Vitals: LCP < 2.5s, FID < 100ms, CLS < 0.1

---

## Example 8: Migrating from Jekyll to Astro

### Scenario

You have an existing Jekyll site and want to migrate to Astro for better performance and modern tooling.

### Invocation

```text
@Web-Conductor

Migrate my existing Jekyll academic site to Astro:

Current site (Jekyll):
- Blog posts in Markdown
- Publications from YAML data file
- Liquid templates for layouts
- SCSS for styling
- Deployed to GitHub Pages

Target (Astro):
- Keep all content (blog posts, publications)
- Convert templates to Astro components
- Modern CSS (Tailwind or CSS Modules)
- Improved performance
- Content collections for better organization
- Keep GitHub Pages deployment

Preserve URLs to avoid breaking links.
```

### Expected Workflow

1. **Exploration**: Web-Explore maps Jekyll structure

2. **Planning**: Web-Plan creates migration strategy:
   - Phase 1: Astro project setup
   - Phase 2: Convert layouts to Astro components
   - Phase 3: Migrate blog posts (Markdown → Content Collections)
   - Phase 4: Convert publications data
   - Phase 5: Styling migration (SCSS → Tailwind/CSS)
   - Phase 6: URL structure preservation
   - Phase 7: Testing and validation
   - Phase 8: GitHub Pages deployment

3. **Implementation**: Phased migration with parallel testing

### Key Deliverables

- Astro project structure
- Converted layouts (Astro components)
- Content collections for blog and publications
- Preserved URL structure (redirects if needed)
- Tailwind CSS styling
- GitHub Actions workflow for Astro
- Side-by-side testing (Jekyll vs Astro)
- Performance improvements measured
- Successful GitHub Pages deployment

---

## Tips for Effective Use

### 1. Be Specific About Requirements

❌ **Vague**: "Make my site better"

✅ **Specific**: "Improve accessibility to WCAG 2.1 Level AA, focusing on color contrast and keyboard navigation"

### 2. Mention Tech Stack Preferences

Include framework, styling approach, deployment target:

```text
@Web-Conductor

Create a portfolio site with:
- Tech: Next.js 14 (App Router), TypeScript, Tailwind CSS
- Content: MDX for blog, JSON for publications
- Deploy: Vercel
- Testing: Vitest for components, Playwright for E2E
```

### 3. Specify Accessibility Requirements

Academic sites often need strong accessibility:

```text
- WCAG 2.1 Level AA compliance
- Screen reader compatible
- Keyboard navigation throughout
- Minimum color contrast ratios
```

### 4. Include SEO Considerations

For academic visibility:

```text
- Schema.org markup for publications (ScholarlyArticle)
- Open Graph tags for social sharing
- Google Scholar optimization
- Meta tags for all pages
```

### 5. Ask for Stress-Testing

Let the agents identify edge cases:

```text
Include stress-testing for:
- Very long publication lists (100+)
- Long paper titles that break layout
- Missing images or data
- Mobile devices with small screens
```

### 6. Request Testing Strategy

Specify testing needs:

```text
Testing requirements:
- Component tests with React Testing Library
- Visual regression with Playwright
- Accessibility tests with axe-core
- E2E tests for critical flows
```

### 7. Think in Phases

For large projects, structure the work:

```text
Phase 1: Basic site structure and navigation
Phase 2: Content management (publications, blog)
Phase 3: Styling and responsive design
Phase 4: Accessibility improvements
Phase 5: Performance optimization
Phase 6: Deployment setup
```

### 8. Leverage Specialists

Call specific agents for focused tasks:

- **@Web-Content**: For publication parsing, blog setup, structured data
- **@Web-Style**: For design systems, theming, responsive layouts
- **@Web-Implement**: For component implementation with tests
- **@Web-Review**: For accessibility audits, code reviews

---

## Common Use Cases

### Quick Reference

| Task | Best Agent | Example Invocation |
|------|------------|-------------------|
| New site from scratch | Web-Conductor | "Create a Hugo academic site with..." |
| BibTeX integration | Web-Content | "Parse publications.bib and create filterable listing" |
| Accessibility audit | Web-Conductor | "Audit site for WCAG 2.1 AA compliance" |
| Responsive navigation | Web-Implement | "Create accessible mobile/desktop navigation" |
| Dark mode | Web-Style | "Implement dark mode with system preference" |
| Performance optimization | Web-Conductor | "Optimize Core Web Vitals" |
| Blog setup | Web-Content | "Set up MDX blog with frontmatter and RSS" |
| Testing setup | Web-Implement | "Configure Vitest and Playwright for testing" |

---

## Next Steps

After creating your site:

1. **Deploy**: GitHub Pages, Vercel, Netlify
2. **Analytics**: Google Analytics, Plausible
3. **Monitoring**: Lighthouse CI, Sentry
4. **Domain**: Set up custom domain
5. **Maintenance**: Regular content updates, dependency updates
6. **SEO**: Submit sitemap to Google Scholar, Google Search Console

For more information, see [web-agents/README.md](README.md) for agent details and capabilities.
