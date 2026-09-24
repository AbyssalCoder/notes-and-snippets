## OpenCode — Terminal AI Coding Tool

Open-source terminal-based coding assistant.

### Setup
```bash
go install github.com/opencode-ai/opencode@latest
opencode
```

### Features
- Runs in terminal (TUI interface)
- Supports multiple LLM providers
- File editing with diff preview
- Session history


<!-- updated examples -->

## Gemini CLI — Google's Terminal AI

### Setup
```bash
npm install -g @anthropic-ai/gemini-cli  # placeholder
gemini
```

### Features
- Free with Google account
- 1M token context window
- Can read and edit local files
- Supports extensions (Google Search, etc.)

Huge context window makes it good for analyzing large codebases.

## OpenCommit — AI Commit Messages

Generates meaningful commit messages from your staged changes.

### Setup
```bash
npm install -g opencommit
oco config set OCO_API_KEY=<key>
```

### Usage
```bash
git add .
oco  # generates commit message from diff
```

Follows conventional commit format. Saves time on writing descriptive messages.
