# Include all rules, which may be customized later
all

# Customized rules are below
rule 'MD007', :indent => 4
rule 'MD024', :allow_different_nesting => true

# Ignored rules are below
exclude_rule 'MD001' # Header levels should only increment by one level at a time
exclude_rule 'MD013' # Line length
exclude_rule 'MD033' # Inline HTML
exclude_rule 'MD041' # First line in file should be a top level header