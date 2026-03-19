# Contributing to Alternative Coffee Intelligence

Thank you for your interest in contributing to Alternative Coffee Intelligence! 🎉☕

This document provides guidelines for contributing to this project.

---

## 🎯 How to Contribute

### Types of Contributions We Welcome

1. **Reference Files**
   - Additional domain expertise (roasting, extraction, equipment)
   - Origin-specific deep-dives (Ethiopia, Kenya, Colombia, etc.)
   - Disease/pest identification database

2. **Documentation**
   - Usage examples
   - Tutorial videos/articles
   - Translation to other languages
   - FAQ entries

3. **Bug Reports**
   - Incorrect scientific information
   - Skill execution errors
   - Documentation issues

4. **Feature Requests**
   - New analysis modes
   - Additional knowledge domains
   - Integration suggestions

---

## 🚀 Getting Started

### Prerequisites

- GitHub account
- Familiarity with Git
- Understanding of Claude AI Skills
- Coffee knowledge (for content contributions)

### Development Setup

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/alternative-coffee-intelligence.git
   cd alternative-coffee-intelligence
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

4. **Make your changes**
   - Follow the style guide (see below)
   - Test your changes
   - Update documentation if needed

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add roasting reference file"
   # or
   git commit -m "fix: correct fermentation temperature range"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template

---

## 📝 Style Guide

### Markdown Files

**Headers:**
```markdown
# Top-level (skill name)
## Major sections
### Subsections
#### Details
```

**Lists:**
- Use `-` for unordered lists
- Use `1.` for ordered lists
- Indent nested lists with 2 spaces

**Code blocks:**
````markdown
```bash
# For shell commands
```

```javascript
// For code examples
```
````

**Emphasis:**
- `**bold**` for important terms
- `*italic*` for emphasis
- `` `code` `` for inline code/values

### Content Style

**Alternative Slowbar Voice:**
```
✅ Science-driven (cite mechanisms, not myths)
✅ Farmer-first (consider economics, not just quality)
✅ Honest (acknowledge unknowns, no BS)
✅ Specific (numbers, not adjectives)

❌ No coffee romanticism ("mountain magic")
❌ No vague marketing terms ("exotic", "premium")
❌ No unsupported claims
```

**Scientific Accuracy:**
- Cite mechanisms (physics, chemistry, biology)
- Include ranges (e.g., "160-180°C" not "around 170°C")
- Acknowledge uncertainty ("typically" vs "always")
- Link causes to effects (System Thinking)

**Example — Good:**
```markdown
**First Crack Physics:**
Temperature: 196-205°C (varies by density, variety)
Mechanism: Water vapor + CO2 pressure → cell wall rupture
Bean expansion: 50-100% volume increase
Heat release: Exothermic reaction
```

**Example — Bad:**
```markdown
**First Crack:**
Happens around 200°C when the beans crack and expand.
```

---

## 🧪 Testing Guidelines

### For Reference Files

Before submitting a new reference file (e.g., ROASTING.md):

1. **Scientific accuracy check**
   - Verify all scientific claims
   - Cite sources if possible
   - Check against known coffee science

2. **Completeness check**
   - Coverage of key topics in domain
   - Practical utility (actionable information)
   - System Thinking (cause-effect chains)

3. **Style consistency**
   - Follows Alternative Slowbar voice
   - Uses standard markdown formatting
   - Includes examples

4. **Integration test**
   - Does the skill load the file correctly?
   - Does it enhance responses in that domain?

### For SKILL.md Changes

1. **Test all modes**
   - Each of 8 modes should execute correctly
   - Quality gates should pass
   - System Thinking should be visible

2. **Test edge cases**
   - Ambiguous queries
   - Multi-domain queries
   - Simple vs complex queries

---

## 📋 Pull Request Template

When submitting a PR, please use this template:

```markdown
## Description
[Brief description of changes]

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Related Issue
Closes #[issue-number]

## Changes Made
- [List key changes]
- [One per line]

## Testing
- [ ] Tested locally with Claude.ai
- [ ] Verified scientific accuracy
- [ ] Checked style consistency
- [ ] Updated documentation

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where needed
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests (if applicable)

## Screenshots (if applicable)
[Add screenshots of skill responses]

## Additional Notes
[Any additional context]
```

---

## 🐛 Bug Reports

### Before Submitting

1. **Check existing issues** — Has this been reported?
2. **Verify it's a bug** — Not a misunderstanding of coffee science?
3. **Isolate the problem** — Minimal reproducible example

### Bug Report Template

