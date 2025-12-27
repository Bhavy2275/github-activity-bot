# CI/CD Scheduler

This project is an experiment in using **GitHub Actions** and **Python** to automate Git operations and schedule daily recurring tasks.

## How it works
- A GitHub Action workflow (`daily.yml`) runs on a scheduled CRON job.
- It executes a Python script that generates activity logs.
- The script uses `subprocess` to perform git commands (add, commit).
- Changes are pushed back to the repository automatically.

## Purpose
Demonstrating:
- Automated CI/CD pipelines.
- Scheduled cloud execution.
- Programmatic git interaction.
