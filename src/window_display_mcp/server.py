"""
Window Display MCP Server
Three-layer olog architecture for visual merchandising vocabulary

LAYER 1: Pure taxonomy (composition types, focal strategies, lighting frameworks)
LAYER 2: Deterministic parameter mapping (ratios, angles, spatial calculations)
LAYER 3: Image prompt synthesis (geometric specifications for generators)
"""

from fastmcp import FastMCP
from typing import Literal, Optional
import json

mcp = FastMCP("Window Display Visual Merchandising")

# ============================================================================
# LAYER 1: CATEGORICAL TAXONOMY
# ============================================================================

COMPOSITION_TYPES = {
    "pyramidal": {
        "description": "Stable hierarchical arrangement with apex focal point",
        "eye_movement": "upward_convergent",
        "stability": "high",
        "typical_ratios": {"base_width": 1.0, "apex_height": 0.618},
        "retail_contexts": ["luxury", "aspirational", "hero_product"]
    },
    "step_progression": {
        "description": "Zigzag or stair-step creating guided left-to-right scan",
        "eye_movement": "sequential_horizontal",
        "stability": "medium",
        "typical_ratios": {"step_height": 0.15, "step_depth": 0.20},
        "retail_contexts": ["storytelling", "product_range", "seasonal_narrative"]
    },
    "radial": {
        "description": "Elements emanating from central focal point",
        "eye_movement": "outward_from_center",
        "stability": "dynamic",
        "typical_ratios": {"center_zone": 0.25, "radiation_angle": 45},
        "retail_contexts": ["celebration", "abundance", "variety"]
    },
    "isolation": {
        "description": "Single element in negative space for maximum impact",
        "eye_movement": "immediate_focal_lock",
        "stability": "very_high",
        "typical_ratios": {"negative_space": 0.70, "focal_offset": 0.382},
        "retail_contexts": ["ultra_luxury", "museum_quality", "iconic_statement"]
    },
    "repetition": {
        "description": "Rhythmic pattern creating visual momentum",
        "eye_movement": "scanning_rhythm",
        "stability": "medium",
        "typical_ratios": {"unit_spacing": 0.12, "pattern_repeat": 5},
        "retail_contexts": ["mass_appeal", "variety", "abundance"]
    },
    "triangular_cluster": {
        "description": "Three focal points forming stable triangle composition",
        "eye_movement": "triangular_scan",
        "stability": "high",
        "typical_ratios": {"spacing": 0.30, "vertex_angle": 60},
        "retail_contexts": ["collection", "coordinated_set", "balanced_variety"]
    }
}

DEPTH_STAGING = {
    "compressed_2d": {
        "description": "Flat graphic composition maximizing window glass plane",
        "depth_zones": 1,
        "viewing_distance": "close_inspection",
        "spatial_compression": 0.95
    },
    "theatrical_depth": {
        "description": "Strong foreground/midground/background separation",
        "depth_zones": 3,
        "viewing_distance": "street_level_15ft",
        "spatial_compression": 0.30
    },
    "forced_perspective": {
        "description": "Exaggerated depth using scale manipulation",
        "depth_zones": 4,
        "viewing_distance": "dramatic_distance_20ft",
        "spatial_compression": 0.15
    },
    "shallow_focus": {
        "description": "Photography-style depth with clear focal plane",
        "depth_zones": 2,
        "viewing_distance": "intimate_6ft",
        "spatial_compression": 0.60
    }
}

LIGHTING_FRAMEWORKS = {
    "accent_dramatic": {
        "description": "High-contrast accent spots creating sculptural shadows",
        "key_angle": 35,
        "key_intensity_ratio": 4.0,
        "fill_ratio": 0.25,
        "color_temperature": 3200,
        "shadow_quality": "hard_defined"
    },
    "soft_luxury": {
        "description": "Even diffuse lighting with subtle modeling",
        "key_angle": 45,
        "key_intensity_ratio": 2.0,
        "fill_ratio": 0.60,
        "color_temperature": 4500,
        "shadow_quality": "soft_graduated"
    },
    "theatrical_uplight": {
        "description": "Low-angle uplighting for drama and monumentality",
        "key_angle": -25,
        "key_intensity_ratio": 5.0,
        "fill_ratio": 0.15,
        "color_temperature": 2900,
        "shadow_quality": "theatrical_elongated"
    },
    "cool_modern": {
        "description": "Daylight-balanced cross-lighting for dimensionality",
        "key_angle": 55,
        "key_intensity_ratio": 3.0,
        "fill_ratio": 0.40,
        "color_temperature": 5600,
        "shadow_quality": "crisp_natural"
    },
    "ambient_even": {
        "description": "Shadowless illumination for pure color and form",
        "key_angle": 0,
        "key_intensity_ratio": 1.2,
        "fill_ratio": 0.90,
        "color_temperature": 4000,
        "shadow_quality": "minimal"
    }
}

SIGHT_LINE_GEOMETRY = {
    "street_pedestrian": {
        "description": "Typical adult walking at sidewalk distance",
        "viewing_angle": 25,
        "viewing_distance_ft": 8,
        "eye_height_in": 64,
        "optimal_focal_height": 0.55
    },
    "passing_vehicle": {
        "description": "Driver or passenger in moving car",
        "viewing_angle": 15,
        "viewing_distance_ft": 20,
        "eye_height_in": 52,
        "optimal_focal_height": 0.50
    },
    "close_inspection": {
        "description": "Stopped viewer examining details",
        "viewing_angle": 45,
        "viewing_distance_ft": 3,
        "eye_height_in": 64,
        "optimal_focal_height": 0.60
    },
    "elevated_view": {
        "description": "Second-floor or elevated walkway perspective",
        "viewing_angle": -20,
        "viewing_distance_ft": 15,
        "eye_height_in": 120,
        "optimal_focal_height": 0.35
    }
}

# ============================================================================
# LAYER 1 TOOLS: PURE TAXONOMY LOOKUP
# ============================================================================