```markdown
## Bug Description
[Clear description of the bug]

## Steps to Reproduce
1. Install skill
2. Query: "[exact query]"
3. See error/incorrect response

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happened]

## Environment
- Claude.ai version: [e.g., web, mobile]
- Skill version: [e.g., v1.0.0]
- Date: [when did this occur]

## Screenshots/Logs
[If applicable]

## Additional Context
[Any other relevant information]
```

---

## 💡 Feature Requests

### Feature Request Template

```markdown
## Feature Description
[Clear description of the proposed feature]

## Problem It Solves
[What problem does this address?]

## Proposed Solution
[How would this work?]

## Alternatives Considered
[What else did you consider?]

## Additional Context
[Any other relevant information]

## Would You Like to Implement This?
- [ ] Yes, I'd like to work on this
- [ ] No, just suggesting
```

---

## 🔬 Scientific Accuracy

### Sources We Trust

1. **Specialty Coffee Association (SCA)**
   - Brewing standards
   - Cupping protocols
   - Water quality standards

2. **World Coffee Research (WCR)**
   - Genetic information
   - Variety profiles
   - Breeding programs

3. **Coffee Quality Institute (CQI)**
   - Q Grader protocols
   - Defect identification
   - Quality scoring

4. **Academic Journals**
   - Journal of Agricultural and Food Chemistry
   - Food Chemistry
   - Crop Science

5. **Technical Manuals**
   - Roasting software documentation
   - Equipment manufacturer specs
   - Processing guides

### When Citing

```markdown
**Statement:** [Scientific claim]
**Source:** [Citation]

Example:
**Statement:** "Chlorogenic acids degrade during roasting to form quinic acid and caffeic acid."
**Source:** Farah, A. (2012). Coffee Constituents. In Coffee: Emerging Health Effects and Disease Prevention.
```

---

## 📚 Documentation

### Types of Documentation

1. **Reference Files** (VARIETALS.md, PROCESSING.md, etc.)
   - Comprehensive domain knowledge
   - Scientific foundation
   - Practical guidance

2. **Usage Guides** (in docs/)
   - Installation
   - Examples
   - Troubleshooting
   - FAQ

3. **API Documentation**
   - Mode descriptions
   - Input/output formats
   - Integration guides

### Documentation Standards

- Clear, concise language
- Examples for every concept
- Links to related sections
- Keep up-to-date with code changes

---

## 🌍 Translation Guidelines

### Currently Supported Languages

- English (primary)
- Thai (in progress)

### Translation Process

1. **Translate reference files**
   - Keep scientific terms in English
   - Translate explanations
   - Maintain Alternative Slowbar voice

2. **Create language directory**
   ```
   /lang/
     /th/
       SKILL.th.md
       VARIETALS.th.md
       ...
   ```

3. **Update skill loader**
   - Auto-detect language
   - Load appropriate files

4. **Test translations**
   - Verify accuracy
   - Check natural flow
   - Test with native speakers

---

## ✅ Review Process

### What We Look For

1. **Scientific Accuracy**
   - Claims supported by research
   - Mechanisms explained correctly
   - Ranges and numbers accurate

2. **Style Consistency**
   - Alternative Slowbar voice
   - Markdown formatting
   - System Thinking approach

3. **Practical Utility**
   - Actionable information
   - Real-world applicability
   - Clear recommendations

4. **Documentation**
   - README updated
   - Examples included
   - Comments where needed

### Timeline

- **Initial review:** Within 1 week
- **Feedback:** We'll provide specific feedback
- **Iteration:** Work with you to refine
- **Merge:** When all checks pass

---

## 🙏 Recognition

Contributors will be:
- Listed in [`CONTRIBUTORS.md`](./CONTRIBUTORS.md)
- Mentioned in release notes
- Credited in documentation

---

## 📞 Questions?

- **GitHub Discussions:** For general questions
- **GitHub Issues:** For specific problems
- **Email:** your-email@example.com

---

## 🎖️ Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of:
- Experience level
- Gender identity
- Sexual orientation
- Disability
- Personal appearance
- Race or ethnicity
- Age
- Religion

### Our Standards

**Examples of behavior that contributes to a positive environment:**
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Examples of unacceptable behavior:**
- Trolling, insulting/derogatory comments, personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

### Enforcement

Instances of unacceptable behavior may be reported to the project team. All complaints will be reviewed and investigated.

---

**Thank you for contributing to Alternative Coffee Intelligence! ☕🔬**

**Together, we're building the most comprehensive coffee intelligence system in the world.**
