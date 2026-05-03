import pandas as pd
import argparse

def analyze_token_density(csv_file, threshold=20.0):
    """
    Analyzes token density from lexical logs and flags files that are token heavy.
    """
    print(f"Loading lexical logs from {csv_file}...")
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return

    # Check required columns
    required_cols = {'file_name', 'total_tokens', 'total_lines'}
    if not required_cols.issubset(df.columns):
        print(f"Error: CSV must contain columns {required_cols}")
        return

    # Aggregate tokens and lines per file in case of multiple logs per file
    df_agg = df.groupby('file_name')[['total_tokens', 'total_lines']].sum().reset_index()

    # Derive Token_Density (tokens per line)
    # Handle division by zero
    df_agg['Token_Density'] = df_agg.apply(
        lambda row: row['total_tokens'] / row['total_lines'] if row['total_lines'] > 0 else 0,
        axis=1
    )

    # Create flag Is_Token_Heavy
    df_agg['Is_Token_Heavy'] = df_agg['Token_Density'] > threshold

    print("\nLexical Analysis - Token Density Indicator Results:")
    print("-" * 60)
    print(df_agg.to_string(index=False))
    print("-" * 60)

    # Save results
    output_file = 'token_density_results.csv'
    df_agg.to_csv(output_file, index=False)
    print(f"\nResults saved to '{output_file}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate token density from lexical logs.")
    parser.add_argument('--input', type=str, default='lexical_logs.csv', help='Path to input CSV file')
    parser.add_argument('--threshold', type=float, default=20.0, help='Threshold for Is_Token_Heavy flag')
    
    args = parser.parse_args()
    analyze_token_density(args.input, args.threshold)
