# Compiler Lexical Analysis - Token Density

This repository contains the solution for **Problem 1: Lexical Analysis – Token Density Indicator**.

## Case Study Background
A compiler development team collects lexical analysis logs containing raw tokens and line numbers for multiple source files. Raw token streams cannot be directly used to analyze code complexity or maintainability.

## Task
Use Python to derive a feature `Token_Density` (tokens per line) and create a flag `Is_Token_Heavy` if the density exceeds a defined threshold (default: 20.0).

## Requirements
- Python 3.x
- Pandas

Install dependencies:
```bash
pip install pandas
```

## Usage
Run the script to analyze the sample lexical logs:

```bash
python token_density.py --input lexical_logs.csv --threshold 20.0
```

The output will be displayed in the console and saved to `token_density_results.csv`.
