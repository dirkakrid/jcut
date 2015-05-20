Prints fields from JSON input. Takes stdin by default, or file(s) with the --file flag.

Why not use jq? The jq syntax for specifying keys with special characters in them is hard to type. I wanted something to use with Bro's JSON logs, which have lots of "." characters in key names.
