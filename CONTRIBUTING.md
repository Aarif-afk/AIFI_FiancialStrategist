# Contributing to Finance Consultant Agent

Thank you for your interest in contributing! This project welcomes contributions from developers, finance professionals, and enthusiasts.

## How to Contribute

### 1. For Developers

**Add new features:**
- [ ] Fork the repository
- [ ] Create a feature branch: `git checkout -b feature/your-feature`
- [ ] Make your changes
- [ ] Test thoroughly
- [ ] Commit with clear messages: `git commit -m "Add: XYZ feature"`
- [ ] Push to fork: `git push origin feature/your-feature`
- [ ] Create a Pull Request with description

**Suggested improvements:**
- Web UI (Flask/FastAPI/Streamlit)
- Additional metrics calculations
- Industry-specific scenarios (SaaS, Manufacturing, Retail)
- Better PDF conversion methods
- Real-time market data integration
- Mobile app
- Slack/Teams integration

### 2. For Finance Professionals

**Improve benchmarks:**
- Add industry-specific financial benchmarks
- Validate DIO/DSO/DPO calculations
- Suggest peer comparison data

**Share analyses:**
- Run on public companies
- Create case studies
- Submit pull requests with examples

### 3. For Everyone

**Report bugs:**
- Open an issue with clear description
- Include error message and steps to reproduce
- Attach screenshots if relevant

**Suggest improvements:**
- Open a discussion or issue
- Describe the problem and proposed solution
- Add any supporting data

## Development Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourname/finance-consultant-agent.git
cd finance-consultant-agent

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
pip install -r dev-requirements.txt  # Optional dev tools

# 4. Test the agent
# Open in VS Code and test with sample data
```

## Code Style

- **Python:** Follow PEP 8
- **Markdown:** Use clear headers and formatting
- **Commits:** Use conventional commits (`fix:`, `feat:`, `docs:`, etc.)

## Pull Request Process

1. **Fork** the repository
2. **Create a branch** with descriptive name
3. **Make changes** with clear commit messages
4. **Test thoroughly** before submitting
5. **Write/update documentation** if needed
6. **Submit PR** with:
   - Clear title describing the change
   - Detailed description of what and why
   - Screenshots if UI changes
   - Reference to related issues

## Project Structure

```
finance-consultant-agent/
├── .github/agents/              # VS Code Agent
├── docs/                        # Documentation
├── templates/                   # Report templates
├── scripts/                     # Python utilities
├── examples/                    # Case studies
└── tests/                       # Unit tests (if adding)
```

## Feedback & Questions

- **Repository:** [github.com/Aarif-afk/AIFI_FiancialStrategist](https://github.com/Aarif-afk/AIFI_FiancialStrategist)
- Open a GitHub Discussion for questions
- Open an Issue for bugs or feature requests

---

**Thank you for contributing!** 🚀