@mcp.tool()
def list_composition_types() -> str:
    """
    List all window display composition types with their characteristics.
    
    LAYER 1: Pure taxonomy lookup (0 tokens)
    
    Returns: JSON with composition types, eye movement patterns, and retail contexts
    """
    return json.dumps({
        "composition_types": COMPOSITION_TYPES,
        "count": len(COMPOSITION_TYPES),
        "layer": "taxonomy",
        "cost_tokens": 0
    }, indent=2)

@mcp.tool()
def get_composition_specifications(
    composition_type: Literal[
        "pyramidal", "step_progression", "radial", 
        "isolation", "repetition", "triangular_cluster"
    ]
) -> str:
    """
    Get detailed specifications for a composition type.
    
    LAYER 1: Pure taxonomy lookup (0 tokens)
    
    Args:
        composition_type: Type of window display composition
        
    Returns: Complete specifications including ratios and contexts
    """
    specs = COMPOSITION_TYPES.get(composition_type)
    
    return json.dumps({
        "composition_type": composition_type,
        "specifications": specs,
        "layer": "taxonomy",
        "cost_tokens": 0
    }, indent=2)

@mcp.tool()
def list_lighting_frameworks() -> str:
    """
    List all lighting framework types for window displays.
    
    LAYER 1: Pure taxonomy lookup (0 tokens)
    
    Returns: JSON with lighting types, angles, ratios, and shadow qualities
    """
    return json.dumps({
        "lighting_frameworks": LIGHTING_FRAMEWORKS,
        "count": len(LIGHTING_FRAMEWORKS),
        "layer": "taxonomy",
        "cost_tokens": 0
    }, indent=2)

@mcp.tool()
def get_sight_line_geometry(
    viewer_context: Literal[
        "street_pedestrian", "passing_vehicle", 
        "close_inspection", "elevated_view"
    ]
) -> str:
    """
    Get sight line geometry for specific viewer context.
    
    LAYER 1: Pure taxonomy lookup (0 tokens)
    
    Args:
        viewer_context: Type of viewer and viewing situation
        
    Returns: Viewing angles, distances, and optimal focal placement
    """
    geometry = SIGHT_LINE_GEOMETRY.get(viewer_context)
    
    return json.dumps({
        "viewer_context": viewer_context,
        "geometry": geometry,
        "layer": "taxonomy",
        "cost_tokens": 0
    }, indent=2)

# ============================================================================
# LAYER 2: DETERMINISTIC PARAMETER MAPPING
# ============================================================================

def calculate_golden_ratio_offset(dimension: float, use_minor: bool = False) -> float:
    """Calculate golden ratio offset from dimension."""
    phi = 1.618033988749895
    if use_minor:
        return dimension * (1 / phi)  # 0.618...
    return dimension * (phi - 1)  # 0.382...

def calculate_viewing_cone(
    window_width_ft: float,
    window_height_ft: float,
    viewing_distance_ft: float,
    viewing_angle_deg: float
) -> dict:
    """Calculate effective viewing cone and optimal focal zones."""
    import math
    
    # Convert angle to radians
    angle_rad = math.radians(viewing_angle_deg)
    
    # Calculate visible height based on viewing angle
    effective_height = window_height_ft * math.cos(angle_rad)
    
    # Calculate horizontal field of view
    horizontal_fov = 2 * math.atan(window_width_ft / (2 * viewing_distance_ft))
    horizontal_fov_deg = math.degrees(horizontal_fov)
    
    # Optimal focal zone (center 40% of window)
    focal_zone_left = window_width_ft * 0.30
    focal_zone_right = window_width_ft * 0.70
    focal_zone_bottom = window_height_ft * 0.35
    focal_zone_top = window_height_ft * 0.65
    
    return {
        "effective_height_ft": round(effective_height, 2),
        "horizontal_fov_deg": round(horizontal_fov_deg, 1),
        "focal_zone_coords": {
            "left_ft": round(focal_zone_left, 2),
            "right_ft": round(focal_zone_right, 2),
            "bottom_ft": round(focal_zone_bottom, 2),
            "top_ft": round(focal_zone_top, 2)
        },
        "viewing_angle_impact": "compressed" if abs(viewing_angle_deg) > 30 else "natural"
    }

