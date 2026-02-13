# Web Development Agents

A comprehensive suite of specialized AI agents for web development, tailored for academic websites with focus on responsive design, SEO, accessibility, and modern content management. These agents follow best practices for both static site generators (Hugo, Jekyll, 11ty) and modern frameworks (React, Next.js, Astro).

## Overview

The Web-Agents suite provides orchestrated development workflows with built-in stress-testing and preservation stages for creating high-quality, accessible, and performant academic websites.

### Agent Roster

1. **Web-Conductor**: Orchestrator managing the full development lifecycle
2. **Web-Plan**: Planning with options, tradeoffs, and recommendations
3. **Web-Research**: Web best practices and framework research
4. **Web-Explore**: Fast codebase exploration and pattern discovery
5. **Web-Implement**: Frontend implementation with responsive design
6. **Web-Review**: Web standards, accessibility, and performance validation
7. **Web-Content**: Content management specialist for academic websites
8. **Web-Style**: Styling and design system specialist

## Development Workflow

### Standard Lifecycle

```text
Planning → Stress-Test → Implementation → Review → Preserve → Commit
```

**Key Stages:**

1. **Planning**: Web-Plan creates comprehensive plans with implementation options
2. **Stress-Test**: Automatically identify cross-browser issues, responsive breakpoints, accessibility concerns
3. **Implementation**: Web-Implement follows TDD with responsive-first approach
4. **Review**: Web-Review validates WCAG compliance, performance, SEO
5. **Preserve**: Document decisions, assumptions, verifications for traceability
6. **Commit**: User commits with generated message, cycle repeats for next phase

### Stress-Testing

Built-in stress-testing at planning and implementation stages:

- **Cross-Browser**: Chrome, Firefox, Safari, Edge compatibility
- **Responsive Design**: Mobile, tablet, desktop breakpoints and edge cases
- **Accessibility**: WCAG 2.1 Level AA compliance, screen reader compatibility
- **SEO**: Meta tags, schema.org markup, semantic HTML, performance
- **Performance**: Core Web Vitals, bundle size, loading optimization
- **Content Edge Cases**: Long titles, missing images, empty states

### Preservation & Traceability

After each phase, preservation documents capture:

- **Decisions Made**: What approaches were chosen and why
- **Assumptions**: What was assumed and how validated
- **Verifications**: What was tested and how
- **Trade-offs**: What was sacrificed and why

Format: `plans/<task>/phase-<N>-preserve.md`

## Agent Details

### Web-Conductor (Orchestrator)

**Model**: Claude Sonnet 4.5

**Role**: Manages the full development lifecycle, coordinates all subagents

**When to Use**: Start here for any multi-phase web development task

**Key Features**:

- Context-aware delegation to specialized subagents
- Built-in stress-testing coordination
- Preservation stage after each phase
- User approval gates at critical points

**Invocation**:

```text
@Web-Conductor

I need to create a responsive academic portfolio site with a publications page that pulls from BibTeX, a blog section, and a CV page. The site should be accessible and SEO-optimized.
```

### Web-Plan (Planning Agent)

**Model**: Claude Opus 4.6

**Role**: Creates comprehensive implementation plans with options and tradeoffs

**Key Features**:

- Presents 2-3 options for major design decisions (SSG vs framework, styling approach)
- Includes stress-test considerations (responsive, accessibility, performance)
- Specifies test strategy (component, visual regression, accessibility)
- Addresses SEO and performance requirements
- Markdownlint-compliant plans

**Typical Output**:

- Multi-phase plan (3-10 phases)
- Implementation options with pros/cons
- Stress-test considerations
- Accessibility checklist
- SEO optimization checklist

### Web-Research (Research Agent)

**Model**: GPT-5.2

**Role**: Gathers web best practices, framework documentation, accessibility standards

**Key Features**:

- Researches framework patterns (React, Next.js, Astro, Hugo, Jekyll)
- Consults WCAG guidelines and accessibility best practices
- Identifies responsive design patterns and mobile considerations
- Provides SEO optimization strategies
- Delegates to Web-Explore for codebase discovery

**Example Tasks**:

- Research Next.js static generation for academic sites
- Find best practices for accessible navigation patterns
- Investigate BibTeX parsing and rendering approaches
- Compare CSS-in-JS vs Tailwind vs vanilla CSS

### Web-Explore (Exploration Agent)

**Model**: Claude Haiku 4.5

**Role**: Fast codebase exploration and pattern discovery

**Key Features**:

- Parallel search strategy (semantic, grep, file search)
- Understands web project structures (components, pages, layouts, styles)
- Recognizes routing patterns and content organization
- Maps dependencies quickly
- Read-only operation (safe exploration)

**Output Format**:

```xml
<results>
<files>
- /path/to/file.tsx: Brief relevance note
</files>
<answer>
Explanation of what was found
</answer>
<next_steps>
- Actionable step 1
- Actionable step 2
</next_steps>
</results>
```

### Web-Implement (Implementation Agent)

**Model**: Claude Sonnet 4.5

**Role**: Implements frontend code with TDD and responsive design

**Key Features**:

- Strict TDD workflow (red → green → refactor)
- Mobile-first responsive design
- Semantic HTML and accessibility attributes
- SEO-friendly markup and meta tags
- Component testing and visual regression
- Type-safe implementations (TypeScript)

**Quality Checks**:

- `npm run build` (successful production build)
- `npm run lint` (ESLint)
- `npm run test` (unit and component tests)
- `npm run type-check` (TypeScript)

### Web-Review (Review Agent)

