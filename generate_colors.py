import json
import re

code1_colors = {
    "surface-container-highest": "#353535", "surface": "#131313", "secondary-fixed-dim": "#c6c6c7",
    "on-tertiary-container": "#454544", "surface-container": "#1f1f1f", "surface-tint": "#e9c349",
    "surface-container-low": "#1b1b1b", "surface-container-high": "#2a2a2a", "surface-bright": "#393939",
    "on-primary-fixed-variant": "#574500", "tertiary-fixed": "#e5e2e1", "tertiary-fixed-dim": "#c8c6c5",
    "primary-container": "#d4af37", "outline-variant": "#4d4635", "primary-fixed-dim": "#e9c349",
    "on-surface-variant": "#d0c5af", "primary": "#f2ca50", "secondary-fixed": "#e2e2e2",
    "surface-dim": "#131313", "on-secondary": "#2f3131", "on-tertiary": "#313030", "on-error": "#690005",
    "secondary-container": "#454747", "inverse-primary": "#735c00", "on-error-container": "#ffdad6",
    "on-tertiary-fixed-variant": "#474746", "on-secondary-container": "#b4b5b5", "inverse-on-surface": "#303030",
    "tertiary": "#d0cdcd", "error-container": "#93000a", "on-tertiary-fixed": "#1c1b1b", "secondary": "#c6c6c7",
    "on-primary-container": "#554300", "on-secondary-fixed-variant": "#454747", "surface-variant": "#353535",
    "primary-fixed": "#ffe088", "on-primary-fixed": "#241a00", "tertiary-container": "#b4b2b2",
    "on-background": "#e2e2e2", "outline": "#99907c", "inverse-surface": "#e2e2e2", "background": "#131313",
    "surface-container-lowest": "#0e0e0e", "on-secondary-fixed": "#1a1c1c", "on-surface": "#e2e2e2",
    "error": "#ffb4ab", "on-primary": "#3c2f00"
}

code2_colors = {
    "on-surface-variant": "#4d4635", "surface": "#fbf8ff", "secondary": "#5e5e5e",
    "on-tertiary-fixed": "#1a1c1c", "on-primary-fixed-variant": "#574500", "background": "#fbf8ff",
    "error": "#ba1a1a", "surface-dim": "#dad9e3", "outline-variant": "#d0c5af",
    "on-secondary-fixed-variant": "#474747", "on-background": "#1a1b22", "primary-fixed-dim": "#e9c349",
    "surface-container-low": "#f4f2fd", "error-container": "#ffdad6", "inverse-on-surface": "#f1effa",
    "surface-container-highest": "#e3e1ec", "tertiary": "#5d5f5f", "tertiary-fixed-dim": "#c6c6c7",
    "surface-container": "#eeedf7", "primary": "#735c00", "outline": "#7f7663", "on-primary": "#ffffff",
    "tertiary-fixed": "#e2e2e2", "on-surface": "#1a1b22", "surface-variant": "#e3e1ec",
    "on-secondary-container": "#646464", "tertiary-container": "#b2b3b3", "on-error-container": "#93000a",
    "on-primary-fixed": "#241a00", "surface-tint": "#735c00", "on-error": "#ffffff",
    "secondary-fixed-dim": "#c6c6c6", "inverse-surface": "#2f3038", "on-secondary": "#ffffff",
    "on-primary-container": "#554300", "inverse-primary": "#e9c349", "surface-container-lowest": "#ffffff",
    "on-secondary-fixed": "#1b1b1b", "secondary-container": "#e2e2e2", "surface-container-high": "#e8e7f1",
    "secondary-fixed": "#e2e2e2", "primary-container": "#d4af37", "on-tertiary": "#ffffff",
    "on-tertiary-container": "#434546", "primary-fixed": "#ffe088", "surface-bright": "#fbf8ff",
    "on-tertiary-fixed-variant": "#454747"
}

all_keys = set(code1_colors.keys()).union(set(code2_colors.keys()))

with open("theme.html", "w") as f:
    f.write("<style>\n:root, .light {\n")
    for k in sorted(all_keys):
        v = code2_colors.get(k, "#000000")
        f.write(f"    --color-{k}: {v};\n")
    f.write("}\n.dark {\n")
    for k in sorted(all_keys):
        v = code1_colors.get(k, "#ffffff")
        f.write(f"    --color-{k}: {v};\n")
    f.write("}\n</style>\n\n<script>\nconst twColors = {\n")
    for k in sorted(all_keys):
        f.write(f'    "{k}": "var(--color-{k})",\n')
    f.write("};\n</script>\n")

