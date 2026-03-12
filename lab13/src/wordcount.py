"""Word counter using argparse."""
import argparse
from collections import Counter


def build_parser():
    """Create and return the argument parser.

    Arguments to define:
        filename    - positional, the text file to analyze
        --ignore-case / -i  - store_true, lowercase all words
        --top / -t          - int, show top N most frequent words (default: None)
        --min-length / -m   - int, only count words with at least this many chars (default: 1)
        --sort-by / -s      - choices ["freq", "alpha"], how to sort top words (default: "freq")
        --reverse / -r      - store_true, reverse the sort order

    Returns:
        argparse.ArgumentParser
    """
    # TODO: Create an ArgumentParser with a description
    # TODO: Add the positional 'filename' argument
    # TODO: Add --ignore-case / -i (action="store_true")
    # TODO: Add --top / -t (type=int, default=None)
    # TODO: Add --min-length / -m (type=int, default=1)
    # TODO: Add --sort-by / -s (choices=["freq", "alpha"], default="freq")
    # TODO: Add --reverse / -r (action="store_true")
    parser = argparse.ArgumentParser(description = "argparse word counter")
    parser.add_argument("filename", help="the text file to analyze")
    parser.add_argument("-i", "--ignore-case", action="store_true", help="lowercase all words")
    parser.add_argument("-t", "--top", type=int, default=None, help="show top N most frequent words")
    parser.add_argument("-m", "--min-length", type=int, default=1, help="only count words with at least this many characters")
    parser.add_argument("-s", "--sort-by", choices=["freq", "alpha"], default="freq", help="how to sort top words")
    parser.add_argument("-r", "--reverse", action="store_true", help="reverse the sort order")
    return parser

def analyze(filepath, ignore_case=False, top=None, min_length=1,
            sort_by="freq", reverse=False):
    """Analyze a text file and return a formatted result string.

    Args:
        filepath: path to the text file
        ignore_case: if True, lowercase all words before counting
        top: if set, show the N most frequent words with counts
        min_length: only count words with at least this many characters
        sort_by: "freq" (by count) or "alpha" (alphabetical) when showing top words
        reverse: if True, reverse the sort order

    Returns:
        str: formatted result

    Raises:
        FileNotFoundError: if the file doesn't exist
    """
    # TODO: Read the file and split into words on whitespace
    # TODO: If ignore_case, lowercase all words
    # TODO: Filter out words shorter than min_length
    # TODO: Count total words
    # TODO: If top is None, return "<filename>: <count> words"
    # TODO: If top is set, find the most frequent words:
    #   - Use Counter(words).most_common() for frequency data
    #   - If sort_by == "alpha", sort alphabetically instead
    #   - If reverse, flip the order
    #   - Take the first 'top' entries
    #   - Return multi-line string:
    #       "<filename>: <count> words\n\nTop <N> words:\n  <word>: <count>\n  ..."
    try:
        with open(filepath, "r") as f:
            text = f.read()
            words = text.split()
            if ignore_case:
                words = [word.lower() for word in words]
            words = [word for word in words if len(word) >= min_length]
            total_count = len(words)
            if top is None:
                return f"{filepath}: {total_count} words"
            else:
                counter = Counter(words)
                if sort_by == "alpha":
                    top_words = sorted(counter.items(), key=lambda x: x[0], reverse=reverse)[:top]
                else:
                    top_words = counter.most_common(top)
                    if reverse:
                        top_words = sorted(top_words, key=lambda x: x[1])
                result_lines = [f"{filepath}: {total_count} words", "", f"Top {top} words:"]
                result_lines += [f"  {word}: {count}" for word, count in top_words]
                return "\n".join(result_lines)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: file '{filepath}' not found")


def main():
    """Build parser, parse args, analyze, print result."""
    # TODO: Build the parser
    # TODO: Parse args
    # TODO: Call analyze with the parsed arguments
    # TODO: Print the result
    parser = build_parser()
    args = parser.parse_args()
    result = analyze(args.filename, args.ignore_case, args.top, args.min_length, args.sort_by, args.reverse)
    print(result)


if __name__ == "__main__":
    main()
