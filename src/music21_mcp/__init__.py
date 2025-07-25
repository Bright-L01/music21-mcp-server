"""
music21-mcp-server: Multi-interface music analysis server built on music21.

A professional music analysis server providing MCP Server, HTTP API, CLI tools,
and Python library interfaces for comprehensive music analysis and composition.
"""

__version__ = "1.0.0"
__author__ = "Bright Liu"
__email__ = "brightliu@college.harvard.edu"
__license__ = "MIT"

# Import main service classes for easy access
try:
    from .adapters.python_adapter import create_music_analyzer, create_sync_analyzer
    from .services import MusicAnalysisService

    __all__ = [
        "__version__",
        "__author__",
        "__email__",
        "__license__",
        "MusicAnalysisService",
        "create_sync_analyzer",
        "create_music_analyzer",
    ]
except ImportError:
    # Allow version import even if dependencies aren't installed
    __all__ = [
        "__version__",
        "__author__",
        "__email__",
        "__license__",
    ]