def _map_display_parameters_internal(
    window_width_ft: float,
    window_height_ft: float,
    composition_type: str,
    depth_staging: str,
    lighting_framework: str,
    viewer_context: str
) -> dict:
    """Internal version that returns dict directly (for use by other tools)."""
    # Get taxonomy data
    comp_specs = COMPOSITION_TYPES[composition_type]
    depth_specs = DEPTH_STAGING[depth_staging]
    light_specs = LIGHTING_FRAMEWORKS[lighting_framework]
    sight_specs = SIGHT_LINE_GEOMETRY[viewer_context]
    
    # Calculate viewing geometry
    viewing_cone = calculate_viewing_cone(
        window_width_ft,
        window_height_ft,
        sight_specs["viewing_distance_ft"],
        sight_specs["viewing_angle"]
    )
    
    # Calculate focal point based on composition
    if composition_type == "pyramidal":
        focal_x = window_width_ft * 0.50  # Center
        focal_y = window_height_ft * comp_specs["typical_ratios"]["apex_height"]
    elif composition_type == "isolation":
        focal_x = window_width_ft * calculate_golden_ratio_offset(1.0)
        focal_y = window_height_ft * sight_specs["optimal_focal_height"]
    elif composition_type == "radial":
        focal_x = window_width_ft * 0.50
        focal_y = window_height_ft * 0.50
    elif composition_type == "triangular_cluster":
        focal_x = window_width_ft * calculate_golden_ratio_offset(1.0)
        focal_y = window_height_ft * 0.55
    else:
        focal_x = window_width_ft * 0.50
        focal_y = window_height_ft * sight_specs["optimal_focal_height"]
    
    # Calculate negative space ratio
    if composition_type == "isolation":
        negative_space_ratio = comp_specs["typical_ratios"]["negative_space"]
    elif composition_type == "repetition":
        negative_space_ratio = 0.20
    else:
        negative_space_ratio = 0.40
    
    # Depth zone calculations
    if depth_specs["depth_zones"] == 3:
        depth_zones = {
            "foreground": {"distance_ft": 1.0, "scale": 1.0},
            "midground": {"distance_ft": 3.5, "scale": 0.75},
            "background": {"distance_ft": 6.0, "scale": 0.50}
        }
    elif depth_specs["depth_zones"] == 2:
        depth_zones = {
            "focal_plane": {"distance_ft": 2.0, "scale": 1.0},
            "background": {"distance_ft": 5.0, "scale": 0.70}
        }
    else:
        depth_zones = {
            "single_plane": {"distance_ft": 0.5, "scale": 1.0}
        }
    
    return {
        "window_dimensions": {
            "width_ft": window_width_ft,
            "height_ft": window_height_ft,
            "aspect_ratio": round(window_width_ft / window_height_ft, 2)
        },
        "composition": {
            "type": composition_type,
            "primary_focal_point": {
                "x_ft": round(focal_x, 2),
                "y_ft": round(focal_y, 2),
                "x_normalized": round(focal_x / window_width_ft, 3),
                "y_normalized": round(focal_y / window_height_ft, 3)
            },
            "eye_movement_pattern": comp_specs["eye_movement"],
            "negative_space_ratio": negative_space_ratio
        },
        "depth_staging": {
            "strategy": depth_staging,
            "zones": depth_zones,
            "spatial_compression": depth_specs["spatial_compression"]
        },
        "lighting": {
            "framework": lighting_framework,
            "key_light_angle_deg": light_specs["key_angle"],
            "intensity_ratio": light_specs["key_intensity_ratio"],
            "fill_ratio": light_specs["fill_ratio"],
            "color_temperature_k": light_specs["color_temperature"],
            "shadow_quality": light_specs["shadow_quality"]
        },
        "viewing_geometry": {
            "viewer_context": viewer_context,
            "viewing_angle_deg": sight_specs["viewing_angle"],
            "viewing_distance_ft": sight_specs["viewing_distance_ft"],
            "eye_height_in": sight_specs["eye_height_in"],
            "viewing_cone": viewing_cone
        }
    }

@mcp.tool()
def map_display_parameters(
    window_width_ft: float,
    window_height_ft: float,
    composition_type: Literal[
        "pyramidal", "step_progression", "radial", 
        "isolation", "repetition", "triangular_cluster"
    ],
    depth_staging: Literal[
        "compressed_2d", "theatrical_depth", 
        "forced_perspective", "shallow_focus"
    ],
    lighting_framework: Literal[
        "accent_dramatic", "soft_luxury", "theatrical_uplight",
        "cool_modern", "ambient_even"
    ],
    viewer_context: Literal[
        "street_pedestrian", "passing_vehicle",
        "close_inspection", "elevated_view"
    ]
) -> str:
    """
    Map window display parameters to geometric specifications.
    
    LAYER 2: Deterministic calculation (0 tokens)
    
    Args:
        window_width_ft: Window width in feet
        window_height_ft: Window height in feet
        composition_type: Display composition structure
        depth_staging: Depth arrangement strategy
        lighting_framework: Lighting approach
        viewer_context: Target viewer situation
        
    Returns: Complete geometric specifications for image generation
    """
    result = _map_display_parameters_internal(
        window_width_ft,
        window_height_ft,
        composition_type,
        depth_staging,
        lighting_framework,
        viewer_context
    )
    result["layer"] = "deterministic_mapping"
    result["cost_tokens"] = 0
    
    return json.dumps(result, indent=2)

# ============================================================================
# LAYER 3: IMAGE PROMPT SYNTHESIS
# ============================================================================

