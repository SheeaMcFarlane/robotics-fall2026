"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """
    if pattern_name == "rounded_rectangle":
        return [
            Segment(0.22, 0.0, 2.0),
            Segment(0.20, 0.8, 1.9635),
            Segment(0.22, 0.0, 2.0),
            Segment(0.20, 0.8, 1.9635),
            Segment(0.22, 0.0, 2.0),
            Segment(0.20, 0.8, 1.9635),
            Segment(0.22, 0.0, 2.0),
            Segment(0.20, 0.8, 1.9635),
        ]
    elif pattern_name == "l_path":
        return [
            Segment(0.22, 0.0, 3.5),
            Segment(0.22, -0.8, 1.5),
            Segment(0.22, 0.0, 2.5),
        ]
    elif pattern_name == "alternating_arcs":
        return [
            Segment(0.22, -0.8, 1.5),
            Segment(0.22, 0.8, 1.5),
            Segment(0.22, -0.8, 1.5),
            Segment(0.22, 0.8, 1.5),
        ]
    else:
        raise ValueError(f"Unsupported pattern name: {pattern_name}")