# Workshop Support Materials

This directory contains exercises, solutions, and checkpoints for the ADK + FastAPI workshop.

## Structure

```
.workshop/
├── exercises/          # Hands-on exercises for each step
│   ├── step-1/
│   ├── step-2/
│   └── ...
├── solutions/          # Solution code for exercises
│   ├── step-1/
│   ├── step-2/
│   └── ...
└── checkpoints/        # Git tag information and quick reference
```

## Usage for Students

### If You Get Stuck

1. Check the exercise hints in the YAML file
2. Look at solution code in `.workshop/solutions/step-N/`
3. Checkout the git tag to see working code: `git checkout step-N-agent-name`

### If You Fall Behind

Don't worry! Use git tags to catch up:

```bash
# See all available checkpoints
git tag --list

# Jump to a specific step
git checkout step-3-content-pipeline

# Return to latest
git checkout main
```

## Usage for Instructors

### Before Workshop

1. Verify all exercises have solutions
2. Test git tags work correctly
3. Ensure each step builds successfully

### During Workshop

- Use exercises as optional hands-on time
- Show solutions when reviewing concepts
- Reference git tags when students need to catch up

## Exercise Format

Each exercise folder contains:
- `README.md` - Exercise instructions
- `hints.md` - Step-by-step hints
- Files to modify (if creating new files)

Solutions mirror this structure with completed code.