@mcp.tool()
def generate_display_prompt(
    window_width_ft: float,
    window_height_ft: float,
    composition_type: Literal[
        "pyramidal", "step_progression", "radial",
        "isolation", "repetition", "triangular_cluster"
    ],
    depth_staging: Literal[
        "compressed_2d", "theatrical_depth",
        "forced_perspective", "shallow_focus"
    ],
    lighting_framework: Literal[
        "accent_dramatic", "soft_luxury", "theatrical_uplight",
        "cool_modern", "ambient_even"
    ],
    viewer_context: Literal[
        "street_pedestrian", "passing_vehicle",
        "close_inspection", "elevated_view"
    ],
    subject_description: str,
    style_modifier: str = ""
) -> str:
    """
    Generate image generation prompt with geometric specifications.
    
    LAYER 3: Synthesis (this is where you'd call LLM for creative enhancement)
    
    For this demo, generates structured prompt from deterministic parameters.
    In production, this would be the single LLM call for creative synthesis.
    
    Args:
        window_width_ft: Window width in feet
        window_height_ft: Window height in feet
        composition_type: Display composition structure
        depth_staging: Depth arrangement strategy
        lighting_framework: Lighting approach
        viewer_context: Target viewer situation
        subject_description: What products/elements to display
        style_modifier: Optional style guidance (e.g., "minimalist", "baroque")
        
    Returns: Complete image generation prompt with geometric specifications
    """
    # Get deterministic parameters (Layer 2) using internal function
    params = _map_display_parameters_internal(
        window_width_ft,
        window_height_ft,
        composition_type,
        depth_staging,
        lighting_framework,
        viewer_context
    )
    
    # Build geometric prompt
    comp = params["composition"]
    depth = params["depth_staging"]
    light = params["lighting"]
    view = params["viewing_geometry"]
    
    # Composition instructions
    comp_instruction = f"{composition_type.replace('_', ' ')} composition"
    focal_instruction = (
        f"primary focal point at {comp['primary_focal_point']['x_normalized']:.2f} "
        f"horizontal × {comp['primary_focal_point']['y_normalized']:.2f} vertical "
        f"(measured from bottom-left)"
    )
    
    # Depth instructions
    if depth["strategy"] == "theatrical_depth":
        depth_instruction = (
            "strong foreground/midground/background separation with "
            f"30% spatial compression, foreground at 1.0× scale, "
            f"midground at 0.75× scale, background at 0.50× scale"
        )
    elif depth["strategy"] == "compressed_2d":
        depth_instruction = "flat composition maximizing window glass plane, minimal depth cues"
    elif depth["strategy"] == "shallow_focus":
        depth_instruction = "photography-style depth with clear focal plane at 2ft, background at 5ft with 70% scale"
    else:
        depth_instruction = f"{depth['strategy'].replace('_', ' ')} with {depth['spatial_compression']:.0%} compression"
    
    # Lighting instructions
    if light["key_light_angle_deg"] < 0:
        light_direction = f"uplighting from {abs(light['key_light_angle_deg'])}° below horizontal"
    else:
        light_direction = f"key light from {light['key_light_angle_deg']}° above horizontal"
    
    light_instruction = (
        f"{light_direction}, {light['intensity_ratio']:.1f}:1 intensity ratio to ambient fill, "
        f"{light['color_temperature_k']}K color temperature, {light['shadow_quality'].replace('_', ' ')} shadows"
    )
    
    # Viewing geometry instructions
    view_instruction = (
        f"composed for {view['viewer_context'].replace('_', ' ')} perspective at "
        f"{view['viewing_angle_deg']}° viewing angle from {view['viewing_distance_ft']}ft distance, "
        f"eye height {view['eye_height_in']}in"
    )
    
    # Negative space instruction
    negative_instruction = f"{comp['negative_space_ratio']:.0%} negative space ratio"
    
    # Assemble prompt
    prompt_parts = [
        f"Shop window display photograph: {subject_description}.",
        f"{comp_instruction} with {focal_instruction}.",
        f"{depth_instruction}.",
        f"{light_instruction}.",
        f"{view_instruction}.",
        f"{negative_instruction}, {comp['eye_movement_pattern'].replace('_', ' ')} eye movement pattern."
    ]
    
    if style_modifier:
        prompt_parts.insert(1, f"Style: {style_modifier}.")
    
    prompt = " ".join(prompt_parts)
    
    result = {
        "prompt": prompt,
        "parameters_used": params,
        "subject": subject_description,
        "style_modifier": style_modifier if style_modifier else None,
        "layer": "synthesis",
        "note": "In production, this layer would call LLM for creative enhancement"
    }
    
    return json.dumps(result, indent=2)

# ============================================================================
# PHASE 2.6: NORMALIZED PARAMETER SPACE & RHYTHMIC COMPOSITION
# ============================================================================
# 
# Window display aesthetics mapped to 5D normalized parameter space [0.0, 1.0]
# enabling trajectory computation, rhythmic oscillation, and attractor discovery.
#
# Parameters:
#   compositional_tension  - sparse isolation → dense dynamic arrangement
#   depth_complexity       - flat 2D plane → deep theatrical staging
#   lighting_drama         - soft ambient even → harsh theatrical accent
#   viewing_intimacy       - distant/passing → close/detailed inspection
#   negative_space_ratio   - packed/filled → open/breathable
# ============================================================================

DISPLAY_PARAMETER_NAMES = [
    "compositional_tension",
    "depth_complexity",
    "lighting_drama",
    "viewing_intimacy",
    "negative_space_ratio"
]

# Canonical display states with normalized coordinates
DISPLAY_STATE_COORDINATES = {
    "luxury_isolation": {
        "compositional_tension": 0.10,
        "depth_complexity": 0.40,
        "lighting_drama": 0.35,
        "viewing_intimacy": 0.85,
        "negative_space_ratio": 0.90
    },
    "theatrical_drama": {
        "compositional_tension": 0.55,
        "depth_complexity": 0.85,
        "lighting_drama": 0.90,
        "viewing_intimacy": 0.50,
        "negative_space_ratio": 0.40
    },
    "abundance_wall": {
        "compositional_tension": 0.95,
        "depth_complexity": 0.10,
        "lighting_drama": 0.15,
        "viewing_intimacy": 0.20,
        "negative_space_ratio": 0.10
    },
    "editorial_minimal": {
        "compositional_tension": 0.15,
        "depth_complexity": 0.15,
        "lighting_drama": 0.50,
        "viewing_intimacy": 0.80,
        "negative_space_ratio": 0.85
    },
    "immersive_spectacle": {
        "compositional_tension": 0.75,
        "depth_complexity": 0.95,
        "lighting_drama": 0.95,
        "viewing_intimacy": 0.45,
        "negative_space_ratio": 0.25
    },
    "curated_collection": {
        "compositional_tension": 0.45,
        "depth_complexity": 0.60,
        "lighting_drama": 0.35,
        "viewing_intimacy": 0.55,
        "negative_space_ratio": 0.55
    },
    "narrative_journey": {
        "compositional_tension": 0.60,
        "depth_complexity": 0.70,
        "lighting_drama": 0.65,
        "viewing_intimacy": 0.50,
        "negative_space_ratio": 0.35
    }
}

# Phase 2.6 rhythmic presets: temporal oscillation between display states
DISPLAY_RHYTHMIC_PRESETS = {
    "seasonal_transition": {
        "state_a": "editorial_minimal",
        "state_b": "theatrical_drama",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 24,
        "description": "Smooth seasonal arc from restrained editorial to theatrical grandeur and back"
    },
    "day_night_cycle": {
        "state_a": "curated_collection",
        "state_b": "immersive_spectacle",
        "pattern": "sinusoidal",
        "num_cycles": 4,
        "steps_per_cycle": 20,
        "description": "Daylight curation dissolving into night-time spectacle lighting"
    },
    "intimacy_sweep": {
        "state_a": "abundance_wall",
        "state_b": "luxury_isolation",
        "pattern": "triangular",
        "num_cycles": 2,
        "steps_per_cycle": 30,
        "description": "Linear ramp from packed abundance to solitary luxury focus"
    },
    "drama_pulse": {
        "state_a": "curated_collection",
        "state_b": "immersive_spectacle",
        "pattern": "sinusoidal",
        "num_cycles": 5,
        "steps_per_cycle": 16,
        "description": "Rapid rhythmic pulse between restrained curation and full spectacle"
    },
    "narrative_shift": {
        "state_a": "editorial_minimal",
        "state_b": "narrative_journey",
        "pattern": "square",
        "num_cycles": 4,
        "steps_per_cycle": 12,
        "description": "Hard cuts between minimal editorial and storytelling progression"
    }
}