**Model**: Claude Opus 4.6

**Role**: Validates web standards, accessibility, and performance

**Review Criteria**:

- **Semantic HTML**: Proper element usage, document structure
- **WCAG Compliance**: Level AA accessibility standards
- **Responsive Design**: Mobile, tablet, desktop breakpoints
- **SEO**: Meta tags, Open Graph, schema.org markup
- **Performance**: Bundle size, Core Web Vitals, optimization
- **Cross-Browser**: Chrome, Firefox, Safari, Edge compatibility

**Output**: Structured review with APPROVED / NEEDS_REVISION / FAILED status

### Web-Content (Content Agent)

**Model**: Claude Sonnet 4.5

**Role**: Manages academic content and structured data

**Key Features**:

- Publication management (BibTeX parsing, formatting)
- Blog post and article organization
- CV/resume content and formatting
- Frontmatter and metadata management
- Schema.org structured data for Google Scholar
- Content collections and taxonomies

**Typical Tasks**:

- Parse BibTeX and generate publication listings
- Create blog post templates with proper frontmatter
- Structure CV data for display and download
- Generate JSON-LD for academic profiles

### Web-Style (Styling Agent)

**Model**: Claude Sonnet 4.5

**Role**: Implements styling and design systems

**Key Features**:

- Mobile-first responsive layouts
- CSS architecture (Tailwind, CSS Modules, styled-components)
- Design token management
- Accessibility considerations (contrast, focus states, reduced motion)
- Typography and spacing systems
- Dark mode and theming

**Typical Tasks**:

- Create responsive navigation components
- Implement accessible form styling
- Build design system with consistent spacing
- Optimize typography for readability

## Technology Stack

### Static Site Generators

- **Hugo**: Fast, Go-based, excellent for academic sites
- **Jekyll**: Ruby-based, GitHub Pages native support
- **11ty**: JavaScript-based, flexible, powerful

### Modern Frameworks

- **Next.js**: React-based, SSG/SSR, excellent for portfolios
- **Astro**: Multi-framework, content-focused, fast
- **React**: Component-based, flexible

### Styling

- **Tailwind CSS**: Utility-first, rapid development
- **CSS Modules**: Scoped styling, type-safe
- **Styled Components**: CSS-in-JS, dynamic styling

### Testing

- **Playwright**: E2E and visual regression testing
- **Vitest / Jest**: Unit and component testing
- **axe-core**: Accessibility testing
- **Lighthouse**: Performance and SEO auditing

### Content Management

- **Markdown**: Content authoring
- **MDX**: Markdown with components
- **BibTeX**: Publication management
- **YAML/TOML**: Frontmatter and configuration

## Example Workflows

### Creating a Static Academic Site

```text
@Web-Conductor

I need a static academic website using Hugo with:
- Home page with research overview
- Publications page from BibTeX file
- Blog for research updates
- CV/resume page
- Responsive and accessible
```

### Building a Next.js Portfolio

```text
@Web-Conductor

Create a Next.js portfolio site with:
- Static generation for performance
- Blog with MDX support
- Publication listing with filtering
- Dark mode support
- Tailwind CSS for styling
```

### Adding Accessibility Features

```text
@Web-Conductor

Audit and improve accessibility:
- WCAG 2.1 Level AA compliance
- Screen reader optimization
- Keyboard navigation
- Focus management
- ARIA labels where needed
```

## Best Practices

### Responsive Design

- **Mobile-first approach**: Design for mobile, enhance for desktop
- **Breakpoint strategy**: 640px (sm), 768px (md), 1024px (lg), 1280px (xl)
- **Flexible layouts**: Use flexbox/grid, avoid fixed widths
- **Touch targets**: Minimum 44×44px for interactive elements
- **Text scaling**: Use relative units (rem, em) instead of pixels

### Accessibility

- **Semantic HTML**: Use proper elements (`<nav>`, `<main>`, `<article>`)
- **ARIA**: Add labels and roles when semantic HTML isn't enough
- **Color contrast**: Minimum 4.5:1 for normal text, 3:1 for large text
- **Keyboard navigation**: All interactive elements accessible via keyboard
- **Focus management**: Visible focus indicators, logical tab order
- **Alternative text**: Descriptive alt text for images

### SEO

- **Meta tags**: Title, description, Open Graph, Twitter Cards
- **Structured data**: JSON-LD with schema.org for publications, profiles
- **Semantic HTML**: Proper heading hierarchy, meaningful URLs
- **Performance**: Fast loading improves rankings
- **Content**: Quality, relevant, regularly updated

### Performance

- **Bundle optimization**: Code splitting, tree shaking, lazy loading
- **Image optimization**: WebP format, responsive images, lazy loading
- **Critical CSS**: Inline critical styles, defer non-critical
- **Caching**: Proper cache headers, static asset fingerprinting
- **Core Web Vitals**: LCP < 2.5s, FID < 100ms, CLS < 0.1

## Getting Started

1. Choose your approach:
   - Simple static site → Hugo, Jekyll, or 11ty
   - Dynamic features → Next.js or Astro
   - Maximum flexibility → Custom React setup

2. Invoke **Web-Conductor** with your requirements

3. Review and approve the generated plan

4. Follow the implementation phases

5. Commit each phase after review

6. Deploy to GitHub Pages, Vercel, Netlify, or your hosting platform

## Additional Resources

- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [web.dev](https://web.dev/) - Performance and best practices
- [A11y Project](https://www.a11yproject.com/) - Accessibility checklist
- [Schema.org](https://schema.org/) - Structured data
