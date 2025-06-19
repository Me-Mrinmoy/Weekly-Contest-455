class Solution:
    def generateTag(self, caption):
        # Step 1: Split into words
        words = caption.strip().split()

        if not words:
            return "#"

        # Step 2: CamelCase
        camel_case = words[0].lower()
        for word in words[1:]:
            camel_case += word.capitalize()

        # Step 3: Add '#'
        result = '#' + camel_case

        # Step 4: Remove non-letter characters except first #
        cleaned = '#' + ''.join(ch for ch in result[1:] if ch.isalpha())

        # Step 5: Truncate to 100 characters
        return cleaned[:100]