# ============================================================================
# PHASE 2.7: VISUAL VOCABULARY FOR ATTRACTOR VISUALIZATION
# ============================================================================
#
# Maps parameter coordinates to image-generation-ready keywords via
# nearest-neighbor matching against canonical visual types.
# ============================================================================

DISPLAY_VISUAL_TYPES = {
    "luxury_restraint": {
        "coords": {
            "compositional_tension": 0.10,
            "depth_complexity": 0.30,
            "lighting_drama": 0.35,
            "viewing_intimacy": 0.85,
            "negative_space_ratio": 0.90
        },
        "keywords": [
            "single hero product in vast negative space",
            "soft directional key light with graduated shadows",
            "neutral matte backdrop",
            "precise golden-ratio placement",
            "intimate close-inspection viewing distance",
            "museum-quality isolation pedestal",
            "restrained monochromatic palette"
        ]
    },
    "theatrical_grandeur": {
        "coords": {
            "compositional_tension": 0.60,
            "depth_complexity": 0.85,
            "lighting_drama": 0.90,
            "viewing_intimacy": 0.50,
            "negative_space_ratio": 0.35
        },
        "keywords": [
            "dramatic three-zone depth staging foreground midground background",
            "high-contrast accent spotlights with hard-edged shadows",
            "sculptural uplighting from below at 25 degrees",
            "rich warm color temperature 3200K tungsten glow",
            "pyramidal composition rising to apex focal point",
            "theatrical curtain framing at window edges",
            "street-level pedestrian viewing geometry"
        ]
    },
    "abundance_energy": {
        "coords": {
            "compositional_tension": 0.95,
            "depth_complexity": 0.10,
            "lighting_drama": 0.15,
            "viewing_intimacy": 0.20,
            "negative_space_ratio": 0.10
        },
        "keywords": [
            "dense repetitive product grid filling entire window plane",
            "flat compressed 2D graphic composition",
            "bright even shadowless ambient illumination",
            "rhythmic scanning eye movement pattern",
            "maximum visual density minimal negative space",
            "bold pop-art color saturation",
            "passing-vehicle scale legibility"
        ]
    },
    "editorial_cool": {
        "coords": {
            "compositional_tension": 0.15,
            "depth_complexity": 0.15,
            "lighting_drama": 0.50,
            "viewing_intimacy": 0.80,
            "negative_space_ratio": 0.85
        },
        "keywords": [
            "minimal editorial composition with deliberate asymmetry",
            "crisp daylight-balanced cross-lighting at 5600K",
            "clean white or pale grey backdrop",
            "precise typographic-scale spatial intervals",
            "shallow depth single focal plane",
            "gallery-like negative space surrounding subject",
            "close-inspection detail-revealing perspective"
        ]
    },
    "spectacle_immersion": {
        "coords": {
            "compositional_tension": 0.75,
            "depth_complexity": 0.95,
            "lighting_drama": 0.95,
            "viewing_intimacy": 0.45,
            "negative_space_ratio": 0.25
        },
        "keywords": [
            "radial composition emanating from luminous center",
            "forced-perspective exaggerated depth staging",
            "theatrical uplighting creating monumental scale",
            "warm-to-cool color temperature gradient",
            "immersive wraparound environmental staging",
            "dynamic outward-from-center eye movement",
            "multiple overlapping depth planes"
        ]
    }
}


# ============================================================================
# PHASE 2.6 INTERNAL FUNCTIONS
# ============================================================================

import math

def _generate_oscillation(num_steps: int, num_cycles: float, pattern: str) -> list:
    """Generate oscillation pattern values [0, 1]."""
    result = []
    for i in range(num_steps):
        t = 2 * math.pi * num_cycles * i / num_steps
        if pattern == "sinusoidal":
            val = 0.5 * (1 + math.sin(t))
        elif pattern == "triangular":
            t_norm = (t / (2 * math.pi)) % 1.0
            val = 2 * t_norm if t_norm < 0.5 else 2 * (1 - t_norm)
        elif pattern == "square":
            t_norm = (t / (2 * math.pi)) % 1.0
            val = 0.0 if t_norm < 0.5 else 1.0
        else:
            val = 0.5
        result.append(val)
    return result


def _generate_preset_trajectory(preset_name: str) -> list:
    """
    Generate Phase 2.6 preset trajectory as list of state dicts.

    Returns:
        List of dicts, each mapping parameter names to float values.
        Length = num_cycles × steps_per_cycle.
    """
    config = DISPLAY_RHYTHMIC_PRESETS[preset_name]
    state_a = DISPLAY_STATE_COORDINATES[config["state_a"]]
    state_b = DISPLAY_STATE_COORDINATES[config["state_b"]]

    total_steps = config["num_cycles"] * config["steps_per_cycle"]
    alphas = _generate_oscillation(total_steps, config["num_cycles"], config["pattern"])

    trajectory = []
    for alpha in alphas:
        state = {}
        for p in DISPLAY_PARAMETER_NAMES:
            state[p] = round(state_a[p] * (1 - alpha) + state_b[p] * alpha, 4)
        trajectory.append(state)
    return trajectory


