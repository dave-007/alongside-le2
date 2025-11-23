# Contributing to Alongside LE2

Thank you for your interest in contributing to the Alongside Learning Environment 2!

## How to Contribute

### Reporting Issues

If you encounter any issues or have suggestions:

1. Check if the issue already exists in the GitHub Issues
2. If not, create a new issue with:
   - A clear, descriptive title
   - Steps to reproduce (if it's a bug)
   - Expected vs actual behavior
   - Your environment details (OS, Docker version, VS Code version)

### Suggesting Enhancements

We welcome suggestions for:
- New AI tools and libraries to include
- Improved configuration
- Additional examples
- Documentation improvements

### Contributing Code

1. **Fork the Repository**
   ```bash
   git clone https://github.com/dave-007/alongside-le2.git
   cd alongside-le2
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Add new features or fix bugs
   - Update documentation if needed
   - Add examples if relevant

4. **Test Your Changes**
   - Rebuild the devcontainer
   - Run `./verify_setup.sh` to check installations
   - Test any new functionality

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

6. **Push and Create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a pull request on GitHub.

## Development Guidelines

### Adding New Dependencies

When adding new tools or libraries:

1. **Python packages**: Add to the appropriate `RUN pip install` section in the Dockerfile
2. **.NET packages**: Document in the README with installation instructions
3. **System packages**: Add to the `apt-get install` section
4. **Update verification**: Add checks to `verify_setup.sh`
5. **Update documentation**: Update relevant README files

### Documentation Standards

- Use clear, concise language
- Include code examples where helpful
- Keep examples up-to-date with the latest versions
- Add links to official documentation

### Example Standards

When adding examples:

1. Include a docstring explaining what the example does
2. Handle missing API keys gracefully
3. Include setup instructions in the example README
4. Comment complex code sections
5. Follow Python PEP 8 style guidelines

### Testing

Before submitting:

1. Rebuild the devcontainer from scratch
2. Run the verification script: `./verify_setup.sh`
3. Test your examples
4. Check that all documentation links work

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Other conduct inappropriate in a professional setting

## Questions?

Feel free to:
- Open a GitHub Discussion
- Create an issue labeled "question"
- Reach out to the maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be acknowledged in:
- The project README
- Release notes for significant contributions

Thank you for helping make Alongside LE2 better!
