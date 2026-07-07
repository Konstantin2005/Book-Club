#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit import run_audit


def main():
    parser = argparse.ArgumentParser(
        description='Audit an ebook library — extract, compare, and report on all book formats.'
    )
    parser.add_argument(
        'library',
        help='Path to the library root directory'
    )
    parser.add_argument(
        '-o', '--output',
        default=None,
        help='Output directory for reports (default: audit/ inside library)'
    )
    parser.add_argument(
        '--cache',
        default=None,
        help='Cache directory for per-book results (default: <output>/.cache)'
    )
    parser.add_argument(
        '-f', '--force',
        action='store_true',
        help='Re-process all books, ignoring cache'
    )

    args = parser.parse_args()

    try:
        summary = run_audit(
            library_path=args.library,
            output_path=args.output,
            cache_dir=args.cache,
            force=args.force,
        )

        print(f'\nAudit complete.')
        print(f'  Books:         {summary["total"]}')
        print(f'  With content:  {summary["with_content"]}')
        print(f'  With warnings: {summary["with_warnings"]}')
        print(f'  Total warnings: {summary["total_warnings"]}')

    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