def _extract_visual_vocabulary(state: dict, strength: float = 1.0) -> dict:
    """
    Map parameter coordinates to nearest canonical visual type.

    Uses Euclidean nearest-neighbor in 5D parameter space against
    DISPLAY_VISUAL_TYPES to find the closest visual archetype, then
    returns image-generation-ready keywords.

    Args:
        state: Dict mapping DISPLAY_PARAMETER_NAMES to float values.
        strength: Keyword weight multiplier [0.0, 1.0].

    Returns:
        Dict with nearest_type, distance, keywords, and state echo.
    """
    min_dist = float("inf")
    nearest_type = None

    for type_name, type_def in DISPLAY_VISUAL_TYPES.items():
        coords = type_def["coords"]
        dist_sq = sum(
            (state.get(p, 0.5) - coords.get(p, 0.5)) ** 2
            for p in DISPLAY_PARAMETER_NAMES
        )
        dist = math.sqrt(dist_sq)
        if dist < min_dist:
            min_dist = dist
            nearest_type = type_name

    type_def = DISPLAY_VISUAL_TYPES[nearest_type]

    # Weight keywords by strength (filter if very low)
    if strength < 0.2:
        keywords = type_def["keywords"][:3]
    elif strength < 0.5:
        keywords = type_def["keywords"][:5]
    else:
        keywords = list(type_def["keywords"])

    return {
        "nearest_type": nearest_type,
        "distance": round(min_dist, 4),
        "keywords": keywords,
        "strength": strength,
        "state": state
    }


# ============================================================================
# PHASE 2.6 TOOLS: RHYTHMIC COMPOSITION
# ============================================================================

@mcp.tool()
def list_display_states() -> str:
    """
    List all canonical window display states with their parameter coordinates.

    LAYER 1: Pure taxonomy lookup (0 tokens)

    Returns: All 7 canonical display states in normalized parameter space.
    """
    return json.dumps({
        "display_states": DISPLAY_STATE_COORDINATES,
        "parameter_names": DISPLAY_PARAMETER_NAMES,
        "parameter_semantics": {
            "compositional_tension": "0.0 = sparse isolation, 1.0 = dense dynamic",
            "depth_complexity": "0.0 = flat 2D plane, 1.0 = deep theatrical staging",
            "lighting_drama": "0.0 = soft ambient even, 1.0 = harsh theatrical accent",
            "viewing_intimacy": "0.0 = distant/passing, 1.0 = close/detailed",
            "negative_space_ratio": "0.0 = packed/filled, 1.0 = open/breathable"
        },
        "count": len(DISPLAY_STATE_COORDINATES),
        "layer": "taxonomy",
        "cost_tokens": 0
    }, indent=2)


@mcp.tool()
def list_display_rhythmic_presets() -> str:
    """
    List all Phase 2.6 rhythmic presets for window display temporal composition.

    LAYER 1: Pure taxonomy lookup (0 tokens)

    Returns: Preset configurations with periods, patterns, and descriptions.
    """
    presets_summary = {}
    for name, config in DISPLAY_RHYTHMIC_PRESETS.items():
        presets_summary[name] = {
            "period": config["steps_per_cycle"],
            "total_steps": config["num_cycles"] * config["steps_per_cycle"],
            "pattern": config["pattern"],
            "states": f"{config['state_a']} ↔ {config['state_b']}",
            "description": config["description"]
        }

    return json.dumps({
        "presets": presets_summary,
        "count": len(presets_summary),
        "available_patterns": ["sinusoidal", "triangular", "square"],
        "layer": "taxonomy",
        "cost_tokens": 0
    }, indent=2)


@mcp.tool()
def generate_display_rhythmic_sequence(
    state_a_id: str,
    state_b_id: str,
    oscillation_pattern: str = "sinusoidal",
    num_cycles: int = 3,
    steps_per_cycle: int = 20,
    phase_offset: float = 0.0
) -> str:
    """
    Generate rhythmic oscillation between two window display states.

    PHASE 2.6 TOOL: Temporal composition for display aesthetics.
    Creates periodic transitions cycling between display configurations.

    Args:
        state_a_id: Starting display state (luxury_isolation, theatrical_drama, etc.)
        state_b_id: Alternating display state
        oscillation_pattern: "sinusoidal" | "triangular" | "square"
        num_cycles: Number of complete A→B→A cycles
        steps_per_cycle: Samples per cycle (this is the preset period)
        phase_offset: Starting phase (0.0 = A, 0.5 = B)

    Returns:
        Sequence with states, pattern info, and phase points.

    Cost: 0 tokens (Layer 2 deterministic)
    """
    if state_a_id not in DISPLAY_STATE_COORDINATES:
        return json.dumps({"error": f"Unknown state: {state_a_id}. Available: {list(DISPLAY_STATE_COORDINATES.keys())}"})
    if state_b_id not in DISPLAY_STATE_COORDINATES:
        return json.dumps({"error": f"Unknown state: {state_b_id}. Available: {list(DISPLAY_STATE_COORDINATES.keys())}"})

    state_a = DISPLAY_STATE_COORDINATES[state_a_id]
    state_b = DISPLAY_STATE_COORDINATES[state_b_id]
    total_steps = num_cycles * steps_per_cycle

    alphas = _generate_oscillation(total_steps, num_cycles, oscillation_pattern)

    # Apply phase offset
    if phase_offset > 0:
        offset_steps = int(phase_offset * steps_per_cycle)
        alphas = alphas[offset_steps:] + alphas[:offset_steps]

    sequence = []
    for i, alpha in enumerate(alphas):
        state = {}
        for p in DISPLAY_PARAMETER_NAMES:
            state[p] = round(state_a[p] * (1 - alpha) + state_b[p] * alpha, 4)
        sequence.append({
            "step": i,
            "phase": round(alpha, 4),
            "state": state
        })

    return json.dumps({
        "state_a": state_a_id,
        "state_b": state_b_id,
        "pattern": oscillation_pattern,
        "num_cycles": num_cycles,
        "steps_per_cycle": steps_per_cycle,
        "total_steps": total_steps,
        "period": steps_per_cycle,
        "phase_offset": phase_offset,
        "sequence": sequence,
        "layer": "deterministic_composition",
        "cost_tokens": 0
    }, indent=2)


