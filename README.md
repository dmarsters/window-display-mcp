# Window Display Visual Merchandising MCP Server

Shop window display composition and lighting vocabulary system following three-layer olog architecture.

## Architecture

**Layer 1: Pure Taxonomy (0 tokens)**
- Composition types (pyramidal, radial, isolation, etc.)
- Lighting frameworks (dramatic, luxury, theatrical, etc.)
- Depth staging strategies
- Sight line geometry

**Layer 2: Deterministic Mapping (0 tokens)**
- Geometric calculations (focal points, viewing cones)
- Golden ratio offsets
- Spatial compression ratios
- Light angle and intensity calculations

**Layer 3: Synthesis (LLM cost)**
- Structured image generation prompts
- Geometric specifications for composition
- Creative enhancement layer

## Tools

### Layer 1 (Taxonomy)
- `list_composition_types` - All composition structures
- `get_composition_specifications` - Detailed specs for one type
- `list_lighting_frameworks` - All lighting approaches
- `get_sight_line_geometry` - Viewing angle specifications

### Layer 2 (Deterministic)
- `map_display_parameters` - Calculate all geometric specifications

### Layer 3 (Synthesis)
- `generate_display_prompt` - Create image generation prompt

## Example Usage

```python
# Get composition taxonomy
result = list_composition_types()

# Calculate parameters for specific display
params = map_display_parameters(
    window_width_ft=10.0,
    window_height_ft=8.0,
    composition_type="pyramidal",
    depth_staging="theatrical_depth",
    lighting_framework="accent_dramatic",
    viewer_context="street_pedestrian"
)

# Generate image prompt
prompt = generate_display_prompt(
    window_width_ft=10.0,
    window_height_ft=8.0,
    composition_type="isolation",
    depth_staging="shallow_focus",
    lighting_framework="soft_luxury",
    viewer_context="close_inspection",
    subject_description="luxury watch on velvet cushion",
    style_modifier="minimalist modern"
)
```

## Domain Expertise

Based on century-old visual merchandising principles:
- Baum's "Show Window" (1900)
- Modern retail design standards
- Professional visual merchandising certifications
- Sight line engineering principles
- Golden ratio composition theory

## Cost Optimization

~60-85% cost savings vs pure LLM approach:
- Layers 1-2: Zero inference cost (pure taxonomy + math)
- Layer 3: Single LLM call for creative synthesis

## Installation

```bash
pip install -e .
```

## Local Testing

```bash
python -m window_display_mcp
```

## FastMCP Cloud Deployment

Entry point: `src/window_display_mcp/server.py:mcp`
