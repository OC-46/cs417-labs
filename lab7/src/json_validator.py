from stack import Stack


def validate(json_string):

    stack = Stack()                      # stack to track openers
    line = 1
    col = 0
    errors = []

    # ── STATE FLAG ───────────────────────────────────────────────
    # in_string tracks whether we are currently inside a "quoted
    # string". While True, structural characters like { and [ are
    # just text content — they must be ignored by the validator.
    # This is the key insight that separates a real validator from
    # a naive parentheses checker.
    in_string = False
    quote = '"'
    backslash = '\\'
    skip = False                   # Flag to skip escaped characters
    
    for character in json_string:
        if character == '\n':
            line += 1
            col = 0
            continue                      # move to next character

        col += 1
        
        # ── STRING MODE ──────────────────────────────────────────
        # If we are inside a quoted string, the only characters
        # that matter are:
        #   backslash  → the next char is escaped, skip it
        #   double-quote → this ends the string
        # Everything else is just string content — skip it.
        if in_string:
            # If the previous character was a backslash, skip this character
            if skip:
                skip = False
                continue
            
            if character == backslash:
                skip = True          # Mark to skip the next character
                continue
            elif character == quote:
                in_string = False          # we are leaving the string
            continue                           # either way, move on

        # ── NORMAL MODE ──────────────────────────────────────────
        # We are outside any string. Structural characters matter.

        # Encountering a double-quote means we are entering a string.
        # From this point until the matching closing quote, we must
        # ignore all braces and brackets.
        if character == quote:
            in_string = True
            continue

        # Opening brace/bracket: push it onto the stack along with
        # its location. We store the location so that if this opener
        # is never closed, we can tell the user WHERE it was opened.
        if character == '{' or character == '[':
            stack.push((character, line, col))

        # Closing brace/bracket: this is the core stack operation.
        # Pop the most recent opener and verify it matches this
        # closer. { must match }, [ must match ].
        elif character == '}' or character == ']':
            if stack.is_empty():
                errors.append(f"Unexpected closing '{character}' at line {line}, column {col}")
                return (False, errors)

            open_char, open_line, open_col = stack.pop()
            expected = '}' if open_char == '{' else ']'
            if (open_char == '{' and character != '}') or (open_char == '[' and character != ']'):
                errors.append(f"Expected closing '{expected}' for '{open_char}' opened at line {open_line}, column {open_col}, but found '{character}' at line {line}, column {col}")
                return (False, errors)

    # ── AFTER ALL CHARACTERS ─────────────────────────────────────

    # If we reached the end while still inside a string, the last
    # opening quote was never closed.
    if in_string:
        errors.append(f"Unterminated string at line {line}, column {col}")
        return (False, errors)

    # If the stack still has items, those openers were never closed.
    # Report each one with the location where it was opened.
    if not stack.is_empty():
        while not stack.is_empty():
            open_char, open_line, open_col = stack.pop()
            expected_closer = '}' if open_char == '{' else ']'
            errors.append(f"Unclosed '{open_char}' at line {open_line}, column {open_col} (expected '{expected_closer}')")
        return (False, errors)

    return (True, [])                          # all matched correctly


def validate_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return validate(content)