@mcp.tool()
def apply_display_rhythmic_preset(
    preset_name: str
) -> str:
    """
    Apply a curated Phase 2.6 rhythmic preset for window displays.

    PHASE 2.6 CONVENIENCE TOOL: Pre-configured display oscillation patterns.

    Available Presets:
    - seasonal_transition: editorial_minimal ↔ theatrical_drama (period 24)
    - day_night_cycle: curated_collection ↔ immersive_spectacle (period 20)
    - intimacy_sweep: abundance_wall ↔ luxury_isolation (period 30)
    - drama_pulse: curated_collection ↔ immersive_spectacle (period 16)
    - narrative_shift: editorial_minimal ↔ narrative_journey (period 12)

    Args:
        preset_name: Name of the preset to apply.

    Returns:
        Complete rhythmic sequence with all intermediate states.

    Cost: 0 tokens (Layer 2 deterministic)
    """
    if preset_name not in DISPLAY_RHYTHMIC_PRESETS:
        return json.dumps({
            "error": f"Unknown preset: {preset_name}",
            "available": list(DISPLAY_RHYTHMIC_PRESETS.keys())
        })

    config = DISPLAY_RHYTHMIC_PRESETS[preset_name]
    trajectory = _generate_preset_trajectory(preset_name)

    return json.dumps({
        "preset": preset_name,
        "description": config["description"],
        "state_a": config["state_a"],
        "state_b": config["state_b"],
        "pattern": config["pattern"],
        "period": config["steps_per_cycle"],
        "num_cycles": config["num_cycles"],
        "total_steps": len(trajectory),
        "trajectory": trajectory,
        "layer": "deterministic_composition",
        "cost_tokens": 0
    }, indent=2)


# ============================================================================
# PHASE 2.7 TOOLS: ATTRACTOR VISUALIZATION & PROMPT GENERATION
# ============================================================================

@mcp.tool()
def extract_display_visual_vocabulary(
    state: dict,
    strength: float = 1.0
) -> str:
    """
    Extract visual vocabulary from window display parameter coordinates.

    PHASE 2.7 TOOL: Maps a 5D parameter state to the nearest canonical
    display visual type and returns image-generation-ready keywords.

    Uses nearest-neighbor matching against 5 visual archetypes derived
    from the window display taxonomy.

    Args:
        state: Parameter coordinates dict with keys:
            compositional_tension, depth_complexity, lighting_drama,
            viewing_intimacy, negative_space_ratio
        strength: Keyword weight multiplier [0.0, 1.0] (default 1.0)

    Returns:
        Dict with nearest_type, distance, keywords, and state echo.

    Cost: 0 tokens (pure Layer 2 computation)
    """
    result = _extract_visual_vocabulary(state, strength)
    result["layer"] = "deterministic_mapping"
    result["cost_tokens"] = 0
    return json.dumps(result, indent=2)


