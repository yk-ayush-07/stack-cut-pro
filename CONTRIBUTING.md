# Contributing to Stack Cut Pro

Thank you for your interest in contributing to **Stack Cut Pro**! We welcome community contributions to make AI stream clipping even faster, more accurate, and accessible.

---

## Code of Conduct
Please be respectful, constructive, and collaborative in all discussions and pull requests.

---

## Getting Started

1. **Fork the Repository**:
   Fork the project to your own GitHub account and clone it locally:
   ```bash
   git clone https://github.com/<your-username>/stack-cut-pro.git
   cd stack-cut-pro
   ```

2. **Set up the Environment**:
   Run the automated setup:
   ```bash
   python cli.py setup
   ```
   Or install in development mode:
   ```bash
   pip install -e .
   ```

3. **Verify Your Setup**:
   ```bash
   python cli.py doctor
   ```

---

## Making Changes

1. Create a feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
2. Make your improvements with clean, well-commented Python code.
3. Verify syntax and compilation across scripts:
   ```bash
   python -m compileall scripts/
   ```
4. Commit your changes with clear, descriptive commit messages:
   ```bash
   git commit -m "Add: support for custom caption typography"
   ```
5. Push to your branch and open a Pull Request.

---

## Submitting Pull Requests

- Keep PRs focused on a single concern or feature.
- Ensure all CI tests pass.
- Update documentation in `README.md` if CLI flags or configurations are altered.

---

## Author & Maintainer

**Ayush kumar**
- GitHub: [@yk-ayush-07](https://github.com/yk-ayush-07)
