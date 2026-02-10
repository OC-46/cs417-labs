from stack import Stack


def validate(json_string):

    stack = Stack()                      # stack to track openers
    line = 1, 
    col = 0

    # ── STATE FLAG ───────────────────────────────────────────────
    # in_string tracks whether we are currently inside a "quoted
    # string". While True, structural characters like { and [ are
    # just text content — they must be ignored by the validator.
    # This is the key insight that separates a real validator from
    # a naive parentheses checker.
    in_string = False
    for character in json_string:
        col += 1
        if character == '\n':
            line += 1
            col = 0
            continue                      # move to next character

        # ── STRING MODE ──────────────────────────────────────────
        # If we are inside a quoted string, the only characters
        # that matter are:
        #   backslash  → the next char is escaped, skip it
        #   double-quote → this ends the string
        # Everything else is just string content — skip it.
        quote = '"'
        backslash = '\\'
        if in_string is True:
            if character is backslash:
                continue
            elif character is quote:
                in_string = False          # we are leaving the string
            continue                           # either way, move on

        # ── NORMAL MODE ──────────────────────────────────────────
        # We are outside any string. Structural characters matter.

        # Encountering a double-quote means we are entering a string.
        # From this point until the matching closing quote, we must
        # ignore all braces and brackets.
        if character is quote:
            in_string = True
            continue

        # Opening brace/bracket: push it onto the stack along with
        # its location. We store the location so that if this opener
        # is never closed, we can tell the user WHERE it was opened.
        if character is '{' or '[':
            stack.push((character, line, col))


        # Closing brace/bracket: this is the core stack operation.
        # Pop the most recent opener and verify it matches this
        # closer. { must match }, [ must match ].
        elif character is '}' or ']':
            if stack is 0:
                return (False, f"Unexpected closing '{character}' at line {line}, column {col}")

            stack.pop(open_char, open_line, open_col)
            if open_char  != character:
                return (False, f"Expected closing '{expected}' for '{open_char}' opened at line {open_line}, column {open_col}, but found '{character}' at line {line}, column {col}")
            
            open_char, open_line, open_col = stack.pop()

            expected = '}' if open_char is '{' else ']'
            if (open_char is '{' and character is not '}') or (open_char is '[' and character is not ']'):
                return (False, f"Expected closing '{expected}' for '{open_char}' opened at line {open_line}, column {open_col}, but found '{character}' at line {line}, column {col}")
    # ── AFTER ALL CHARACTERS ─────────────────────────────────────

    # If we reached the end while still inside a string, the last
    # opening quote was never closed.
    if in_string is True:
        return (False, f"Unterminated string starting at line {line}, column {col}")
        #REPORT error: unterminated string
        #RETURN failure

    # If the stack still has items, those openers were never closed.
    # Report each one with the location where it was opened.
    if stack is not 0:
        expected_closer = '}' if open_char is '{' else ']'
        for item in stack:
            stack.pop(open_char, open_line, open_col)
        return (False, f"Unclosed '{open_char}' at line {open_line}, column {open_col} (expected '{expected_closer}')")
            #REPORT error: unclosed open_char at (open_line, open_col)
        #RETURN failure

    return (True, "")                          # all matched correctly