@mcp.tool()
def generate_display_attractor_prompt(
    preset_name: str = "",
    custom_state: Optional[dict] = None,
    mode: str = "composite",
    style_modifier: str = "",
    keyframe_count: int = 4
) -> str:
    """
    Generate image prompt from display attractor state or preset trajectory.

    PHASE 2.7 TOOL: Translates display parameter coordinates into
    visual prompts suitable for image generation (ComfyUI, Stable Diffusion,
    DALL-E, etc.).

    Modes:
        composite: Single blended prompt from a single parameter state
        sequence: Multiple keyframe prompts extracted from a preset trajectory

    Args:
        preset_name: Name of a Phase 2.6 preset. Use "" with custom_state
            for arbitrary coordinates.
        custom_state: Optional custom parameter coordinates dict.
            Overrides preset_name if provided.
        mode: "composite" | "sequence"
        style_modifier: Optional prefix (e.g., "photorealistic", "fashion editorial")
        keyframe_count: Number of keyframes for sequence mode (default 4)

    Returns:
        Dict with prompt(s), vocabulary details, and source metadata.

    Cost: 0 tokens (Layer 2 deterministic)
    """
    if mode == "sequence":
        # Sequence mode: extract keyframes from preset trajectory
        if not preset_name or preset_name not in DISPLAY_RHYTHMIC_PRESETS:
            return json.dumps({
                "error": f"Sequence mode requires valid preset_name. Available: {list(DISPLAY_RHYTHMIC_PRESETS.keys())}"
            })

        trajectory = _generate_preset_trajectory(preset_name)
        total = len(trajectory)
        step_size = max(1, total // keyframe_count)
        indices = [min(i * step_size, total - 1) for i in range(keyframe_count)]

        keyframes = []
        for idx in indices:
            state = trajectory[idx]
            vocab = _extract_visual_vocabulary(state)
            prompt_parts = []
            if style_modifier:
                prompt_parts.append(style_modifier)
            prompt_parts.append("Shop window display photograph:")
            prompt_parts.extend(vocab["keywords"])
            keyframes.append({
                "step": idx,
                "state": state,
                "vocabulary": vocab,
                "prompt": ", ".join(prompt_parts)
            })

        config = DISPLAY_RHYTHMIC_PRESETS[preset_name]
        return json.dumps({
            "mode": "sequence",
            "preset": preset_name,
            "description": config["description"],
            "period": config["steps_per_cycle"],
            "keyframe_count": len(keyframes),
            "keyframes": keyframes,
            "layer": "deterministic_mapping",
            "cost_tokens": 0
        }, indent=2)

    else:
        # Composite mode: single prompt from one state
        if custom_state:
            state = custom_state
            source = "custom_state"
        elif preset_name and preset_name in DISPLAY_STATE_COORDINATES:
            state = DISPLAY_STATE_COORDINATES[preset_name]
            source = f"canonical_state:{preset_name}"
        elif preset_name and preset_name in DISPLAY_RHYTHMIC_PRESETS:
            # Use midpoint of preset trajectory
            trajectory = _generate_preset_trajectory(preset_name)
            state = trajectory[len(trajectory) // 2]
            source = f"preset_midpoint:{preset_name}"
        else:
            return json.dumps({
                "error": "Provide custom_state dict or valid preset_name/state name.",
                "available_states": list(DISPLAY_STATE_COORDINATES.keys()),
                "available_presets": list(DISPLAY_RHYTHMIC_PRESETS.keys())
            })

        vocab = _extract_visual_vocabulary(state)
        prompt_parts = []
        if style_modifier:
            prompt_parts.append(style_modifier)
        prompt_parts.append("Shop window display photograph:")
        prompt_parts.extend(vocab["keywords"])
        prompt = ", ".join(prompt_parts)

        return json.dumps({
            "mode": "composite",
            "source": source,
            "prompt": prompt,
            "vocabulary": vocab,
            "layer": "deterministic_mapping",
            "cost_tokens": 0
        }, indent=2)


@mcp.tool()
def generate_display_sequence_prompts(
    preset_name: str,
    keyframe_count: int = 4,
    style_modifier: str = ""
) -> str:
    """
    Generate keyframe prompts from a Phase 2.6 display rhythmic preset.

    PHASE 2.7 TOOL: Extracts evenly-spaced keyframes from a rhythmic
    oscillation sequence and generates an image prompt for each.

    Useful for:
    - Storyboard generation from rhythmic display compositions
    - Animation keyframe specification for window display transitions
    - Multi-panel visualization of seasonal or day/night display cycles

    Args:
        preset_name: Phase 2.6 preset (seasonal_transition, day_night_cycle, etc.)
        keyframe_count: Number of keyframes to extract (default 4)
        style_modifier: Optional style prefix for all prompts

    Returns:
        Dict with keyframes, each containing step, state, prompt, and vocabulary.

    Cost: 0 tokens (Layer 2 deterministic)
    """
    # Delegate to the main attractor prompt tool in sequence mode
    return generate_display_attractor_prompt(
        preset_name=preset_name,
        mode="sequence",
        style_modifier=style_modifier,
        keyframe_count=keyframe_count
    )


@mcp.tool()
def compute_display_state_distance(
    state_a_id: str,
    state_b_id: str
) -> str:
    """
    Compute Euclidean distance between two canonical display states.

    LAYER 2: Pure distance computation (0 tokens)

    Args:
        state_a_id: First display state name
        state_b_id: Second display state name

    Returns:
        Distance value and per-parameter breakdown.
    """
    if state_a_id not in DISPLAY_STATE_COORDINATES:
        return json.dumps({"error": f"Unknown state: {state_a_id}. Available: {list(DISPLAY_STATE_COORDINATES.keys())}"})
    if state_b_id not in DISPLAY_STATE_COORDINATES:
        return json.dumps({"error": f"Unknown state: {state_b_id}. Available: {list(DISPLAY_STATE_COORDINATES.keys())}"})

    a = DISPLAY_STATE_COORDINATES[state_a_id]
    b = DISPLAY_STATE_COORDINATES[state_b_id]

    components = {}
    total_sq = 0.0
    for p in DISPLAY_PARAMETER_NAMES:
        diff = b[p] - a[p]
        components[p] = round(diff, 4)
        total_sq += diff ** 2

    distance = math.sqrt(total_sq)

    return json.dumps({
        "state_a": state_a_id,
        "state_b": state_b_id,
        "euclidean_distance": round(distance, 4),
        "parameter_differences": components,
        "layer": "deterministic_computation",
        "cost_tokens": 0
    }, indent=2)


# ============================================================================
# UPDATED SERVER INFO
# ============================================================================

@mcp.tool()
def get_server_info() -> str:
    """Get information about the Window Display MCP server."""
    return json.dumps({
        "name": "Window Display Visual Merchandising MCP",
        "version": "0.2.0",
        "description": "Shop window display composition, lighting, and aesthetic dynamics vocabulary",
        "architecture": "Three-layer olog pattern + Phase 2.6/2.7 dynamics",
        "layers": {
            "layer_1": "Pure taxonomy (composition types, lighting frameworks, sight lines, display states)",
            "layer_2": "Deterministic parameter mapping (geometric calculations, rhythmic composition, vocabulary extraction)",
            "layer_3": "Image prompt synthesis (structured prompts, attractor visualization)"
        },
        "cost_optimization": "Layers 1-2 are zero-cost deterministic operations",
        "domains": [
            "Visual merchandising",
            "Retail display",
            "Product photography",
            "Commercial composition"
        ],
        "phase_2_6_enhancements": {
            "rhythmic_composition": True,
            "parameter_names": DISPLAY_PARAMETER_NAMES,
            "canonical_states": list(DISPLAY_STATE_COORDINATES.keys()),
            "rhythmic_presets": {
                name: {
                    "period": cfg["steps_per_cycle"],
                    "pattern": cfg["pattern"],
                    "states": f"{cfg['state_a']} ↔ {cfg['state_b']}"
                }
                for name, cfg in DISPLAY_RHYTHMIC_PRESETS.items()
            },
            "preset_periods": sorted(set(
                cfg["steps_per_cycle"] for cfg in DISPLAY_RHYTHMIC_PRESETS.values()
            ))
        },
        "phase_2_7_enhancements": {
            "attractor_visualization": True,
            "visual_types": list(DISPLAY_VISUAL_TYPES.keys()),
            "prompt_modes": ["composite", "sequence"]
        },
        "composition_types": list(COMPOSITION_TYPES.keys()),
        "lighting_frameworks": list(LIGHTING_FRAMEWORKS.keys()),
        "depth_staging_options": list(DEPTH_STAGING.keys()),
        "viewer_contexts": list(SIGHT_LINE_GEOMETRY.keys())
    }, indent=2)

if __name__ == "__main__":
    mcp.run()
